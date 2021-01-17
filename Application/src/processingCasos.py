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
#TODO : Eliminar basura importada que al final no usamos
#import pandas as pd

from pyspark.sql.types import *
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[*]').setAppName('P3_spark.py')
sc = SparkContext(conf = conf)

spark = SparkSession(sc)
df = spark.read.csv("../dataSetsCleans/casos_diagnostico_provincia.csv",header=True,sep=",")


#Adapto el dataSet para poderlo tratar
#provincia_iso,fecha,num_casos,num_casos_prueba_pcr,num_casos_prueba_test_ac,num_casos_prueba_ag,num_casos_prueba_elisa,num_casos_prueba_desconocida

#Casteo la comlumna de total
df = df.withColumn("num_casos",df["num_casos"].cast(IntegerType()))
df = df.withColumn("num_casos_prueba_pcr",df["num_casos_prueba_pcr"].cast(IntegerType()))
df = df.withColumn("num_casos_prueba_test_ac",df["num_casos_prueba_test_ac"].cast(IntegerType()))
df = df.withColumn("num_casos_prueba_ag",df["num_casos_prueba_ag"].cast(IntegerType()))
df = df.withColumn("num_casos_prueba_elisa",df["num_casos_prueba_elisa"].cast(IntegerType()))
df = df.withColumn("num_casos_prueba_desconocida",df["num_casos_prueba_desconocida"].cast(IntegerType()))


#Convierto el dataframe para que muestre las comunidades y no las provincias
u = Util()
f = UserDefinedFunction(lambda x: u.getCCAA(x).nombre, StringType())
dataSet = df.withColumn('provincia_iso', f(df.provincia_iso))

dataSet = dataSet.withColumnRenamed("provincia_iso", "Comunidad")



#dataSetPoblacionSinTotal.coalesce(1).write.mode("overwrite").option("header", "true").option("sep", ";").csv("dataSetPoblacion")

#dataSetPoblacionSinTotal.show()
#dataSetPoblacionSinTotal.printSchema()

#dataSetPoblacion.filter(dataSetPoblacion['Edad'] > 5).filter(dataSetPoblacion['Edad'] < 10).show()

dataSet.groupBy("Comunidad").sum().show()
