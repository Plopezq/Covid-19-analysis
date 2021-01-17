#!/usr/bin/python3

#Este mapper, limpia el .csv para sacar solo ANYO y PRECIO DE CIERRE
import sys
import re
import os
import pandas as pd
import matplotlib.pyplot as plt


#DataSets creados
newDataSetPoblacion_ds = os.listdir("../finalDataSets/newDataSetPoblacion")[2]
dataSetCasos_ds = os.listdir("../finalDataSets/dataSetCasos")[3]
comunidades_extension_poblacion_ds = "../finalDataSets/comunidades_extension_poblacion.csv"


#Creo los dataframes de pandas, uno por cada archivo
#Ademas CASTEO sus columnas
newDataSetPoblacion = pd.read_csv("../finalDataSets/newDataSetPoblacion/" + newDataSetPoblacion_ds, sep=';')
#print(newDataSetPoblacion)

dataSetCasos = pd.read_csv("../finalDataSets/dataSetCasos/" + dataSetCasos_ds, sep=';')
dataSetCasos['num_casos'].astype('int')
#print(dataSetCasos)

comunidades_extension_poblacion = pd.read_csv(comunidades_extension_poblacion_ds, sep=';')
comunidades_extension_poblacion['Comunidad'].astype('str')
comunidades_extension_poblacion['km2'].astype('int')
comunidades_extension_poblacion['poblacion'].astype('int')
#print(comunidades_extension_poblacion)



#Comparamos la densidad de poblacion con el numero de casos
aux = pd.merge(dataSetCasos, comunidades_extension_poblacion, on='Comunidad')
aux['hab/km2'] = aux['poblacion'] / aux['km2']
print(aux)


aux.plot(x ='Comunidad', y='num_casos', kind = 'bar')#Tipo lineal con los ejes nombrados
plt.xlabel('Comunidad')
plt.ylabel('Eje de las x')
plt.show()
aux.plot(x= 'Comunidad', y = 'hab/km2', kind = 'bar')
plt.xlabel('Eje de las x')
plt.ylabel('Eje de las x')
plt.show()
