# Eleva un numero base a su exponente

import os; os.system("Clear")

base = int (input("Base            ?"))
exponente = int (input("Exponente  ?"))

p = 1
for i in range (exponente):
    p = p * base
print(f"\nLa base {base} elevado a la {exponente} es {p}")







p = 1
for _ in range (exponente):
    p = p * base
print(f"\nLa base {base} elevado a la {exponente} es {p}")



