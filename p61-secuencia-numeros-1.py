#Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:
#Dame número ? 4
#Salida:
#1
#2 2
#3 3 3
#4 4 4 

import os

os.system("clear") 

n = int(input("Dame número: "))

for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()  
