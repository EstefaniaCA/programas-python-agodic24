#• Crear un diccionario de llave numérica dias, con los siguientes elementos:
#1 - Lunes, 2 - Martes, 3 - Miércoles, 4 - Jueves, 5 - Viernes, 6 - Sabado, 7 - Domingo.
#• Muestre el diccionario.
#• Luego, accede y muestra:
#o El primer elemento usando []
#o El último elemento usando []
#o El quinto elemento usando get()
#o El séptimo elemento usando get()
#o Muestre el diccionario completo.

import os; os.system("cls")

dias = {        1:"Lunes",
                2:"Martes",
                3:"Miercoles",
                4:"Jueves",
                5:"Viernes",
                6:"Sabado",
                7:"Domingo",}

# Se uso la siguiente manera para mostrar el diccionario

print("Diccionario ", dias, len(dias))

pm = dias[1]
ul = dias[7]

print("\nPrimer elemento: ",   pm)
print("Ultimo elemento: ",   ul)
print(f"Quinto elemento:  {dias.get(5)}")
print(f"Septimo elemento: {dias.get(7)}")

print("\nDiccionario completo ", dias, len(dias))
