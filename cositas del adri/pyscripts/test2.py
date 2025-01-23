import logging

# Configure the logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s - module:%(module)s, function:%(funcName)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

def insertar_linea_en_posicion(ruta_archivo):
    try:
        # Línea deseada que se debe insertar
        linea_deseada = "ID AÑO MES " + " ".join(str(i) for i in range(1, 32)) + "\n"

        # Leer el contenido del archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Eliminar todas las ocurrencias de la línea deseada
        lineas = [linea for linea in lineas if linea != linea_deseada]

        # Asegurarse de que haya al menos 3 líneas (rellenar con "\n" si es necesario)
        while len(lineas) < 3:
            lineas.append("\n")

        # Insertar la línea en la posición 3 (índice 2)
        lineas[2] = linea_deseada

        # Escribir el contenido actualizado de nuevo al archivo
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.writelines(lineas)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

ruta_archivo = '/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/pyscripts/data_sample/precip.P1.MIROC5.RCP60.2006-2100.REGRESION.dat'

# Llamar a la función
insertar_linea_en_posicion(ruta_archivo)