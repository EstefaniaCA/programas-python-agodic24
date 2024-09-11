#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
#además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
#usuario lo decida.

#imprime numeros impares de 1 a n

def imprimir_impares_y_sumar(n):
    suma = 0
    print(f"Números impares desde 1 hasta {n}:")
    for i in range(1, n + 1, 2):
        print(i, end=' ')
        suma += i
    print()  # Salto de línea
    print(f"Suma de los números impares: {suma}")

def main():
    while True:
        try:
            n = int(input("Introduce el número hasta el cual deseas imprimir los números impares: "))
            if n < 1:
                print("Por favor, introduce un número entero positivo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
            continue
        
        imprimir_impares_y_sumar(n)
        
        respuesta = input("¿Deseas realizar otro cálculo? (sí/no): ").strip().lower()
        if respuesta not in ('sí', 'si', 's'):
            print("Fin del programa.")
            break

if __name__ == "__main__":
    main()
