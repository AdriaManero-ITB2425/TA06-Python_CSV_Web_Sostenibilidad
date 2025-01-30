# geospatial.py
import geopandas as gpd
import pandas as pd

def create_geodata():
    df = pd.read_parquet("aggregated_data.parquet")
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df.lon, df.lat),
        crs="EPSG:4326"
    )
    gdf.to_crs("EPSG:25830").to_file("precipitation_data.gpkg", driver="GPKG")

if __name__ == "__main__":
    create_geodata()