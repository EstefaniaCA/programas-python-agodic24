# Table de multiplicar usando funcion

import os

def tabla_multi(t, n):
    for i in range(1, n+1):
        print(f'{t} x {i} = {t * i}')

    print('\n')

#Principal
os.system('clear')
#tabla_multi(10, 5)
#tabla_multi(8, 7)
t = int(input('Que tabla quieres: '))
n = int(input('Hasta donde:  '))
tabla_multi(t, n)