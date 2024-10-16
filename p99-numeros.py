#• Dados los siguientes números:
#◦ 50,60,70,80,90,100,200
#◦ 60,90,100,300,400,500
#◦ 10,20,60,90,70,100,600,700
#• Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)
#• Calcula y muestra:
#◦ unión de los conjuntos A y B ( A | B )
#◦ unión de los conjuntos B y C ( B | C )
#◦ diferencia de A y C ( A – C)
#◦ diferencia simétrica de B y C ( B ^ C)
#◦ intersección de B y C ( B & C )
#• Calcula y responda a las siguientes preguntas>
#◦ A es subconjunto de B ?
#◦ C es subconjunto de A ?
#◦ 100 esta en A ?
#◦ 60 esta en A , y en B y en C ?
#◦ 900 no esta en C ?

# Operaciones entre conjuntos, de numeros

import os; os.system("cls")

A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}

print("Conjuntos A, B y C")
print(A,B,C)

print("\nUnion:")
print("A union B ", A | B)
print("B union C ", B | C)

print("\nDiferencia:")
print("A diferencia C ", A - C)

print("\nDiferencia simetrica:")
print("B dif simetrica C ", B ^ C)

print("\nInterseccion:")
print("B interseccion C ", B & C)

print("\nProbar por subconjuntos:")
print("A es subconjunto de B ", A.issubset(B))
print("C es subconjunto de A ", C.issubset(A))

print("\nVerificar pertenencia o no pertenencia al conjunto:")
print("¿100 esta en el A? ", 100 in A)
print("¿60 esta en el A? ¿y en B? ¿y en C? ", 60 in (A and B and C))
print("¿900 no  esta en el B? ", 900 not in C)