# Muestra el tipo de angulo en base a su magnitud 
# <90 es agudo, =90 es recto, >90 y <180 es obtuso, =180 es llano, >180 y <360 es concavo, =360 es cerrado

import os; os.system("clear")

print("Muestra el tipo de ángulo en base a su magnitud")

angulo = int(input("Dame el ángulo ?"))

if angulo>=0 and angulo <=360:
    if angulo < 90 :
        print("Agudo")
    elif angulo == 90 :
        print("Recto")
    elif angulo > 90 and angulo < 180 :
        print("Obtuso")
    elif angulo == 180 :
        print("Llano")
    elif angulo > 180 and angulo < 360 :
        print("Concavo")
    else:
        print("Cerrado o completo")
else :
    print("\nEl angulo esta fuera de rango")