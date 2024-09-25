#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:
#¿Cuántos términos?? 5
#Salida: 1 + 1/2! + 1/3! + 1/4! + 1/5! , suma: 2.283333333333333

import os
import math

os.system("clear") 

n = int(input("¿Cuántos términos?? "))

suma = 0

terminos = []

for i in range(1, n + 1):
    termino = 1 / math.factorial(i)
    terminos.append(f"1/{i}!")
    suma += termino

print("Salida:", " + ".join(terminos), ", suma:", suma)
