#La Academia de futbol Santos Laguna, desea llevar el control de los jugadores en cada
#categoría, las categorías se conforman de acuerdo con la edad y pueden tener varios
#jugadores. Diseña una aplicación en Python, usando los conceptos aprendidos sobre
#programación orientada a objetos.

class Jugador:
    def __init__(self, nombre, anio_nac, sexo, becado):
        self.nombre = nombre
        self.anio_nac = anio_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        return f"Nombre: {self.nombre} AñoNac: {self.anio_nac} Sexo: {self.sexo} Becado: {'Becado' if self.becado else 'Sin Beca'}"


class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def subtotal(self):
        total = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                total += self.costo
        return total

    def total_jugadores(self, sexo):
        return sum(1 for jugador in self.jugadores if jugador.sexo == sexo)

    def __str__(self):
        return f"Nombre: {self.nombre} Rango: {self.rango} Costo: ${self.costo:,.2f}"


class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_hombres(self):
        return sum(categoria.total_jugadores("Hombre") for categoria in self.categorias)

    def total_mujeres(self):
        return sum(categoria.total_jugadores("Mujer") for categoria in self.categorias)

    def total_ingresos(self):
        return sum(categoria.subtotal() for categoria in self.categorias)

    def __str__(self):
        return (f"Nombre: {self.nombre}\nPropietario: {self.propietario}\n"
                f"Domicilio: {self.domicilio}\nTotal de Categorias: {len(self.categorias)}\n"
                f"Total de Hombres: {self.total_hombres()}\nTotal de Mujeres: {self.total_mujeres()}\n")


def main():
    # Crear la academia y agregar categorías y jugadores
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

    # Agregar categorías
    cat_junior_a = Categoria("Junior A", "2006/2007/2008", 1250.00)
    cat_junior_b = Categoria("Junior B", "2009/2010/2011", 850.00)
    cat_pony_a = Categoria("Pony A", "2012/2013/2014", 700.00)

    # Agregar jugadores a Junior A
    cat_junior_a.agregar_jugador(Jugador("Alexander Lopez", 2006, "Hombre", False))
    cat_junior_a.agregar_jugador(Jugador("Uriel Puga", 2007, "Hombre", True))
    cat_junior_a.agregar_jugador(Jugador("Alejandra Escalona", 2008, "Mujer", False))

    # Agregar jugadores a Junior B
    cat_junior_b.agregar_jugador(Jugador("Armando Santana", 2009, "Hombre", False))
    cat_junior_b.agregar_jugador(Jugador("Daniel Mijares", 2010, "Hombre", False))
    cat_junior_b.agregar_jugador(Jugador("Antonio Hernandez", 2011, "Mujer", True))

    # Agregar jugadores a Pony A
    cat_pony_a.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", True))
    cat_pony_a.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
    cat_pony_a.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", False))

    # Agregar categorías a la academia
    academia.agregar_categoria(cat_junior_a)
    academia.agregar_categoria(cat_junior_b)
    academia.agregar_categoria(cat_pony_a)

    # reporte
    print("REPORTE DEL CLUB DEPORTIVO")
    print(academia)
    print(">> Datos generales de las Categorías")
    for categoria in academia.categorias:
        print(categoria)

    print(">> Jugadores por Categoría:")
    for categoria in academia.categorias:
        print(f"> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})")
        for jugador in categoria.jugadores:
            print(jugador)
        print(f"- SubTotal : ${categoria.subtotal():,.2f}\n")

    print(f"-> Total : ${academia.total_ingresos():,.2f}")


if __name__ == "__main__":
    main()
