import pandas as pd
import numpy as np


df = pd.read_csv('/home/adr1k/PycharmProjects/TA06-Python_CSV_Web_Sostenibilidad/cositas del adri/pyscripts/data_sample/precip.P9.MIROC5.RCP60.2006-2100.REGRESION.dat', skiprows=2, sep=r'\s+', engine='python')

# Replace invalid values (-999) with NaN
df.replace(-999, np.nan, inplace=True)

# Melt the DataFrame to handle daily values as a single column
df_melted = df.melt(id_vars=["ID", "AÑO", "MES"], var_name="Día", value_name="Precipitación")

# Convert "Precipitación" to numeric (in case of non-numeric values)
df_melted["Precipitación"] = pd.to_numeric(df_melted["Precipitación"], errors="coerce")

# Group by year and calculate total and average precipitation
results = df_melted.groupby("AÑO")["Precipitación"].agg(["sum", "mean"]).rename(columns={"sum": "Total", "mean": "Average"})

# Print results
print(results)

print(df_melted)




