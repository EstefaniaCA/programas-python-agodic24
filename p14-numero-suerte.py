#Definir el numero de la suerte a partir del año de nacimiento
#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. Mostrar los dígitos individuales y el número de la suerte.

def calcular_numero_de_la_suerte(ano_nacimiento):
    digitos = [int(digito) for digito in str(ano_nacimiento)]
    numero_de_la_suerte = sum(digitos)
    
    return digitos, numero_de_la_suerte

ano_nacimiento = int(input("Ingresa tu año de nacimiento: "))

digitos, numero_de_la_suerte = calcular_numero_de_la_suerte(ano_nacimiento)

print(f"Los dígitos individuales de tu año de nacimiento son: {', '.join(map(str, digitos))}")
print(f"Tu número de la suerte es: {numero_de_la_suerte}")
