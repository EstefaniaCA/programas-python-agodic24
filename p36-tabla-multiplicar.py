# imprime la tabla de multiplicar 

while(True):

    t = int(input("De cuál número quieres imprimir su tabla de multiplicar?: "))
    n = int(input("Hasta cuál número quieres imprimir?:  "))
    c = 1

    while( c <= n):
        print(f'{t} x {c} = {t*c}')
        c+=1

    r=input("Deseas Continuar [S]/[N]? ")
    if r.upper()=="N":
        print("Saliendo...")
        break
