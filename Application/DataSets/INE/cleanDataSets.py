#!/usr/bin/python3

#Este mapper, limpia el .csv para sacar solo ANYO y PRECIO DE CIERRE
import sys
import re

for line in sys.stdin: #Para cada linea
    #Quita simbolos raros y guarda el resultado en un string
    line = re.sub( r'^\W+|\W+$', '', line)
    #Hace un array con las palabras de la linea.
    #Tiene en cuenta la coma para separar los elementos
    words = re.split(r"[;]", line)

    #Voy a eliminar todas las tildes
    for i in range(4):
        words[i] = words[i].replace('á', 'a')
        words[i] = words[i].replace('Á', 'A')

        words[i] = words[i].replace('é', 'e')
        words[i] = words[i].replace('É', 'E')

        words[i] = words[i].replace('í', 'i')
        words[i] = words[i].replace('Í', 'I')

        words[i] = words[i].replace('ó', 'o')
        words[i] = words[i].replace('Ó', 'O')

        words[i] = words[i].replace('ú', 'u')
        words[i] = words[i].replace('Ú', 'U')

        words[i] = words[i].replace('Ñ', 'NY')
        words[i] = words[i].replace('ñ', 'ny')

    #Ahora de la columna anyo, me quedo solo con las filas que tengan 2020
    if "2020" in words[3]:
        print(words)
