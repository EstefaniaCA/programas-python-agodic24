#Convertir temperaturas de celcius a farenheit y viceversa

import os; os.system("clear")

print("Convertir tenperaturas de celcius a farenheit y viceversa\n") 

print("[1] Convertir Farenheit a Celcius ") 
print("[ 2 ] Convertir Celius a Farenheit ") 
op=int(input("Elige?"))
if op == 1:
  print("Convirtiendo de Farenheit a Celcius")
  temp = float(input("Dame los grados Farenheit ?")) 
  res = (temp 32) * 5/9
  print (f" (temp) Farenheit equivale a {res) Celcius") 

else:

  print("Convirtiendo de Celcius a Farenheit")
  temp = float(input("Dame los grados Celcius ? ")) 
  res = temp = 9/5 + 32
  print(f" (temp) Celcius equivale a (res) Farenheit")