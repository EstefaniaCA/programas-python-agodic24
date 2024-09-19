# Imprime numeros del 1 a n o de n a 1 segun lo decida el usario

import os;

while True:
    os.system("Clear")

    print("[1] imprimir del 1 a n")
    print("[2] imprimir del 1 a n")
    print("[3] Salir....")
    op = int(input("Elige ?"))

    if op==1:
        print("Imprimiendo numeros del 1 a n")
        n = int(input("Hasta Donde ? "))
        for x in range (1, n+1):
            print(x, end=" ")
        
    elif op==2:
        print("Imprimiendo numeros del n a 1")
        n = int(input("Hasta Donde ? "))
        for x in range (n, 0, -1):
            print(x, end=" ")
        
    elif op==3:
        break
    else:
        print("\nOpcion Invalida")

        input("\n < Presiona cualquier tecla para continuar > ")


print("\nProceso terminado.. ")