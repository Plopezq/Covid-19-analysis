#!/usr/bin/pyhton3
# -*- coding: utf-8 -*-
from util import *
from pyspark import SparkConf, SparkContext
import string
import re
from pyspark.sql.functions import *
from pyspark.sql import functions as F

#import pandas as pd
from pyspark.sql.types import *
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[*]').setAppName('P3_spark.py')
sc = SparkContext(conf = conf)

spark = SparkSession(sc)
df = spark.read.csv("../dataSetsCleans/clean_sexo_edad_provincia_anyo.csv",header=True,sep=";")

#Adapto el dataSet para poderlo tratar
#Elimino los puntos
df2 = df.withColumn('Total', translate('Total', '.', ''))
#Casteo la comlumna de total
df3 = df2.withColumn("Total",df2["Total"].cast(DoubleType()))
#Casteo el periodo para quedarme solo con el año y NO el dia y el mes
df4 = df3.withColumn('Periodo', split(df['Periodo'], ' ').getItem(4))
df5 = df4.withColumn("Periodo",df4["Periodo"].cast(DoubleType()))

df6 = df5.filter(df5['Periodo'] > 2019) #DataSet con todas las provincias y el anyo 2020

#Convierto el dataframe para que muestre las comunidades y no las provincias

u = Util()

for prov, comunidad in dict.items(u.dict):
    update_func = F.when(F.col('Provincias') == prov, comunidad.nombre).otherwise(F.col("col2"))
    df6 = df6.withColumn('Provincias', update_func)

df6.show()

#Convierto las provincias a comunidades
#df6 = df5.filter(df5['Periodo'] > 2019).show()

#df7.coalesce(1).write.option("header", "true").option("sep", ";").csv("sample_file.csv")

#df2020.show() #Para mostrarlo por pantalla

#Lo exporto a un csv, separados por tabuladores, si se desea exportar por comas, tan solo hay que eliminar
# la parte de 'option("sep", "\t")' o poner una , donde esta el \t
