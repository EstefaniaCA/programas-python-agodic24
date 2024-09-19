# Imprime numeros paresde n a 2 y numeros impares de 1 a n , sumar en ambos casos 

import os;

while True:
    os.system("Clear")

    print("[1] imprimir del 1 a n")
    print("[2] imprimir del 1 a n")
    print("[3] Salir....")
    op = int(input("Elige ?"))

    if op==1:
        s = 0
        print("Imprimiendo numeros pares de n a 2")
        n = int(input("Desde Donde ? "))
        n = n if n%2==0 else n-1
        for x in range (1, n, -2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de pares es " + str(s))
        
    elif op==2:
        s=0
        print("Imprimiendo numeros impares del 1 a n")
        n = int(input("Hasta Donde ? "))
        n = n if n%2!=0 else n-1
        for x in range (n, n+1, 2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de impares es " + str(s))
    elif op==3:
        break
    else:
        print("\nOpcion Invalida")

        input("\n < Presiona cualquier tecla para continuar > ")


print("\nProceso terminado.. ")