#Calcular volumen en un cilindro
#Se desea calcular el volumen de un cilindro dado su radio y altura

import math

def calcular_volumen_cilindro(radio, altura):
    volumen = math.pi * (radio ** 2) * altura
    return volumen

radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

resultado = calcular_volumen_cilindro(radio, altura)

print(f"El volumen del cilindro es: {resultado:.2f} unidades cúbicas")