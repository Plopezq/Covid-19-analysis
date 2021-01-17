#PYTHON
#Limpieza del primer dataSet con python
python3 cleanSexoEdadProvinciaAnyo.py < ../DataSets/INE/sexo_edad_provincia_anyo.csv > ../dataSetsCleans/clean_sexo_edad_provincia_anyo.csv

#SPARK-SUBMIT --> ejecutando los dos en paralelo
  #sexo-edad-Provincia
  #num casos
spark-submit processingSexoEdadProvincia.py && spark-submit processingCasos.py

cp ../DataSets/INE/comunidades_extension.csv ../finalDataSets/comunidades_extension.csv

#PYTHON Y GRAFICAS
