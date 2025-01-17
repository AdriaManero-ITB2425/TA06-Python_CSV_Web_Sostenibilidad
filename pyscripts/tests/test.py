# Leer el archivo
with open('data2.dat', 'r') as file:
    lines = file.readlines()

# Eliminar las primeras dos líneas
lines = lines[2:]

# Crear la nueva línea de encabezados
new_header = ['ID', 'AÑO', 'MES'] + [str(i) for i in range(1, 32)]
new_header_line = ' '.join(new_header) + '\n'

# Insertar la nueva línea de encabezados en la primera posición
lines.insert(0, new_header_line)

# Guardar el archivo modificado
with open('data2_modified.dat', 'w') as file:
    file.writelines(lines)

print("Archivo modificado guardado como 'data2_modified.dat'.")

