#!/usr/bin/python3

#Este mapper, limpia el .csv para sacar solo ANYO y PRECIO DE CIERRE
import sys
import re
from util import *
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

#Creo los dataframes de pandas, uno por cada archivo
#PRIMER DATASET
# newDataSetPoblacion_ds = os.listdir("../finalDataSets/newDataSetPoblacion/*.csv")

dataSetsPath = '../finalDataSets/'

dataSetPoblacionPath = glob.glob(dataSetsPath + 'newDataSetPoblacion/' + '*.{}'.format('csv'))[0]

CCAA_RANGO_EDAD = pd.read_csv(dataSetPoblacionPath, sep=';')

CCAA_RANGO_EDAD['hombres'].astype('int')
CCAA_RANGO_EDAD['mujeres'].astype('int')
CCAA_RANGO_EDAD['total'].astype('int')
CCAA_RANGO_EDAD['00-10'].astype('int')
CCAA_RANGO_EDAD['11-20'].astype('int')
CCAA_RANGO_EDAD['21-30'].astype('int')
CCAA_RANGO_EDAD['31-40'].astype('int')
CCAA_RANGO_EDAD['41-50'].astype('int')
CCAA_RANGO_EDAD['51-60'].astype('int')
CCAA_RANGO_EDAD['61-70'].astype('int')
CCAA_RANGO_EDAD['71-80'].astype('int')
CCAA_RANGO_EDAD['81-85'].astype('int')
CCAA_RANGO_EDAD['100'].astype('int')
#print(CCAA_RANGO_EDAD)


#SEGUNDO DATASET
dataSetCasosPath = glob.glob(dataSetsPath + 'dataSetCasos/' + '*.{}'.format('csv'))[0]
#print(dataSetCasosPath)
CASOS_COMUNIDAD = pd.read_csv(dataSetCasosPath, sep=';')
CASOS_COMUNIDAD['num_casos'].astype('int')
#print(CASOS_COMUNIDAD)


#TERCER DATASET
comunidades_extension_poblacion_ds = "../finalDataSets/comunidades_extension_poblacion.csv"
extensionPath = glob.glob(dataSetsPath + '*.{}'.format('csv'))[0]
COMUNIDAD_EXTENSION_POBLACION = pd.read_csv(extensionPath, sep=';')
COMUNIDAD_EXTENSION_POBLACION['Comunidad'].astype('str')
COMUNIDAD_EXTENSION_POBLACION['km2'].astype('int')
COMUNIDAD_EXTENSION_POBLACION['poblacion'].astype('int')
#print(COMUNIDAD_EXTENSION_POBLACION)



#Comparamos la densidad de poblacion con el numero de casos
aux = pd.merge(CASOS_COMUNIDAD, COMUNIDAD_EXTENSION_POBLACION, on='Comunidad')
aux['hab/km2'] = aux['poblacion'] / aux['km2']
aux['casos/poblacion'] = aux['num_casos'] / aux['poblacion']
#print(aux)

if sys.argv[1] == '0':
    #NUMERO DE CASOS POR COMUNIDAD EN COMPARACION CON HAB/KM2
    aux.plot(x ='Comunidad', y='num_casos', kind = 'bar')#Tipo lineal con los ejes nombrados
    plt.title("Numeros de casos por comunidad")
    plt.xlabel('Comunidad')
    plt.ylabel('num_casos')
    aux.plot(x= 'Comunidad', y = 'hab/km2', kind = 'bar')
    plt.title("Densidad de poblacion por comunidad")
    plt.xlabel('Comunidad')
    plt.ylabel('Densidad')
    plt.show()
    #NO SE OBSERVA RELEVACION ALGUNA


if sys.argv[1] == '1':
    #DENSIDAD DE POBLACION versus CASOS POR HABITANTES
    x = aux['hab/km2']
    y = aux['casos/poblacion']
    plt.xlabel('hab/km2')
    plt.ylabel('casos/poblacion')
    (m, b) = np.polyfit(x, y, 1)
    yp = np.polyval([m, b], x)
    plt.plot(x, yp)
    plt.grid(True)
    plt.scatter(x,y)
    plt.show()


if sys.argv[1] == '2':
    #CASOS POR RANGO DE EDAD
    aux = CCAA_RANGO_EDAD.drop(20,axis=0) #Quito el total nacional
    aux['+85'] = aux['100']
    eje_y = ["00-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-85", "+85"]
    aux.plot(x= 'ccaa', y = eje_y, kind = 'bar')
    plt.show()


if sys.argv[1] == '3':
    #CASOS POR COMUNIDAD --> Hombres vs mujeres
    CCAA_RANGO_EDAD.rename(columns={'ccaa': 'comunidad'}, inplace=True)
    CASOS_COMUNIDAD.rename(columns={'Comunidad': 'comunidad'}, inplace=True)
    #print(CASOS_COMUNIDAD)
    #print(CCAA_RANGO_EDAD)
    aux = pd.merge(CASOS_COMUNIDAD, CCAA_RANGO_EDAD, on='comunidad')
    print(aux)
    eje_y = ["hombres", "mujeres"]
    aux.plot(x= 'comunidad', y = eje_y, kind = 'bar')
    plt.show()















#asfd
