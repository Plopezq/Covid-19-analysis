#!/usr/bin/pyhton
# -*- coding: utf-8 -*-

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local[*]').setAppName('preprocessingAutobusUrbano')
sc = SparkContext(conf = conf)
ss = SparkSession(sc)

data = ss.read.csv('../DataSets/INE/autobus_urbano_comunidades.csv',
	header=True, sep=';')

# CCAA, viajeros_y_tasas, Periodo, Total

data.show()

data = data.filter(data['viajeros_y_tasas'].encode('utf-8') == 'Variación anual')

data.show()

data = data.drop('Viajeros y tasas')

data.show()

