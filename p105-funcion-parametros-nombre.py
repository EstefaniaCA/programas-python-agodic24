# Funciones con nombres en los parametros

import os

def saluda(apaterno, amaterno, nombre):
    print(f'Hola {apaterno} {amaterno}, {nombre}')

# Principal
os.system('clear')
saluda('Vaquera', 'Dominguez', 'Alondra')
saluda(nombre='Alondra', amaterno='Dominguez', apaterno='Vaquera')
saluda(amaterno='Alonso ', nombre='Estefania', apaterno='Castaneda')