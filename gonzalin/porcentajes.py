import os
import pandas as pd

# Ruta de la carpeta
folder_path = r'C:\Users\adria\PycharmProjects\TA06-Python_CSV_Web_Sostenibilidad\precip.MIROC5.RCP60.2006-2100.SDSM_REJ'

# Inicializar contadores
total_values = 0
good_values = 0
bad_values = 0

# Iterar sobre todos los archivos en la carpeta
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Verificar si es un archivo
    if os.path.isfile(file_path):
        try:
            # Leer el archivo CSV omitiendo las primeras dos filas
            df = pd.read_csv(file_path, skiprows=2, header=None, sep=' ')

            # Seleccionar desde la fila 3 y la columna 4
            df = df.iloc[3:, 4:]
            total_values += df.size
            good_values += (df != -999).sum().sum()
            bad_values += (df == -999).sum().sum()
        except Exception as e:
            print(f'Error processing file {file_name}: {e}')

print(f'Total de valores: {total_values}')
print(f'Valores buenos: {good_values}')
print(f'Valores malos: {bad_values}')