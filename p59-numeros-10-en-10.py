#desea imprimir los números de 1 a n de 10 en 10
#Dame número: 100
#Salida. 1 11 21 31 41 51 61 71 81 91

import os

os.system("clear")  

n = int(input("Dame un número: "))

for i in range(1, n+1, 10):
    for j in range(i, i+1):
        print(j, end=" ")

print()  
