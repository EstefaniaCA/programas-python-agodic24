# Imprime tabla mltiplicar 1 a n, desde 1 hasta m

import os

while True:
      os.system("Clear")

      n = int(input("Hasta que tabla quieres ?"))
      m = int(input("Hasta donde deseas la tabla ?"))

      for  i in range(1, n+1):
            print("Tabla del " + str(i))
            for j in range(1, m+1):
                  print(f"{i} * {j} = {i*j}")
            print()
    
      if input("\nDeseas Continuar (S/N))").lower().startswith('n'): break