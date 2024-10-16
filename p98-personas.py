#• Dados los siguientes nombres:
#• Juan, Maria, Pedro, Jose, Rocio
#• Pedro, Juan, Pablo, Mateo, Esther
#• Crea dos conjuntos uno para cada lista de nombres y muéstralos ( A, B )
#• Calcula y muestra:
#◦ union de los conjuntos ( A | B)
#◦ intesección de los conjuntos ( A & B)
#◦ diferenia de los conjuntos ( A – B )
#◦ diferencia simetrica de los conjuntos ( A ^ B )
#• Calcula y muestra también
#◦ si el conjunto de nombres Pablo, Mateo, es subconjunto de B
#◦ si el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica
#◦ si Pedro esta en A
#◦ si Lilia no esta en B

# Operaciones entre conjuntos, de nombres

import os; os.system("clear")

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print("Conjuntos A, B")
print(A,B)

print("\nUnion:")
print("A union B ", A | B)

print("\nInterseccion:")
print("A interseccion B ", A & B)

print("\nDiferencia:")
print("A diferencia B ", A - B)

print("\nDiferencia simetrica:")
print("A dif simetrica B ", A ^ B)

print("\nProbar por subconjuntos:")
C = {"Pablo", "Mateo"}
print("Pablo y Mateo es subconjunto de B ", C.issubset(B))

print("\nProbar superconjuntos:")
D = {"Reynalod", "Angelica"}
print("A es superconjunto de Reynaldo y Angelica ", A.issuperset(D))

print("\nVerificar pertenencia o no pertenencia al conjunto:")
print("Pedro esta en el A ", "Pedro" in A)
print("Lilia no esta en el B ", "Lilia" not in B)