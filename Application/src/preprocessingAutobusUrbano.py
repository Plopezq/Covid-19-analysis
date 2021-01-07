#!/usr/bin/pyhton3
# -*- coding: utf-8 -*-

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[*]').setAppName('preprocessingAutobusUrbano')
sc = SparkContext(conf = conf)
ss = SparkSession(sc)

data = ss.read.csv('../DataSets/INE/autobus_urbano_comunidades.csv',
	header=True, sep=';')

# CCAA, Viajeros y tasas, Periodo, Total
# CCAA, viajeros_y_tasas, Periodo, Total
data = data.withColumnRenamed('viajeros_y_tasas', 'Viajeros y tasas')

data = data.viajeros_y_tasas.contains('Variación anual').show()

data = data.drop('Viajeros y tasas')

data.show()

