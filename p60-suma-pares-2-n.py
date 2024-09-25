#Se desea imprimir los pares de 2 a n y su suma
#Dame número: 20
#Salida: 2 4 6 8 10 12 14 16 18 20 , La suma es = xxx

import os

os.system("clear") 

n = int(input("Dame un número: "))

suma = 0

for i in range(2, n+1, 2):
    for j in range(i, i+1):
        print(j, end=" ")
        suma += j 

print(f", La suma es = {suma}")
