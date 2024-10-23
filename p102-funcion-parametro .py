# Funcion con parametros

import os

def saluda(nombre):
    print(f'Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres')

# Programa principal
os.system('clear')
saluda('Alondra Vaquera')
saluda('Fernanda Martinez')
saluda('Jose Garcia ')

saluda(20)