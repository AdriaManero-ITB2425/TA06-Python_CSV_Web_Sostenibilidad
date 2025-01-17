import pandas as pd
from uaclient.defaults import PRINT_WRAP_WIDTH

# Leer el archivo (asumimos que ya tienes el archivo con la nueva cabecera)
df = pd.read_csv('data2_modified.dat', sep=' ')

# Reemplazar los valores -999 por NaN
df.replace(-999, pd.NA, inplace=True)

# Contar los valores nulos (NaN) en el DataFrame
null_count = df.isna().sum().sum()
total_values = df.count().sum()

print(f"Total de valores no nulos: {total_values}")
# Contar los valores -999 (ahora representados como NaN)
# Como ya hemos reemplazado -999 con NaN, el recuento de NaN ya incluye esos valores

print(f"Total de valores nulos o '-999': {null_count}")


columnas_dias = [str(i) for i in range(1, 32)]

# Agrupar por el año y sumar los valores diarios
suma_anual = df.groupby('AÑO')[columnas_dias].sum(numeric_only=True).sum(axis=1)

# Mostrar el resultado
print(suma_anual)


print(df[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']])

print(df)