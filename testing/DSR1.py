import pandas as pd
from pathlib import Path
import geopandas as gpd
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(filename='data_processing.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

data_dir = Path("/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/testing/dataSample")
all_data = []

# Get list of files
files = list(data_dir.glob("*.dat"))

# Process each file with a progress bar
for file in tqdm(files, desc="Processing files"):
    try:
        # Read the second line to extract coordinates
        with open(file, "r") as f:
            lines = [next(f) for _ in range(2)]  # Read first 2 lines
        # Parse the second line (split by whitespace)
        metadata = lines[1].strip().split()
        station_id = metadata[0]
        lat = float(metadata[1])
        lon = float(metadata[2])

        # Read precipitation data (skip first 2 rows)
        df = pd.read_csv(file, skiprows=2, sep=r'\s+', engine='python')

        # Drop redundant 'ID' column (already captured in station_id)
        df = df.drop(columns="ID")

        # Melt daily columns into rows (wide-to-long format)
        df_melted = df.melt(
            id_vars=["AÑO", "MES"],
            value_vars=[str(i) for i in range(1, 32)],  # Days 1-31
            var_name="DIA",
            value_name="precipitation"
        )
        df_melted["DIA"] = df_melted["DIA"].astype(int)

        # Add station metadata to the DataFrame
        df_melted["station_id"] = station_id
        df_melted["lat"] = lat
        df_melted["lon"] = lon

        all_data.append(df_melted)
    except Exception as e:
        logging.error(f"Error processing file {file}: {e}")

# Combine all DataFrames
combined = pd.concat(all_data, ignore_index=True)



# Convert to datetime (handle invalid dates)
combined["date"] = pd.to_datetime(
    combined["AÑO"].astype(str) + "-" +
    combined["MES"].astype(str) + "-" +
    combined["DIA"].astype(str),
    errors="coerce"
)

# Drop rows with invalid dates (e.g., February 30)
combined = combined.dropna(subset=["date"])

# Replace -999 with NaN for missing precipitation values
combined["precipitation"] = combined["precipitation"].replace(-999, pd.NA)

# Aggregate by year and station (yearly average)
combined["year"] = combined["date"].dt.year
yearly_avg = combined.groupby(["station_id", "year", "lat", "lon"])["precipitation"].mean().reset_index()

# Create GeoDataFrame with point geometries
gdf = gpd.GeoDataFrame(
    yearly_avg,
    geometry=gpd.points_from_xy(yearly_avg.lon, yearly_avg.lat),
    crs="EPSG:4326"  # WGS84
)

# Reproject to a Spain-friendly CRS (e.g., ETRS89 UTM zone 30N)
gdf = gdf.to_crs("EPSG:25830")