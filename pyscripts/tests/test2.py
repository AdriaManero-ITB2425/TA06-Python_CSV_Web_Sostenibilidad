import pandas as pd
import numpy as np

# Función para verificar la primera línea del archivo
def verificar_primera_linea(ruta_archivo):
    # Línea que se espera encontrar
    linea_esperada = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"

    # Abrir el archivo y leer la primera línea
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        primera_linea = archivo.readline().strip()

    # Comparar la primera línea con la línea esperada
    return 0 if primera_linea == linea_esperada else 1


# Función para insertar una línea única en el archivo
def insertar_linea_unica(ruta_archivo):
    # Línea deseada que se debe insertar
    linea_deseada = "ID AÑO MES " + " ".join(str(i) for i in range(1, 32)) + "\n"

    # Leer el contenido del archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    # Verificar si la línea deseada ya existe en el archivo
    if linea_deseada in lineas:
        return 1  # La línea ya existe, no se realiza ningún cambio

    # Insertar la línea en la posición 3 (índice 2)
    lineas.insert(2, linea_deseada)  # Insertar la línea en el índice 2

    # Escribir el contenido actualizado de nuevo al archivo
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.writelines(lineas)

    return 0  # La línea se insertó correctamente


# Función para procesar los datos y convertir valores no enteros a NaN
def procesar_datos(ruta_archivo):
    # Lee el archivo
    df = pd.read_csv(ruta_archivo, skiprows=2, header=0, sep=' ')

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

    return df


# Ruta del archivo que deseas verificar, modificar y procesar
ruta_archivo = "/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/PRUEBAS/precip.P1.MIROC5.RCP60.2006-2100.REGRESION.dat"

# Verificar la primera línea del archivo
resultado_verificacion = verificar_primera_linea(ruta_archivo)
print(f"Resultado de verificación de la primera línea: {resultado_verificacion}")

# Insertar la línea única en el archivo
resultado_insercion = insertar_linea_unica(ruta_archivo)
print(f"Resultado de inserción de línea única: {resultado_insercion}")

# Procesar los datos en el archivo (sin imprimir el DataFrame)
df_resultado = procesar_datos(ruta_archivo)
