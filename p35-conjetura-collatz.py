#Imprime y calcula los  numeros de la conjetura de Collatz

import os

while(True):
  
  os.system("clear")
  num = int (input("Dame un entero positivo?"))

  while num!=1 :
   print (num, end= "")
   if num% 2 == 0:
    num = num // 2
  else:
    num= num *3 +1 
  print (num, end= "") 


  if input ("\n n Deseas continuar (S/N)").upper().startswith("N"): break

print("\n Proceso terminadon")

