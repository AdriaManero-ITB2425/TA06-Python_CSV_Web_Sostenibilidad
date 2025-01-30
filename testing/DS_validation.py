import logging
import pandas as pd
import os
from tqdm import tqdm
from io import StringIO
import numpy as np

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s - module:%(module)s, function:%(funcName)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)


def validate_integers(df, filename):
    """Validate integer columns using vectorized operations."""
    for col in df.columns[1:]:
        if pd.api.types.is_numeric_dtype(df[col]):
            series = df[col]
            if pd.api.types.is_integer_dtype(series):
                continue
            invalid = (series != series.astype(int)) | series.isna()
            invalid_indices = invalid[invalid].index
        else:
            invalid_indices = [
                idx for idx, val in df[col].items()
                if not isinstance(val, (int, np.integer)) and
                   (isinstance(val, float) and not val.is_integer() or
                    not str(val).strip().isdigit())
            ]

        for idx in invalid_indices:
            value = df.at[idx, col]
            logging.warning(f"Invalid value '{value}' at row {idx}, column '{col}' in file '{filename}'")


def process_files(directory, target_string):
    """Process all .dat files in directory with optimized I/O."""
    files = [f for f in os.listdir(directory) if f.endswith(".dat")]
    header_line = "ID AÑO MES " + " ".join(map(str, range(1, 32))) + "\n"

    for filename in tqdm(files, desc="Processing files"):
        filepath = os.path.join(directory, filename)

        try:
            # Single file read operation
            with open(filepath, 'r+', encoding='utf-8') as f:
                lines = f.readlines()

                # Target string check
                if not any(target_string in line for line in lines):
                    logging.info(f"Target string missing in {filepath}")

                # Header processing
                lines = [line for line in lines if line != header_line]
                lines = lines[:2] + [header_line] + lines[2:]  # Insert at position 2
                while len(lines) < 3:
                    lines.append("\n")

                # Single file write operation
                f.seek(0)
                f.writelines(lines)
                f.truncate()

                # DataFrame processing from memory
                df = pd.read_csv(
                    StringIO(''.join(lines[2:])),
                    sep=r'\s+',
                    engine='python',
                    header=0,
                    dtype={0: str}  # Keep first column as string
                )
                validate_integers(df, filename)

        except FileNotFoundError:
            logging.error(f"File not found: {filepath}")
        except PermissionError as e:
            logging.error(f"Permission error: {filepath} - {e}")
        except pd.errors.ParserError as e:
            logging.error(f"CSV parsing error in {filename}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error processing {filename}: {e}")


if __name__ == "__main__":
    directory_path = "/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"
    target_str = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"
    process_files(directory_path, target_str)