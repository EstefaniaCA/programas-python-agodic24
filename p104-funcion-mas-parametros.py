# Numero de parametros desconocidos

import os

def saludatodos(*todos):
    print(todos)
    print('Hola', todos[0])
    print(f'Separados por - {'-'.join(todos)}')
    for n in todos:
        print('Hola :', n.upper())
    

# PRINCIPAL
os.system('Clear')
saludatodos('Juan', 'Pedro', 'Luis', 'Rocio', 'Maria')
saludatodos('Luis', 'Jose')
saludatodos('Carlos')