import os
import pandas as pd
from tqdm import tqdm

# Ruta de la carpeta
folder_path = '/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ'

# Inicializar contadores
total_values = 0
null_values = 0

# Obtener la lista de archivos en la carpeta
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Iterar sobre todos los archivos en la carpeta con una barra de progreso
for file_name in tqdm(file_list, desc="Processing files", unit="file"):
    file_path = os.path.join(folder_path, file_name)

    try:
        # Leer el archivo CSV omitiendo las primeras dos filas
        df = pd.read_csv(file_path, skiprows=2, sep=r'\s+', engine='python')

        # Seleccionar desde la columna 4
        df = df.iloc[:, 3:]
        total_values += df.size
        null_values += (df == -999).sum().sum()
    except Exception as e:
        print(f'Error processing file {file_name}: {e}')

print(f'Total de valores: {total_values}')
print(f'Valores nulos (-999): {null_values}')