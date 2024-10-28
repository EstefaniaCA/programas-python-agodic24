#Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá́ mostrar un
#menú con las opciones correspondientes.
#Considere las siguientes formulas:
#• centímetros = pulgadas * 2.54
#• pies = metros * 3.281


def pulgadas_a_centimetros():
    pulgadas = float(input("Ingresa pulgadas: "))
    print(f"{pulgadas} pulgadas son {pulgadas * 2.54:.2f} centímetros.")

def metros_a_pies():
    metros = float(input("Ingresa metros: "))
    print(f"{metros} metros son {metros * 3.281:.2f} pies.")

while True:
    opcion = input("\n1. Pulgadas a centímetros\n2. Metros a pies\n3. Salir\nElige una opción: ")
    
    if opcion == "1":
        pulgadas_a_centimetros()
    elif opcion == "2":
        metros_a_pies()
    elif opcion == "3":
        print("Saliendo.")
        break
    else:
        print("Opción no válida.")
