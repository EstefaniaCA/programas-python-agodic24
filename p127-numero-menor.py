#Diseña un programa con una función que pida 3 números enteros y devuelva el menor de ellos, usando una función}

def leerdatos():
    datos=[]
    while True:
        d = int(input('Numero ?'))
        if d==-1: break
        datos.append(d)
    return datos

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

#Programa principal
import os;os.system('clear')
nums = leerdatos()
print(nums)
men = menor(nums)
print('El menor res ', men)
