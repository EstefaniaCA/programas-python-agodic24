# Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,
# VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error.
# Ej. 11, número inválido, Ej: 4 , IV

# Convierte  numeros decimales a romanos en un rango de 1 al 10

def numero_a_romano(numero):
    
    romanos = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'
    }
    
    if 1 <= numero <= 10:
        return romanos[numero]
    else:
        return "Número inválido"


num = int(input("Introduce un número entre 1 y 10: "))


resultado = numero_a_romano(num)
print(resultado)
