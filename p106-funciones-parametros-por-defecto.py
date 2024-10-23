# Funciones con valores por defecto para los parametros

import os

def saluda(nombre='Alumno X', edad=15):
    print(f'Hola {nombre}, tienes {edad}años de edad')

# Principal

os.system('clear')
saluda('Alondra')
saluda()
saluda('Diana', 35)