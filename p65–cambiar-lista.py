#   Acceder a los elementos de la lista de numeros 

import os;os.system('Clear')

nums= [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('Acceder a los elementos de una lista')
print('La lista     : ', nums )
print('# elementos  : ', len(nums))
print('Acceder con indices positivos 0 .. 8 ')
print('Primero       : ', nums [0])
print('Ultimo        : ', nums [8])
print('Del 2 al 6    :', nums [2:6])
print('Primero 3     :', nums [:3])
print('Ultimos 3     :', nums [6:])

print('\nAcceder con indices positivos -9 .. -1')
print('Primero       : ', nums [-9])
print('Ultimo        : ', nums [-1])
print('Del 2 al 6    :', nums [-7:-2])
print('Primero 3     :', nums [:-6])
print('Ultimos 3     :', nums [-3:])