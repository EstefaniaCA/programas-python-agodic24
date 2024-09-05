#Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo,
# 2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, mostrar un mensaje de error.
# Ej: 1 , Lunes, Ej 8 , dia inválido

# Imprimir dia de la semana a partir de un numero del 1 al 7

def numero_a_dia(numero):
    # Diccionario de días de la semana
    dias_semana = {
        1: 'Domingo', 2: 'Lunes', 3: 'Martes', 4: 'Miércoles',
        5: 'Jueves', 6: 'Viernes', 7: 'Sábado'
    }
    
    if 1 <= numero <= 7:
        return dias_semana[numero]
    else:
        return "Día inválido"

# Solicitar el número al usuario
num = int(input("Introduce un número entre 1 y 7: "))

# Mostrar el resultado
resultado = numero_a_dia(num)
print(resultado)
