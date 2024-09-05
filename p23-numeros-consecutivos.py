#Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son (1,4,6) mandar mensaje de error.
# Verificar numeros consecutivos

def son_consecutivos(a, b, c):
    # Ordenar los números para verificar si son consecutivos
    numeros = sorted([a, b, c])
    
    # Verificar si los números son consecutivos
    if numeros[1] == numeros[0] + 1 and numeros[2] == numeros[1] + 1:
        print("Los números son consecutivos.")
    else:
        print("Error: Los números no son consecutivos.")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

son_consecutivos(num1, num2, num3)
