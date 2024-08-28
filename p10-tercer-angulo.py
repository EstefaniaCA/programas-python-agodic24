#Calcular el tercer angulo dentro de un triangulo, conociendo 2 de ellos
#Dados dos ángulos de un triángulo, calcular el 3er ángulo,

def calcular_tercer_angulo(angulo1, angulo2):
    angulo3 = 180 - (angulo1 + angulo2)
    return angulo3

angulo1 = float(input("Ingresa el valor del primer ángulo (en grados): "))
angulo2 = float(input("Ingresa el valor del segundo ángulo (en grados): "))

resultado = calcular_tercer_angulo(angulo1, angulo2)

print(f"El tercer ángulo del triángulo es: {resultado:.2f} grados")