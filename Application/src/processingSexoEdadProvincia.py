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

from pyspark.sql.types import *
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[16]').setAppName('P3_spark.py')
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
	StructField('100', DoubleType(), True),
])

#dataSetPoblacionSinTotal.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("dataSetPoblacion")

newDataSetPoblacion = spark.createDataFrame([], columnas)

for ccaa in u.lista_CCAA:
	ccaa = ccaa.nombre

	data_CCAA = dataSetPoblacion.filter(dataSetPoblacion['Comunidades'] == ccaa)

	#data_CCAA.show()

	# data_CCAA = data_CCAA.filter((data_CCAA['Edad'] == 'total')) | (data_CCAA['Edad'] <= 85))

	#data_CCAA.show()

	# data_CCAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CCAA" + str(ccaa))

	hom = data_CCAA.filter(data_CCAA['Sexo'] == 'hombres').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]
	muj = data_CCAA.filter(data_CCAA['Sexo'] == 'mujeres').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]
	amb = data_CCAA.filter(data_CCAA['Sexo'] == 'ambos sexos').filter(data_CCAA['Edad'] == 'total').groupBy('Sexo').sum().collect()[0][1]

	data_CCAA = data_CCAA.filter(data_CCAA['Edad'] != 'total')
	data_CCAA = data_CCAA.filter(data_CCAA['Sexo'] == 'ambos sexos')

	#data_CCAA.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CCAA" + str(ccaa))

	t0010 = data_CCAA.filter(data_CCAA['Edad'] >= 0).filter(data_CCAA['Edad'] <= 10).groupBy("Edad", "Sexo").sum()
	#t0010.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "0-10"+ str(ccaa))
	t0010 = t0010.groupBy().sum().collect()[0][0]


	t1120 = data_CCAA.filter(data_CCAA['Edad'] >= 11).filter(data_CCAA['Edad'] <= 20).groupBy("Edad", "Sexo").sum()
	#t1120.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "11-20"+ str(ccaa))
	t1120 = t1120.groupBy().sum().collect()[0][0]


	t2130 = data_CCAA.filter(data_CCAA['Edad'] >= 21).filter(data_CCAA['Edad'] <= 30).groupBy("Edad", "Sexo").sum()
	#t2130.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "21-30"+ str(ccaa))
	t2130 = t2130.groupBy().sum().collect()[0][0]


	t3140 = data_CCAA.filter(data_CCAA['Edad'] >= 31).filter(data_CCAA['Edad'] <= 40).groupBy("Edad", "Sexo").sum()
	#t3140.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "31-40"+ str(ccaa))
	t3140 = t3140.groupBy().sum().collect()[0][0]


	t4150 = data_CCAA.filter(data_CCAA['Edad'] >= 41).filter(data_CCAA['Edad'] <= 50).groupBy("Edad", "Sexo").sum()
	#t4150.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "41-50"+ str(ccaa))
	t4150 = t4150.groupBy().sum().collect()[0][0]


	t5160 = data_CCAA.filter(data_CCAA['Edad'] >= 51).filter(data_CCAA['Edad'] <= 60).groupBy("Edad", "Sexo").sum()
	#t5160.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "51-60"+ str(ccaa))
	t5160 = t5160.groupBy().sum().collect()[0][0]


	t6170 = data_CCAA.filter(data_CCAA['Edad'] >= 61).filter(data_CCAA['Edad'] <= 70).groupBy("Edad", "Sexo").sum()
	#t6170.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "61-70"+ str(ccaa))
	t6170 = t6170.groupBy().sum().collect()[0][0]

	t7180 = data_CCAA.filter(data_CCAA['Edad'] >= 71).filter(data_CCAA['Edad'] <= 80).groupBy("Edad", "Sexo").sum()
	#t7180.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "71-80"+ str(ccaa))
	t7180 = t7180.groupBy().sum().collect()[0][0]


	t8185 = data_CCAA.filter(data_CCAA['Edad'] >= 81).filter(data_CCAA['Edad'] <= 85).groupBy("Edad", "Sexo").sum()
	#t8185.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "80+"+ str(ccaa))
	t8185 = t8185.groupBy().sum().collect()[0][0]


	t100 = data_CCAA.filter(data_CCAA['Edad'] > 85).groupBy("Edad", "Sexo").sum()
	#t100.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("data_CAA" + "100")
	t100 = t100.groupBy().sum().collect()[0][0]


	newDataSetPoblacion = newDataSetPoblacion.union(spark.createDataFrame([(
		ccaa, hom, muj, amb, t0010, t1120, t2130, t3140, t4150, t5160, t6170, t7180, t8185, t100
		)], columnas))

#newDataSetPoblacion.show()
newDataSetPoblacion.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("../finalDataSets/newDataSetPoblacion")
