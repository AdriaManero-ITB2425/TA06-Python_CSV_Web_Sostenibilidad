import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

# Cargar las coordenadas desde el archivo CSV
data = pd.read_csv("coordenadas_estaciones.csv")

# Crear un mapa con Cartopy
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={"projection": ccrs.PlateCarree()})

# Configurar el mapa
ax.set_title("Mapa de Estaciones Meteorológicas", fontsize=16)
ax.coastlines()  # Dibujar las líneas de la costa
ax.gridlines(draw_labels=True)  # Añadir líneas de cuadrícula

# Graficar las estaciones
latitudes = data["Latitud"].astype(float)
longitudes = data["Longitud"].astype(float)

ax.scatter(longitudes, latitudes, color="red", s=10, transform=ccrs.PlateCarree(), label="Estaciones")

# Añadir leyenda
ax.legend(loc="upper right")

# Guardar el mapa en un archivo
plt.savefig("mapa_estaciones.png", dpi=300)
plt.show()
