#Dados tres números enteros, verificar cual es el mayor, ej: 10, 9 8, el mayor es 10, 11, 30, -1 el mayor es 30
#Elegir el numero mayor

def encontrar_mayor(a, b, c):
    # Encontrar el mayor de los tres números
    mayor = max(a, b, c)
    print(f"El mayor es: {mayor}")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

encontrar_mayor(num1, num2, num3)