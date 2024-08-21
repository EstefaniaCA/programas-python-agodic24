# p04-paga-trabajador - Calcula la paga total de un trabajador

print("Calculando la paga de un trabajador : \n")

nombre = imput("Dame tu nombre ?")
horas = int(imput("Horas ?"))
paga = float(imput("Paga x hora ?"))
tasa = 0.03

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"el trabajador {nombre}, trabajo {horas} horas a una paga de  {paga} pesos, con una tasa de {tasa}")
print(f"Paga Bruta : {pagabruta:,.2f}")
print(f"Impuesto : {impuesto:,.2f}")
print(f"Paga Neta : {paganeta:,.2f}")