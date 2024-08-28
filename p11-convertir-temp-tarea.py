#Convertir temperatura por 3ra vez pero en tarea
#Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit

def convertir_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

resultado = convertir_a_fahrenheit(celsius)

print(f"La temperatura en grados Fahrenheit es: {resultado:.2f}")