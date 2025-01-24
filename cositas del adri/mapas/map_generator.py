import folium
import pandas as pd

# Cargar las coordenadas desde el archivo CSV
data = pd.read_csv("coordenadas_estaciones.csv")

# Crear un mapa centrado en una ubicación aproximada
mapa = folium.Map(location=[0, 0], zoom_start=2)

# Añadir marcadores al mapa
for _, row in data.iterrows():
    folium.Marker(
        location=[float(row["Latitud"]), float(row["Longitud"])],
        popup=row["Archivo"]
    ).add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapa_estaciones.html")

print("Mapa generado: 'mapa_estaciones.html'")
