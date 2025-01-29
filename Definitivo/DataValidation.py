import logging
import pandas as pd
import os
from tqdm import tqdm

# Configure the logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s - module:%(module)s, function:%(funcName)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

def string_exists_in_file(filepath, target_string):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return any(target_string in line for line in file)
    except FileNotFoundError:
        logging.error(f"The file '{filepath}' was not found.")
    except PermissionError:
        logging.error(f"Permission denied to read the file '{filepath}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return False

def insertar_linea_en_posicion(ruta_archivo):
    try:
        linea_deseada = "ID AÑO MES " + " ".join(str(i) for i in range(1, 32)) + "\n"
        with open(ruta_archivo, 'r+', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            lineas = [linea for linea in lineas if linea != linea_deseada]
            while len(lineas) < 3:
                lineas.append("\n")
            lineas.insert(2, linea_deseada)
            archivo.seek(0)
            archivo.writelines(lineas)
            archivo.truncate()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def validate_integers_with_logging(df, filename):
    for col in df.columns[1:]:
        for idx, value in enumerate(df[col]):
            try:
                int(value)
            except (ValueError, TypeError):
                logging.warning(f"Invalid value '{value}' at row {idx}, column '{col}' in file '{filename}'")

directory = "/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"
target_string = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"

files = [f for f in os.listdir(directory) if f.endswith(".dat")]
for filename in tqdm(files, desc="Processing files in directory"):
    filepath = os.path.join(directory, filename)

    if not string_exists_in_file(filepath, target_string):
        logging.info(f"The string '{target_string}' was not found in the file '{filepath}'.")

    insertar_linea_en_posicion(filepath)

    try:
        df = pd.read_csv(filepath, skiprows=2, sep=r'\s+', engine='python')
    except Exception as e:
        logging.error(f"Error processing file with pandas {filename}: {e}")
        continue

    validate_integers_with_logging(df, filename)