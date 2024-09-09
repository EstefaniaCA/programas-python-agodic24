# Imprime numeros de 1 a n, en incrementos de p,  usando wile 

import os;os.system("Clear")

print ("Imprime numeros de 1 al 100 usando wile\n")

c =  0


n = int (input("Hata donde deceas llegar ?"))

p = int (input("En incrementos de ?"))

while c <= n :
    print (c, end = " ")
    c = c + p


print ("\nCiclo terminado")