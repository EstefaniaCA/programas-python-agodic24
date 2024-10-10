#• Crear un diccionario de llave de cadena, ventas, con los siguientes elementos:
#Juan - 1550, Jose - 2600, Maria - 2220
#• Mostrar el diccionario
#• Luego agregar los siguientes elementos al diccionario:
#o Elemento Rocio - 2500 usando []
#o Elemento: Mateo - 1567 usando []
#o Elemento: Andrea - 9567 usando update()
#o Elemento: Miguel - 1234 usando update()

import os; os.system("cls")

ventas = {      "Juan"  : 1550,
                "Jose"  : 2600,
                "Maria" : 2220,}

print("Diccionario ", ventas, len(ventas))

ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

ventas.update({"Andrea":9567})
ventas.update({"Miguel":1234})

print("\nDiccionario con elementos agregados ", ventas, len(ventas))