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

for i in range(len(u.dict)):
    replace_val = dict[i]
    new_value = u.getCCAA(replace_val).nombre
    update_func = (F.when(F.col('Provincias') == replace_val, new_value)
                    .otherwise(F.col('Provincias')))
    df7 = df6.withColumn('Provincias', update_func)


df7.show()



class Util:

	an = CCAA('andalucia', 'Andalucía')
	ar = CCAA('aragon', 'Aragón')
	ast = CCAA('asturias', 'Asturias') # 'as' is reserved
	cn = CCAA('canarias', 'Canarias')
	cb = CCAA('cantabria', 'Cantabria')
	cl = CCAA('castilla y leon', 'Castilla y León')
	cm = CCAA('castilla-la mancha', 'Castilla-La Mancha')
	ct = CCAA('catalunya', 'Cataluña')
	ex = CCAA('extremadura', 'Extremadura')
	ga = CCAA('galicia', 'Galicia')
	ib = CCAA('islas baleares', 'Islas Baleares')
	ri = CCAA('la rioja', 'La Rioja')
	md = CCAA('comunidad de madrid', 'Comunidad de Madrid')
	mc = CCAA('murcia', 'Región de Murcia')
	nc = CCAA('navarra', 'Navarra')
	pv = CCAA('pais vasco', 'País Vasco')
	vc = CCAA('comunidad valenciana', 'Comunidad Valenciana')

	ce = CCAA('ceuta', 'Ceuta')
	ml = CCAA('melilla', 'Melilla')

	dict = {
		'alava' : pv, 'araba/alava' : pv,
		'albacete' : cm,
		'alicante' : vc,
		'almeria' : an,
		'asturias' : ast,
		'avila' : cl,
		'badajoz' : ex,
		'barcelona' : ct,
		'burgos' : cl,
		'caceres' : ex,
		'cadiz' : an,
		'cantabria' : cb,
		'castellon' : vc,
		'ciudad real' : cm,
		'cordoba' : an,
		'corunya, a' : ga,
		'cuenca' : cm,
		'gerona' : ct,
		'granada' : an,
		'guadalajara' : cm,
		'guipúzcoa' : pv,
		'huelva' : an,
		'huesca' : ar,
		'baleares' : ib,
		'jaen' : an,
		'leon' : cl,
		'lerida' : ct,
		'lugo' : ga,
		'madrid' : md,
		'málaga' : an,
		'murcia' : mc,
		'navarra' : nc,
		'orense' : ga,
		'palencia' : cl,
		'las palmas' : cn,
		'pontevedra' : ga,
		'la rioja' : ri,
		'salamanca' : cl,
		'segovia' : cl,
		'sevilla' : an,
		'soria' : cl,
		'tarragona' : ct,
		'santa cruz de tenerife' : cn,
		'teruel' : ar,
		'toledo' : cm,
		'valencia' : vc,
		'valladolid' : cl,
		'vizcaya' : pv,
		'zamora' : cl,
		'zaragoza' : ar
		# TODO ceuta and melilla
	}
#Convierto las provincias a comunidades
#df6 = df5.filter(df5['Periodo'] > 2019).show()

#df7.coalesce(1).write.option("header", "true").option("sep", ";").csv("sample_file.csv")

#df2020.show() #Para mostrarlo por pantalla

#Lo exporto a un csv, separados por tabuladores, si se desea exportar por comas, tan solo hay que eliminar
# la parte de 'option("sep", "\t")' o poner una , donde esta el \t
