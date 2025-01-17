import pandas as pd
import numpy as np

# Leer el archivo ignorando las dos primeras líneas y usando la tercera como encabezados
df = pd.read_csv("data2.dat", skiprows=2, header=0, sep=' ')

# Mostrar los datos
print(df)

log = []

# Verificar cada valor en el DataFrame, ignorando la primera columna (ID)
for indice_fila, fila in df.iloc[:, 1:].iterrows():  # Usamos iloc para omitir la primera columna
    for indice_columna, valor in fila.items():
        # Comprobar si el valor no es entero
        if not isinstance(valor, (int, np.integer)):
            log.append((indice_fila, indice_columna, valor))  # Guardar posición y valor

# Mostrar el log de valores no enteros
if log:
    print("Valores no enteros encontrados:")
    for entrada in log:
        print(f"Fila {entrada[0]}, Columna '{entrada[1]}': {entrada[2]}")
else:
    print("Todos los valores son enteros.")