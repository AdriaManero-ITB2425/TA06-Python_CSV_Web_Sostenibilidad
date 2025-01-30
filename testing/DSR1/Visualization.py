# visualize.py
import geopandas as gpd
import matplotlib.pyplot as plt

def plot_yearly_precipitation(year):
    gdf = gpd.read_file("precipitation_data.gpkg")
    gdf_year = gdf[gdf["year"] == year]
    # Plotting logic here

if __name__ == "__main__":
    for year in range(2006, 2101):
        plot_yearly_precipitation(year)