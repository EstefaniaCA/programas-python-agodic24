#Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
#• Se crea una función que suma los dígitos individuales de un número (ya la hicimos en clase)
#• Se crea una función que recibe las lista capturada, usa la función anterior (suma dígitos) y recorre la lista
#de números y suma sus dígitos, y regresa una lista con las sumas de tos dígitos de los números de la lista.
#• Se imprime la lista original y la lista con las sumas de los dígitos de los números capturados.
#Dame los números: 1971 2345 2015 2022
#La lista de números original : [1971, 2345, 2015, 2022]
#La lista con las suma de dígitos de los números: [18, 14, 8, 6]

def leer_arreglo():
    """Lee una lista de números enteros desde la entrada del usuario."""
    return list(map(int, input("Dame los números: ").split()))

def suma_digitos(num):
    """Suma los dígitos individuales de un número."""
    return sum(int(d) for d in str(num))

def sumar_digitos_lista(lista):
    """Recorre la lista y suma los dígitos de cada número, regresando una nueva lista con las sumas."""
    return [suma_digitos(num) for num in lista]

# Programa principal
numeros = leer_arreglo()
suma_digitos_numeros = sumar_digitos_lista(numeros)

print("La lista de números original:", numeros)
print("La lista con las suma de dígitos de los números:", suma_digitos_numeros)
