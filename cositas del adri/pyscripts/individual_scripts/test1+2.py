import logging

# Configure the logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s - module:%(module)s, function:%(funcName)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

#Functions
def string_exists_in_file(filepath, target_string):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if target_string in line:
                    return True
        return False
    except FileNotFoundError:
        logging.error(f"The file '{filepath}' was not found.")
    except PermissionError:
        logging.error(f"Permission denied to read the file '{filepath}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return False

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

# File paths and target string
filepath = "/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/pyscripts/data_sample/precip.P3.MIROC5.RCP60.2006-2100.REGRESION.dat"
target_string = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"

# Check if the string exists in the file
if string_exists_in_file(filepath, target_string):
    print(0)
else:
    logging.info(f"The string '{target_string}' was not found in the file '{filepath}'.")
    print(1)

# Call the function to insert the line
insertar_linea_en_posicion(filepath)