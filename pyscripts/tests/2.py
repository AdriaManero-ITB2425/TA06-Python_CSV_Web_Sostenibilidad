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

# Ruta del archivo que deseas modificar
ruta_archivo = "ruta_del_archivo.txt"

# Llamar a la función y capturar el resultado
resultado = insertar_linea_unica(ruta_archivo)