# funcion con parametros, que regresa valor 

import os


def suma(n1, n2):
    s = n1 + n2
    return s


# Principal
os.system('clear')

# Caso 1: el resultado se guarda en un variable
r = suma(100, 200)
print('El resultado es', r)

# Caso 2: el resultado se calcula y se imprime directamente
print('\nOtra suam', suma(500, 200))


# Caso 3: el usuario proporciona el valor de los parametros
print('Dame dos numero para sumar, separados por <ENTER>')
a, b = int(input()), int(input())
print('\nLa suma del usuario es ', suma(a, b))