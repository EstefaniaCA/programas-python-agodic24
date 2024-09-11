#Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
#introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados
#centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor
#final. El proceso debe poder repetirse hasta que el usuario lo decida.

import os
os.system("clear")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Conversión de grados Celsius a Fahrenheit en un rango de valores.")

while True:
    try:
        celsius_inicio = float(input("Introduce la temperatura inicial en grados Celsius: "))
        celsius_final = float(input("Introduce la temperatura final en grados Celsius: "))

        if celsius_inicio > celsius_final:
            print("La temperatura inicial debe ser menor o igual a la temperatura final.")
            continue

        print("\nTemperaturas en grados Celsius y sus equivalentes en grados Fahrenheit:")
        for celsius in range(int(celsius_inicio), int(celsius_final) + 1):
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")

    except ValueError:
        print("Por favor, introduce un valor numérico válido.")

    repetir = input("\n¿Deseas realizar otra conversión? (s/n): ").strip().lower()
    if repetir != 's':
        break

print("\nCiclo terminado")
