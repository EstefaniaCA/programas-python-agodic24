# Imprime la tabla de multiplicar usando el ciclo for

import os

while True:
    os.system("Clear")

    t = int(input("Dame la tabla que deceas imprimir ? "))
    n = int(input("Hasta donde deseas la tabla  ? "))

    for i in range(1, n+1, 1):
        print(f"{t} x {i} = {t*i}")


    if input("\nContinuar (S/N))").lower().startswith('n'): break

print("\nProceso terminado...")