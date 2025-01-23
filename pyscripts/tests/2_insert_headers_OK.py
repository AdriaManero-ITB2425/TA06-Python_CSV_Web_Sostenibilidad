import os
import glob

# Ruta del directorio donde se encuentran los archivos .dat
directorio = "/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/PRUEBAS"

# Generar la línea con el bucle
linea_deseada = "ID AÑO MES " + " ".join(str(i) for i in range(1, 32)) + "\n"

# Encontrar todos los archivos .dat en el directorio
archivos_dat = glob.glob(os.path.join(directorio, "*.dat"))

# Aplicar el script a cada archivo .dat
for ruta_archivo in archivos_dat:
    # Leer el contenido del archivo
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()  # Leer todas las líneas como una lista

    # Eliminar todas las ocurrencias de la línea deseada, si existen
    lineas = [linea for linea in lineas if linea != linea_deseada]

    # Insertar la línea en la posición 3 (índice 2)
    lineas.insert(2, linea_deseada)

    # Sobrescribir el archivo con el contenido modificado
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(lineas)

    print(f"La línea deseada se ha asegurado en la posición 3 del archivo {ruta_archivo}.")