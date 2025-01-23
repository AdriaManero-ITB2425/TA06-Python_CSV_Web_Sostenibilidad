def verificar_primera_linea(ruta_archivo):
    # Línea que se espera encontrar
    linea_esperada = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"

    # Abrir el archivo y leer la primera línea
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        primera_linea = archivo.readline().strip()

    # Comparar la primera línea con la línea esperada
    return 0 if primera_linea == linea_esperada else 1


# Ruta del archivo que deseas verificar
ruta_archivo = "ruta_del_archivo.txt"

# Llamar a la función y capturar el resultado
resultado = verificar_primera_linea(ruta_archivo)

# Imprimir el resultado (opcional)
print(f"Resultado: {resultado}")

