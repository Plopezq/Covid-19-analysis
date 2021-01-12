import pandas as pd #Para los pandas
import numpy as np
import csv, operator


texto = 'casos_diagnostico_ccaa.csv'

df = pd.read_csv(texto)

df2 = df.groupby(['ccaa_iso']).sum()

print(df2)
