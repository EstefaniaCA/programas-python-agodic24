#Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
#imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida.

def imprimir_pares_y_sumar(n):
    suma = 0
    print(f"Números pares desde 100 hasta {n}:")
    for i in range(100, n + 1):
        if i % 2 == 0:
            print(i, end=' ')
            suma += i
    print()  # Salto de línea
    print(f"Suma de los números pares: {suma}")

def main():
    while True:
        try:
            n = int(input("Introduce el número hasta el cual deseas imprimir los números pares: "))
            if n < 100:
                print("Por favor, introduce un número mayor o igual a 100.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
            continue
        
        imprimir_pares_y_sumar(n)
        
        respuesta = input("¿Deseas realizar otro cálculo? (sí/no): ").strip().lower()
        if respuesta not in ('sí', 'si', 's'):
            print("Fin del programa.")
            break

if __name__ == "__main__":
    main()
