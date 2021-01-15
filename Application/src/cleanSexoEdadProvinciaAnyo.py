#!/usr/bin/python3

#Este mapper, limpia el .csv para sacar solo ANYO y PRECIO DE CIERRE
import sys
import re

print("Sexo;Edad;Provincias;Periodo;Total")
for line in sys.stdin: #Para cada linea

    line = re.sub( r'^\W+|\W+$', '', line)

    #Hace un array con las palabras de la linea.
    #Tiene en cuenta la coma para separar los elementos
    words = re.split(r"[;]", line)


    #Para eliminar los numeros
    for i in range(10):
        words[2] = words[2].replace(str(i),'')

    anyos = words[1].split(' ')
    words[1] = anyos[0]

    #Para eliminar el espacio inicial
    if words[2][0] == " " :
        words[2] = words[2][1:]

    #Ahora de la columna anyo, me quedo solo con las filas que tengan 2020
    if "2020" in words[3]:
        #Voy a eliminar todas las tildes
        for i in range(5):
            words[i] = words[i].lower()

            words[i] = words[i].replace('á', 'a')

            words[i] = words[i].replace('é', 'e')

            words[i] = words[i].replace('è', 'e')

            words[i] = words[i].replace('í', 'i')

            words[i] = words[i].replace('ó', 'o')

            words[i] = words[i].replace('ú', 'u')

            words[i] = words[i].replace('ñ', 'ny')

        for j in range(4):
            print (words[j] + ";", end = "")
        print(words[4])
