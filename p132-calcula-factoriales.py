#Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
#• Se crea una función que calcula el factorial de un número (ya la hicimos en clase)
# Se crea una función que recibe las lista capturada, usa la función anterior (calcular factorial) que recorre la
#lista de números y calcula el factorial de cada uno de ellos, y regresa como resultado una lista con los
#factoriales de los números de la lista.
#• Se imprime la lista original y la lista con los factoriales de los números capturados.
#Dame los números: 2 5 8 9
#La lista de números originales: [2, 5, 8, 9]
#La lista con los factoriales: [2, 120, 40320, 362880]

def leer_arreglo():
    """Lee una lista de números enteros desde la entrada del usuario."""
    return list(map(int, input("Dame los números: ").split()))

def calcular_factorial(num):
    """Calcula el factorial de un número."""
    if num == 0 or num == 1:
        return 1
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial

def factoriales_lista(lista):
    """Calcula el factorial de cada número en la lista y devuelve una nueva lista de factoriales."""
    return [calcular_factorial(num) for num in lista]

# Programa principal
numeros = leer_arreglo()
factoriales_numeros = factoriales_lista(numeros)

print("La lista de números originales:", numeros)
print("La lista con los factoriales:", factoriales_numeros)
