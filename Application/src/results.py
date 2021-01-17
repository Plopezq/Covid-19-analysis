#!/usr/bin/python3

#Este mapper, limpia el .csv para sacar solo ANYO y PRECIO DE CIERRE
import sys
import re
import os
import pandas as pd
import matplotlib.pyplot as plt


#DataSets existentes
newDataSetPoblacion_ds = os.listdir("../finalDataSets/newDataSetPoblacion")[2]
dataSetCasos_ds = os.listdir("../finalDataSets/dataSetCasos")[3]
comunidades_extension_poblacion_ds = "../finalDataSets/comunidades_extension_poblacion.csv"


#Creo los dataframes de pandas, uno por cada archivo
#Ademas CASTEO sus columnas
newDataSetPoblacion = pd.read_csv("../finalDataSets/newDataSetPoblacion/" + newDataSetPoblacion_ds, sep=';')
newDataSetPoblacion['hombres'].astype('int')
newDataSetPoblacion['mujeres'].astype('int')
newDataSetPoblacion['total'].astype('int')
newDataSetPoblacion['00-10'].astype('int')
newDataSetPoblacion['11-20'].astype('int')
newDataSetPoblacion['21-30'].astype('int')
newDataSetPoblacion['31-40'].astype('int')
newDataSetPoblacion['41-50'].astype('int')
newDataSetPoblacion['51-60'].astype('int')
newDataSetPoblacion['61-70'].astype('int')
newDataSetPoblacion['71-80'].astype('int')
newDataSetPoblacion['81-85'].astype('int')
newDataSetPoblacion['100'].astype('int')

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

'''
aux.plot(x ='Comunidad', y='num_casos', kind = 'line')#Tipo lineal con los ejes nombrados
plt.title("Numeros de casos por comunidad")
plt.xlabel('Comunidad')
plt.ylabel('num_casos')
aux.plot(x= 'Comunidad', y = 'hab/km2', kind = 'line')
plt.title("Densidad de poblacion por comunidad")
plt.xlabel('Comunidad')
plt.ylabel('Densidad')
plt.show()
#NO SE OBSERVA RELEVACION ALGUNA
'''





#Ver UNA COMUNIDAD EN ESPECIFICO con el rango de edad mas predominante y los casos por comunidad, a ver si la edad inlfuye en algo
aux = newDataSetPoblacion
aux.plot(x ='Comunidad', y='00-10', kind = 'line')#Tipo lineal con los ejes nombrados
plt.title("Numeros de casos por comunidad")
plt.xlabel('Comunidad')
plt.ylabel('num_casos')
plt.show()
print(aux)
