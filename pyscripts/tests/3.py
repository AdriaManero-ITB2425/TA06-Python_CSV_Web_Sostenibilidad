import pandas as pd
import numpy as np

# Lee el archivo
df = pd.read_csv('data.dat', skiprows=2, header=0, sep=' ')

# Función que convierte los valores no enteros a NaN
def to_int_or_nan(x):
    try:
        return int(x)  # Intenta convertir el valor a entero
    except ValueError:
        return np.nan  # Si no puede, devuelve NaN

# Aplica la función a todas las columnas (excepto la primera)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda col: col.apply(to_int_or_nan))

# Sustituye los NaN por -999
df.iloc[:, 1:] = df.iloc[:, 1:].fillna(-999)

# Forzar la inferencia del tipo de objeto
df.iloc[:, 1:] = df.iloc[:, 1:].infer_objects()

