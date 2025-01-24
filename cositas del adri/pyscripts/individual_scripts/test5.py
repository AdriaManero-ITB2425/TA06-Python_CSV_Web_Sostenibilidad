import pandas as pd
import glob
from tqdm import tqdm

# List of CSV files
csv_files = glob.glob("/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ/*.dat")

# Initialize a counter for total values
total_values_count = 0

# Iterate through all CSV files and count values with a progress bar
for file in tqdm(csv_files, desc="Processing CSV Files", unit="file"):
    df = pd.read_csv(file, skiprows=2, sep=r'\s+', engine='python')
    total_values_count += df.size  # Count all values in the DataFrame

# Print the total count of values
print(f"Total number of values in all DataFrames: {total_values_count}")