#Teniendo horas, calcular la conversion a dias, minutos y segundos
#Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos,

def convertir_horas(horas):
    dias = horas // 24
    horas_restantes = horas % 24
    minutos = horas * 60
    segundos = minutos * 60
    
    return dias, horas_restantes, minutos, segundos

horas = float(input("Ingresa la cantidad de horas: "))

dias, horas_restantes, minutos, segundos = convertir_horas(horas)

print(f"{horas} horas equivalen a:")
print(f"{dias} días y {horas_restantes:.2f} horas")
print(f"{minutos:.2f} minutos")
print(f"{segundos:.2f} segundos")