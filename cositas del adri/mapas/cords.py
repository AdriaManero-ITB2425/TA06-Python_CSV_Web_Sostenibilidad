import os
import csv

# Directorio donde están los archivos
directorio = "/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"

# Nombre del archivo de salida
archivo_salida = "coordenadas_estaciones.csv"

# Crear el archivo CSV de salida
with open(archivo_salida, mode="w", newline="", encoding="utf-8") as salida:
    escritor_csv = csv.writer(salida)
    # Escribir encabezados
    escritor_csv.writerow(["Archivo", "Latitud", "Longitud"])

    # Recorrer todos los archivos en el directorio
    for archivo in os.listdir(directorio):
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(directorio, archivo)

        # Verificar que sea un archivo (y no una carpeta)
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, mode="r", encoding="utf-8") as f:
                # Leer todas las líneas del archivo
                lineas = f.readlines()

                # Verificar que el archivo tenga al menos dos líneas
                if len(lineas) >= 2:
                    # Leer la segunda línea (índice 1) para obtener las coordenadas
                    segunda_linea = lineas[1].strip()

                    # Separar la línea por tabulaciones
                    partes = segunda_linea.split("\t")

                    # Verificar que haya al menos 3 columnas (ignorando la columna 0)
                    if len(partes) >= 3:
                        # Extraer latitud (columna 1) y longitud (columna 2)
                        latitud, longitud = partes[1], partes[2]

                        # Escribir en el archivo CSV
                        escritor_csv.writerow([archivo, latitud, longitud])

print(f"Archivo CSV '{archivo_salida}' generado con éxito.")
