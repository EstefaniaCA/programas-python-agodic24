#Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
#además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo
#decida.

import os
os.system("clear")

print("Cuenta números, los suma, cuenta positivos, negativos y ceros. Parar con -1")

c = s = 0
cp = cn = cc = 0

while True:
    num = int(input("Número? "))
    if num == -1:
        break
    else:
        c += 1
        s += num
        if num > 0:
            cp += 1
        elif num < 0:
            cn += 1
        else:
            cc += 1

print("\nYa terminé el ciclo while")
print(f"Capturaste {c} números y su suma es {s}")
print(f"Números positivos: {cp}")
print(f"Números negativos: {cn}")
print(f"Números ceros: {cc}")
print("\nCiclo terminado")

