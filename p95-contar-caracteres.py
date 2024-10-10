#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada
#carácter en la cadena.
#Como estrategia:
#- Crear un diccionario donde la llave es el carácter y el valor el número de veces que aparece
#- Hacer un ciclo que pase por cada carácter de la cadena
#o buscamos el carácter en el diccionario, si no existe lo agregamos y sumamos 1,
#o si ya existe solo sumamos 1
#- Al final quedará algo así, estarán en él solo los caracteres que aparezcan al menos una vez en el orden en
#que aparezcan la primera vez.
#{ ‘a’: 1 , ‘b’:3, ........}
#Ejemplo: Hola Mundo
#{ ‘H’: 1, ‘o’:2, ‘l’:1, ‘a’:1, ‘ ‘:1, ‘M’:1, ‘u’:1, ‘n’:1, ‘d’:1}

import os; os.system("cls")

cadena = input("Escribe una cadena: ")

contador = {}

for caracter in cadena:
    if caracter in contador:
            contador[caracter] += 1
    else:
            contador[caracter] = 1
            
print(contador)
