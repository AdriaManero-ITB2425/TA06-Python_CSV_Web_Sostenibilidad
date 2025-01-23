import pandas as pd
import numpy as np
import glob
import os

# Ruta del directorio donde están los archivos
directorio = "/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/PRUEBAS/"
log_file_path = "valores_no_enteros.log"  # Archivo donde se guardarán los valores no enteros

# Variable para rastrear si se encontraron errores
se_encontraron_errores = False

# Abrir el archivo de log solo si es necesario
with open(log_file_path, 'w') as log_file:
    for ruta_archivo in glob.glob(os.path.join(directorio, "*.dat")):
        nombre_archivo = os.path.basename(ruta_archivo)

        # Leer el archivo ignorando las dos primeras líneas y usando la tercera como encabezados
        df = pd.read_csv(ruta_archivo, skiprows=2, header=0, sep=' ')

        # Verificar cada valor en el DataFrame, ignorando la primera columna (ID)
        for indice_fila, fila in df.iloc[:, 1:].iterrows():  # Omitir la primera columna
            for indice_columna, valor in fila.items():
                # Comprobar si el valor no es entero
                if not isinstance(valor, (int, np.integer)):
                    # Escribir el error en el log
                    log_file.write(f"Archivo: {nombre_archivo}, Fila {indice_fila + 1}, Columna '{str(indice_columna)}': {valor}\n")
                    se_encontraron_errores = True

# Si no se encontraron errores, eliminar el archivo de log
if not se_encontraron_errores:
    os.remove(log_file_path)
    print("Todos los valores en los archivos son enteros.")
else:
    print(f"Se encontraron valores no enteros. Revisa el archivo de log: {log_file_path}")
