#Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos
#regrese la suma de números pares o impares en el rango de números especificados.
#El programa deberá mostrar un menú con las opciones correspondientes y llamara a la función según la opción
#seleccionada.


def suma_pares_impares(inicio, fin, tipo):
    return sum(num for num in range(inicio, fin + 1) if (num % 2 == 0 if tipo == "P" else num % 2 != 0))

def mostrar_menu():
    print("\n--- Suma de Números ---")
    print("1. Sumar números pares")
    print("2. Sumar números impares")
    print("3. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1, 2, o 3): ")
        
        if opcion in ["1", "2"]:
            inicio = int(input("Inicio: "))
            fin = int(input("Fin: "))
            tipo = "P" if opcion == "1" else "I"
            resultado = suma_pares_impares(inicio, fin, tipo)
            print(f"La suma de números {'pares' if tipo == 'P' else 'impares'} entre {inicio} y {fin} es: {resultado}")
        
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida.")

ejecutar_programa()
