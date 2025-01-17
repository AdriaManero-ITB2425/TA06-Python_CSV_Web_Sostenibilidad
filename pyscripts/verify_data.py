import os


def verificar_lineas(directorio, num_lineas):
    """
    Verifica que los archivos en un directorio tengan una cantidad exacta de líneas.

    :param directorio: Ruta del directorio que contiene los archivos a verificar.
    :param num_lineas: Número esperado de líneas por archivo.
    """
    reporte = []

    for archivo in os.listdir(directorio):
        if archivo.endswith(".dat"):  # Asumiendo que los archivos tienen extensión .dat
            ruta_archivo = os.path.join(directorio, archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                lineas = f.readlines()

            # Verificar número de líneas
            if len(lineas) != num_lineas:
                reporte.append(
                    f"Archivo '{archivo}': Número de líneas incorrecto ({len(lineas)} en lugar de {num_lineas}).")

    # Imprimir el reporte
    if not reporte:
        print("Todos los archivos cumplen con el número de líneas especificado.")
    else:
        print("\n".join(reporte))


# Parámetros
directorio = "/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/precip.MIROC5.RCP60.2006-2100.SDSM_REJ"  # Ruta al directorio con los archivos
num_lineas = 1142  # Número esperado de líneas

# Llamada a la función
verificar_lineas(directorio, num_lineas)
