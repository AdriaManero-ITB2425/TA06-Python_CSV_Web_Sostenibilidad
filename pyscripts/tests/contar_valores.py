import pandas as pd

# Leer el archivo
df = pd.read_csv('/home/adrian.gonzalez.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/pyscripts/tests/data2.dat', sep=' ', skiprows = 2)

# Seleccionar los datos a partir de la fila 3 y columna 3
data = df.iloc[3:, 3:]

# Contar el número de valores -999
count_neg_999 = (data == -999).sum().sum()
count_valoresbuenos = (data != -999).sum().sum()

# Contar el número total de valores
total_values999 = data.size
total_valoresbuenos = data.size

# Calcular el porcentaje
percentage_neg_999 = (count_neg_999 / total_values999) * 100
porcentaje_valoresbuenos = (count_valoresbuenos / total_valoresbuenos) * 100

print(f'El porcentaje de valores -999 es: {percentage_neg_999:.2f}%')
print(f'El porcentaje de valores buenos es: {porcentaje_valoresbuenos:.2f}%')