#Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:
#Dame número ? 4
#Salida:
#1
#1 2
#1 2 3
#1 2 3 4

import os

os.system("clear") 

n = int(input("Dame número: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print() 
