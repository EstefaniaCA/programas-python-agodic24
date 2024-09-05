# Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir
#un mensaje de acuerdo al promedio obtenido:
#• >0 y < 6 Quedas reprobado
#• >6 a <7 Pasas de panzazo
#• >7 y <8 Muy bien, pues mejorar
#• >8 y < 9 Excelente sigue así
#• >9 y <=10 Perfecto tu esfuerzo valió la pena
 
# imprime el promedio de 5 calificaciones

# Función para calcular el promedio y dar el mensaje correspondiente
def evaluar_promedio():
    calificaciones = []
    
    # Solicitar 5 calificaciones al usuario
    for i in range(5):
        calificacion = float(input(f"Introduce la calificación {i+1}: "))
        calificaciones.append(calificacion)
    
    # Calcular el promedio
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Evaluar el promedio y mostrar el mensaje correspondiente
    if 0 <= promedio < 6:
        print(f"Promedio: {promedio:.2f} - Quedas reprobado")
    elif 6 <= promedio < 7:
        print(f"Promedio: {promedio:.2f} - Pasas de panzazo")
    elif 7 <= promedio < 8:
        print(f"Promedio: {promedio:.2f} - Muy bien, puedes mejorar")
    elif 8 <= promedio < 9:
        print(f"Promedio: {promedio:.2f} - Excelente, sigue así")
    elif 9 <= promedio <= 10:
        print(f"Promedio: {promedio:.2f} - Perfecto, tu esfuerzo valió la pena")
    else:
        print(f"Promedio: {promedio:.2f} - Calificación inválida")

# Llamar a la función
evaluar_promedio()
