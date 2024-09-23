#Calcula l factorial de un numero

import os; os.system("clear")

#n = int(input("Dame un numero?"))

n=5


f=1

print(f"{n}! =", end=())

for i in range (1, n+1):
    f = f*i
    print(f"{i}{"x" if i!=n else ""}", end ="")

print (f"={f}")