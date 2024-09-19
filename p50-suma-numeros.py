# Sumar n numeros elegidos por el usuario 

import os; os.system("Clear")

suma = 0
n = int(input("Cuantas calificaciones ? "))


for  i in range (1, n+1):
    print (f"calificacion {i} ? ", end=" ")
    x = float(input())
    suma = suma + x


print(f"\nLa suma es {suma}")
print(f"\nEl promedio es {suma / n }")

