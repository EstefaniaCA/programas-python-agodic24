#• Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
#• Crear una función para cada una de las siguientes estadísticas (poblacional):
   #o Mayor
   #o Menor
   #o Media
   #o Varianza
   #o Desviación estándar
#• Se muestran los resultados de cada operación.

def leer_arreglo():
    """Lee una lista de números enteros desde la entrada del usuario."""
    return list(map(int, input("Dame los números: ").split()))

def mayor(lista):
    """Devuelve el valor mayor de la lista."""
    return max(lista)

def menor(lista):
    """Devuelve el valor menor de la lista."""
    return min(lista)

def media(lista):
    """Calcula la media de los números en la lista."""
    return sum(lista) / len(lista)

def varianza(lista):
    """Calcula la varianza de los números en la lista."""
    mu = media(lista)
    return sum((x - mu) ** 2 for x in lista) / len(lista)

def desviacion_estandar(lista):
    """Calcula la desviación estándar de los números en la lista."""
    return varianza(lista) ** 0.5

# Programa principal
numeros = leer_arreglo()

print("Lista de números:", numeros)
print("La media:", media(numeros))
print("Mayor de los datos:", mayor(numeros))
print("Menor de los datos:", menor(numeros))
print("Varianza:", varianza(numeros))
print("Desviación estándar:", desviacion_estandar(numeros))
