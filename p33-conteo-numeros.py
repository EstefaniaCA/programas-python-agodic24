# Cuenta números, los suma, cuenta positivos, negativos y ceros, parar con -1

import os; os.system("clear")

print("Cuenta números, los suma, cuenta positivos, negativos y ceros, parar con -1")

c=s=0
cp=cn=cc=0


while True:
    num= int (input("Numero?"))
    if num== -1:
        break
    else:
        c= c+1
        s= s+ num
        if num> 0: 
            cp= cp+1
        elif num< 0:
            cn+1
        else: cc= cc+1    

else:
    print("\nYa termine el ciclo while")

print(f"Capturaste{c} numeros y su suma es {s}")       
print(f"Capturaste{c} numeros")   
print("\nCiclo terminado")
