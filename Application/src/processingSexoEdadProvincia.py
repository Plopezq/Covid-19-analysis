#!/usr/bin/pyhton3
# -*- coding: utf-8 -*-
from util import *
from pyspark import SparkConf, SparkContext
import string
import re
from pyspark.sql.functions import *
from pyspark.sql import functions as F
from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import StringType

#import pandas as pd
from pyspark.sql.types import *
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[*]').setAppName('P3_spark.py')
sc = SparkContext(conf = conf)

spark = SparkSession(sc)
df = spark.read.csv("../dataSetsCleans/clean_sexo_edad_provincia_anyo.csv",header=True,sep=";")

#Adapto el dataSet para poderlo tratar
#Elimino los puntos
df = df.withColumn('Total', translate('Total', '.', ''))
#Casteo la comlumna de total
df = df.withColumn("Total",df["Total"].cast(DoubleType()))
#Casteo el periodo para quedarme solo con el año y NO el dia y el mes
df = df.withColumn('Periodo', split(df['Periodo'], ' ').getItem(4))
df = df.withColumn("Periodo",df["Periodo"].cast(DoubleType()))
df = df.filter(df['Periodo'] > 2019) #DataSet con todas las provincias y el anyo 2020

#Convierto el dataframe para que muestre las comunidades y no las provincias
u = Util()
f = UserDefinedFunction(lambda x: u.getCCAA(x).nombre, StringType())
dataSetPoblacion = df.withColumn('Provincias', f(df.Provincias))
dataSetPoblacion = dataSetPoblacion.withColumnRenamed("Provincias", "Comunidades")

dataSetPoblacion = dataSetPoblacion.drop('Periodo')

#Quito las filas donde la edad sea TOTAL para hacer un casteo correcto
dataSetPoblacionSinTotal = dataSetPoblacion.filter(dataSetPoblacion['Edad'] != 'total')
dataSetPoblacionSinTotal.withColumn("Edad",dataSetPoblacion["Edad"].cast(DoubleType()))

#dataSetPoblacionSinTotal.show()
#dataSetPoblacionSinTotal.printSchema()


# dataSetPoblacion.filter(dataSetPoblacion['Edad'] > 5).filter(dataSetPoblacion['Edad'] < 10).show()


dataSetPoblacion.show()

columnas = StructType([
	StructField('ccaa', StringType(), True),
	StructField('hombres', DoubleType(), True),
	StructField('mujeres', DoubleType(), True)
])
newDataSetPoblacion = spark.createDataFrame([], columnas)
for ccaa in u.lista_CCAA:
	ccaa = ccaa.nombre

	data_CCAA = dataSetPoblacion.filter(dataSetPoblacion['Comunidades'] == ccaa)
	hom = data_CCAA.filter(data_CCAA['Sexo'] == 'hombres').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]
	muj = data_CCAA.filter(data_CCAA['Sexo'] == 'mujeres').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum()
	amb = data_CCAA.filter(data_CCAA['Sexo'] == 'ambos sexos').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum()

	newDataSetPoblacion = newDataSetPoblacion.union(spark.createDataFrame([(
		ccaa, hom, hom
		)], columnas))

newDataSetPoblacion.show()
























#Convierto las provincias a comunidades
#df6 = df5.filter(df5['Periodo'] > 2019).show()




#dfaux.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("../dataSetsCleans/clean_sexo_edad_ccaa_anyo.csv")


#df2020.show() #Para mostrarlo por pantalla

#Lo exporto a un csv, separados por tabuladores, si se desea exportar por comas, tan solo hay que eliminar
# la parte de 'option("sep", "\t")' o poner una , donde esta el \t
