#Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir
#0. El proceso debe poder repetirse hasta que el usuario lo decida.

import os
os.system("clear")

print("Encuentra el número mayor en una serie de números introducidos. Detén el proceso introduciendo 0.")

while True:
    mayor = None  # Inicializa la variable que almacenará el mayor número

    while True:
        try:
            num = float(input("Número? "))
            if num == 0:
                break
            if mayor is None or num > mayor:
                mayor = num
        except ValueError:
            print("Por favor, introduce un número válido.")

    if mayor is not None:
        print(f"\nEl número mayor en la serie introducida es {mayor}.")
    else:
        print("\nNo se introdujo ningún número válido.")

    repetir = input("\n¿Deseas realizar otra búsqueda? (s/n): ").strip().lower()
    if repetir != 's':
        break

print("\nCiclo terminado")
