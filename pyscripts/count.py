import os
import glob
import pandas as pd
from tqdm import tqdm

# Ruta del directorio donde se encuentran los archivos .dat
directorio = "/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/test_4testing"

# Encontrar todos los archivos .dat en el directorio
archivos_dat = glob.glob(os.path.join(directorio, "*.dat"))

# Inicializar contadores totales
total_minus_999_count = 0
total_values_count = 0

# Procesar cada archivo .dat con una barra de progreso
for ruta_archivo in tqdm(archivos_dat, desc="Procesando archivos"):
    # Leer el archivo
    df = pd.read_csv(ruta_archivo, sep=' ', skiprows=2)

    # Seleccionar solo las columnas "1" a "31"
    df = df.loc[:, '1':'31']

    # Contar los valores -999
    minus_999_count = (df == -999).sum().sum()

    # Contar el número total de valores
    total_values = df.size

    # Acumular los contadores
    total_minus_999_count += minus_999_count
    total_values_count += total_values

print(f"Total de valores -999: {total_minus_999_count}")
print(f"Total de valores: {total_values_count}")