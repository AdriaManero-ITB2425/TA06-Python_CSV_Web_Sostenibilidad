import pandas as pd
from pathlib import Path
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(filename='data_processing.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def extract_coordinates(file_path):
    try:
        with open(file_path, "r") as f:
            lines = [next(f) for _ in range(2)]
        metadata = lines[1].strip().split()
        return metadata[0], float(metadata[1]), float(metadata[2])
    except Exception as e:
        logging.error(f"Error extracting coordinates from {file_path}: {e}")
        raise

def process_station(file_path):
    try:
        station_id, lat, lon = extract_coordinates(file_path)
        df = pd.read_csv(file_path, skiprows=2, sep=r'\s+', engine='python')
        df['station_id'] = station_id
        df['lat'] = lat
        df['lon'] = lon
        return df
    except Exception as e:
        logging.error(f"Error processing station data from {file_path}: {e}")
        raise

if __name__ == "__main__":
    data_dir = Path("../dataSample")
    all_dfs = []
    files = list(data_dir.glob("*.dat"))

    for file in tqdm(files, desc="Processing files"):
        try:
            all_dfs.append(process_station(file))
        except Exception as e:
            logging.error(f"Error processing file {file}: {e}")

    combined = pd.concat(all_dfs, ignore_index=True)
    combined.to_parquet("aggregated_data.parquet")