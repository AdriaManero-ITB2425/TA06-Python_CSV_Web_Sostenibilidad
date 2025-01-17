import os

# Ruta del directorio donde están los archivos
directorio = ("/home/adria.manero.7e8/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"
              "")
linea_objetivo = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"
log_file_path = "errores.log"  # Archivo donde se guardarán los errores

# Lista para almacenar errores
errores = []

# Recorrer los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".dat"):  # Filtrar solo archivos relevantes
        ruta_archivo = os.path.join(directorio, archivo)
        with open(ruta_archivo, 'r') as f:
            primera_linea = f.readline().strip()  # Leer la primera línea y quitar espacios
            if primera_linea != linea_objetivo:
                errores.append(f"Archivo inválido: {archivo} (Línea: {primera_linea})")

# Crear el archivo de log si hay errores
if errores:
    with open(log_file_path, 'w') as log_file:
        log_file.write("\n".join(errores))
    print(f"Se encontraron errores. Revisa el archivo de log: {log_file_path}")
else:
    print("Todos los archivos son válidos.")

