#Calcular la hipotenusa
#Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados,

import math

def calcular_hipotenusa(lado1, lado2):
    cuadrado_lado1 = lado1 * lado1
    cuadrado_lado2 = lado2 * lado2
    suma_cuadrados = cuadrado_lado1 + cuadrado_lado2
    hipotenusa = math.sqrt(suma_cuadrados)
    return hipotenusa

lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))

resultado = calcular_hipotenusa(lado1, lado2)

print(f"La hipotenusa del triángulo es: {resultado:.2f}")