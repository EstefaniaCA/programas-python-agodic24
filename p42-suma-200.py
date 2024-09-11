import os
os.system("clear")

print("Calcula la suma de números introducidos hasta que la suma sea >= 200. Parar con 0")

while True:
    suma = 0
    conteo = 0

    while suma < 200:
        num = float(input("Número? "))
        if num == 0:
            break
        suma += num
        conteo += 1

    if suma >= 200:
        print("\nSuma alcanzada o superada")
        print(f"Se introdujeron {conteo} números con una suma total de {suma}.")
    else:
        print("\nProceso interrumpido antes de alcanzar la suma deseada.")

    repetir = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
    if repetir != 's':
        break

print("\nCiclo terminado")
