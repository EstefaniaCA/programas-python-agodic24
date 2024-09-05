#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La
#Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.
#Ej: Maria, 22, M, 10 9 10, Maria has sido aceptada, tu edad de 22 y tus calificaciones 10, 9 y 10, lo permiten
#Ej: Jose, H, 21, 7, 6, 5, solo aceptamos mujeres
#Ej: Dolores, M ,20, 10, 10, 10, Eres mujer, pero no tienes la edad, solo mayores a 21
#Ej: Sandra, M, 25, 7, 6, 5, Eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios de 8 a 9.5

# Elegir si un estudiante es aceptado

def evaluar_estudiante():
    # Solicitar los datos del estudiante
    nombre = input("Introduce el nombre del estudiante: ")
    sexo = input("Introduce el sexo (h/m): ").lower()
    edad = int(input("Introduce la edad del estudiante: "))
    
    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"Introduce la calificación {i+1}: "))
        calificaciones.append(calificacion)
    
   
    promedio = sum(calificaciones) / len(calificaciones)
    
   
    if sexo != 'm':
        print(f"{nombre}, solo aceptamos mujeres")
    elif edad <= 21:
        print(f"{nombre}, eres mujer, pero no tienes la edad, solo aceptamos mayores de 21")
    elif not (8 <= promedio <= 9.5):
        print(f"{nombre}, eres mujer, tienes la edad, pero tu promedio no alcanza, solo aceptamos promedios de 8 a 9.5")
    else:
        print(f"{nombre}, has sido aceptada, tu edad de {edad} y tus calificaciones {calificaciones[0]}, {calificaciones[1]} y {calificaciones[2]} lo permiten")


evaluar_estudiante()
