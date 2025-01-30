import os
import pandas as pd
import numpy as np
from tqdm import tqdm

# Ruta de la carpeta
folder_path = '../precip.MIROC5.RCP60.2006-2100.SDSM_REJ'

# Inicializar un DataFrame para almacenar los resultados agregados
aggregated_results = pd.DataFrame()

# Obtener la lista de archivos en la carpeta
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Contador de archivos procesados
file_count = 0

# Iterar sobre todos los archivos en la carpeta con una barra de progreso
for file_name in tqdm(file_list, desc="Processing files", unit="file"):
    file_path = os.path.join(folder_path, file_name)

    try:
        # Leer el archivo CSV omitiendo las primeras dos filas
        df = pd.read_csv(file_path, skiprows=2, sep=r'\s+', engine='python')

        # Reemplazar valores inválidos (-999) con NaN
        df.replace(-999, np.nan, inplace=True)

        # Derretir el DataFrame para manejar valores diarios como una sola columna
        df_melted = df.melt(id_vars=["ID", "AÑO", "MES"], var_name="DIA", value_name="PRECIP")

        # Convertir "Precipitación" a numérico (en caso de valores no numéricos)
        df_melted["PRECIP"] = pd.to_numeric(df_melted["PRECIP"], errors="coerce")

        # Agrupar por año y calcular la suma y el promedio de la precipitación
        df_yearly = df_melted.groupby("AÑO")["PRECIP"].agg(["sum", "mean"]).rename(columns={"sum": "Total", "mean": "Average"})

        # Agregar los resultados al DataFrame agregado
        if aggregated_results.empty:
            aggregated_results = df_yearly
        else:
            aggregated_results = aggregated_results.add(df_yearly, fill_value=0)

        # Incrementar el contador de archivos procesados
        file_count += 1

    except Exception as e:
        print(f'Error processing file {file_name}: {e}')

# Calcular la media de los valores agregados
mean_results = aggregated_results / file_count

# Calcular el cambio porcentual de un año a otro
mean_results['Pct_Change'] = mean_results['Total'].pct_change()

# Encontrar el valor mínimo y máximo de cada columna y sus índices
min_values = mean_results.min()
max_values = mean_results.max()
min_indices = mean_results.idxmin()
max_indices = mean_results.idxmax()

# Imprimir los valores mínimos y máximos con sus índices
print("Minimum values:\n", min_values)
print("Indices of minimum values:\n", min_indices)
print("Maximum values:\n", max_values)
print("Indices of maximum values:\n", max_indices)

# Guardar el DataFrame de resultados medios en un archivo CSV
mean_results.to_csv('mean_output_with_stats.csv', index=True)