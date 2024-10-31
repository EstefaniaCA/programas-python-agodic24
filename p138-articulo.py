# Una clase llamada Articulo la cual modela un artículo, con id, descripción, cantidad y precio, se describe
# en el siguiente diagrama de clase

class Articulo:
    def __init__(self, id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtenerTotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"id={self.id},descripcion={self.descripcion},cantidad={self.cantidad},precio={self.precio:.2f},total={self.obtenerTotal():.2f}"


# Programa principal

import os; os.system("clear")

art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)
art1.cantidad = 999
art1.precio = 0.99
print("id = ",art1.id)
print("descripcion = ",art1.descripcion)
print("cantidad = ",art1.cantidad)
print("precio = ",art1.precio)
print("total = ",art1.obtenerTotal())
art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)
art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)
total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print('Total todos:', total)


#Añadi lo siguiente al codigo para que solo muestre la descripción de un solo articulo
# Solo por que queria separarlo

articulos = {"A101": art1, "A102": art2, "P103": art3}
id_buscar = input("Ingrese el ID del artículo para ver su descripción: ")
if id_buscar in articulos:
    print(articulos[id_buscar])
else:
    print("Artículo no encontrado.")


