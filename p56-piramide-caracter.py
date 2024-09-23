#Imprime el cuadrado de un caracter determinado
import os

os.system("clear")

r = int(input("Renglones"))
#c = int(input("Columnas"))
car = int(input("Caracter2"))
for i in range (1, r+1):
    for j in range (1, i+1):
     print ("*", end="")
    print ()   