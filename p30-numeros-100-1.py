# Imprime numeros el 100 al 1

import os; os.system("clear")
print ("\nImprime numeros del 100 a 1 usando chile\n")

n = int(input("Hasta donde quieres llegar?"))
c = 100
while c >= 1:
 print(c, end=" ")
 c-= c- 1

print("\nCiclo terminado")
