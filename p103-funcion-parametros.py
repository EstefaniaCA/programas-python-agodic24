# Funcion que recibe dos parametros

import os

def saluda(apaterno, nombre):
    print(f'Hola {apaterno} {nombre} longitud {len(apaterno+nombre)}')

# PRINCIPAL
os.system('Clear')
saluda ('Vaquera', 'Alondra')
#saluda('Soto')
#saluda('Soto', 'Bernal', 'Garcia')