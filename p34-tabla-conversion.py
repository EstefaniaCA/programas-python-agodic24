#Imprimir una tabla de conversion

import os

os.system("")


# Tabla de conversion de Peso a Dollar

import os

while(True):
 os.system('clear')

 tc = 20.71
 pi = float(input("Valor inicial: "))
 pf = float(input("Valor final : "))
 c = pi

 print("\nPesos\tDollar")
 print("-"*15)

 while c<=pf :
  print(f'{c}\t{c/tc:.2f}')
  c+=1
 print("-"*15)

 res=input('Deseas Continuar(S/N)? ')

 if res.upper()=='N':
  break