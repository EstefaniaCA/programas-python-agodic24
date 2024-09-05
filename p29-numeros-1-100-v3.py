#imprime numeros del 1 al n, en incremenetos de p usando while

import os; os.system("clear")

print ("\nImprime numeros del 1 a 100usando chile\n")

c=1

n = int(input("Hasta donde quieres llegar?"))
p = int(input("En incrementos de ?"))

while c<=n: 
 print(c, end=" ")
 c= c+ p

print("\nCiclo terminado")