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
            for line in file:
                if target_string in line:
                    return True
        return False
    except FileNotFoundError:
        logging.error(f"The file '{filepath}' was not found.")
    except PermissionError:
        logging.error(f"Permission denied to read the file '{filepath}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return False


def insertar_linea_en_posicion(ruta_archivo):
    try:
        # Línea deseada que se debe insertar
        linea_deseada = "ID AÑO MES " + " ".join(str(i) for i in range(1, 32)) + "\n"

        # Leer el contenido del archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Eliminar todas las ocurrencias de la línea deseada
        lineas = [linea for linea in lineas if linea != linea_deseada]

        # Asegurarse de que haya al menos 3 líneas (rellenar con "\n" si es necesario)
        while len(lineas) < 3:
            lineas.append("\n")

        # Insertar la línea en la posición 3 (índice 2)
        lineas.insert(2, linea_deseada)

        # Escribir el contenido actualizado de nuevo al archivo
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.writelines(lineas)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def validate_integers_with_logging(df, filename):
    """
    Validates that all values in the DataFrame (excluding column 0) are integers.
    Logs any non-integer values using Python's logging module.

    Parameters:
        df (pd.DataFrame): The DataFrame to validate.
        filename (str): The name of the file being processed.
    """
    # Iterate over all columns starting from column 1
    for col in df.columns[1:]:
        for idx, value in enumerate(df[col]):
            try:
                # Check if the value can be converted to an integer
                int(value)
            except (ValueError, TypeError):
                # Log the invalid value
                logging.warning(f"Invalid value '{value}' at row {idx}, column '{col}' in file '{filename}'")


# Directory containing the .dat files
directory = "/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"
target_string = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"

# Process each .dat file in the directory
files = [f for f in os.listdir(directory) if f.endswith(".dat")]
for filename in tqdm(files, desc="Processing files in directory"):
    filepath = os.path.join(directory, filename)

    # Check if the string exists in the file
    if string_exists_in_file(filepath, target_string):
        pass
    else:
        logging.info(f"The string '{target_string}' was not found in the file '{filepath}'.")

    # Call the function to insert the line
    insertar_linea_en_posicion(filepath)

    # Dataframe from CSV
    try:
        df = pd.read_csv(filepath, skiprows=2, sep=r'\s+', engine='python')
    except Exception as e:
        logging.error(f"Error processing file with pandas {filename}: {e}")
        continue

    # Validate the DataFrame
    validate_integers_with_logging(df, filename)