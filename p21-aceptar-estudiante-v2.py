# Aceptar un estudiante en base a su edad y dos calificaciones V2

# >= 18    c1>=8   y   c2>=8

import os; os.system("clear")

print("Universidad Patito SA de CV")
print("Aceptar un estudiante en base a su edad y dos calificaciones")


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18 :
    print("Ingresa 2 calificaciones separadas por enter:  ")
    c1, c2 = int(input()), int(input())
    if c1 >= 8 and c2 >= 8:
        print(f"{nombre} bienvenid@ a la Universidad Patito, tu edad {edad} y calificaciones {c1} y {c2} lo permiten")
    else:
        print("solo aceptamos alumnos con calificaciones mayores a 8")
else:
    print("Solo aceptamos a mayores de 18 años")    
print("Gracias por utilizar el programa")