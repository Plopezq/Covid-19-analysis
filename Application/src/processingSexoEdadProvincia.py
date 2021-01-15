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

#dataSetPoblacion.filter(dataSetPoblacion['Edad'] > 5).filter(dataSetPoblacion['Edad'] < 10).show()


dataSetPoblacion.show()

columnas = StructType([
	# TODO cambiar tipos, NO debería ser DOUBLE
	StructField('ccaa', StringType(), True),
	StructField('hombres', DoubleType(), True),
	StructField('mujeres', DoubleType(), True),
	StructField('total', DoubleType(), True),
	StructField('00-10', DoubleType(), True),
	StructField('11-20', DoubleType(), True),
	StructField('21-30', DoubleType(), True),
	StructField('31-40', DoubleType(), True),
	StructField('41-50', DoubleType(), True),
	StructField('51-60', DoubleType(), True),
	StructField('61-70', DoubleType(), True),
	StructField('71-80', DoubleType(), True),
	StructField('81-85', DoubleType(), True),
])

# dataSetPoblacion.show().show()

dataSetPoblacion.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("dataSetPoblacion")

newDataSetPoblacion = spark.createDataFrame([], columnas)
for ccaa in u.lista_CCAA:
	ccaa = ccaa.nombre

	data_CCAA = dataSetPoblacion.filter(dataSetPoblacion['Comunidades'] == ccaa)
	hom = data_CCAA.filter(data_CCAA['Sexo'] == 'hombres').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]
	muj = data_CCAA.filter(data_CCAA['Sexo'] == 'mujeres').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]
	amb = data_CCAA.filter(data_CCAA['Sexo'] == 'ambos sexos').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]

	data_CCAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CCAA" + str(ccaa))

	data_CCAA = data_CCAA.filter(data_CCAA['Edad'] != 'total')
	data_CCAA = data_CCAA.filter(data_CCAA['Sexo'] != 'ambos sexos')

	t0010 = data_CCAA.filter(data_CCAA['Edad'] <= 10).groupBy().sum().collect()[0][0]
	data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 10)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "0-10"+ str(ccaa))


	t1120 = data_CCAA.filter(data_CCAA['Edad'] <= 20).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 20)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "11-20"+ str(ccaa))


	t2130 = data_CCAA.filter(data_CCAA['Edad'] <= 30).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 30)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "21-30"+ str(ccaa))


	t3140 = data_CCAA.filter(data_CCAA['Edad'] <= 40).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 40)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "31-40"+ str(ccaa))


	t4150 = data_CCAA.filter(data_CCAA['Edad'] <= 50).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 50)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "41-50"+ str(ccaa))


	t5160 = data_CCAA.filter(data_CCAA['Edad'] <= 60).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 60)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "51-60"+ str(ccaa))


	t6170 = data_CCAA.filter(data_CCAA['Edad'] <= 70).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 70)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "61-70"+ str(ccaa))


	t7180 = data_CCAA.filter(data_CCAA['Edad'] <= 80).groupBy().sum().collect()[0][0]
        data_CAA = data_CCAA.filter(data_CCAA['Edad'] > 80)
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "71-80"+ str(ccaa))


	t8185 = data_CCAA.filter(data_CCAA['Edad'] <= 85).groupBy().sum().collect()[0][0]
	data_CAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "80+")

	# newDataSetPoblacion.show().show()

	newDataSetPoblacion = newDataSetPoblacion.union(spark.createDataFrame([(
		ccaa, hom, muj, amb, t0010, t1120, t2130, t3140, t4150, t5160, t6170, t7180, t8185
		)], columnas))

newDataSetPoblacion.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("newDataSetPoblacion")

























#Convierto las provincias a comunidades
#df6 = df5.filter(df5['Periodo'] > 2019).show()




#dfaux.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("../dataSetsCleans/clean_sexo_edad_ccaa_anyo.csv")


#df2020.show() #Para mostrarlo por pantalla

#Lo exporto a un csv, separados por tabuladores, si se desea exportar por comas, tan solo hay que eliminar
# la parte de 'option("sep", "\t")' o poner una , donde esta el \t
