#Evaluacion del primer parcial de la materia de "Computacion aplicada, MITA"
# Estefania Castañeda Alonso
# Imprime el control de la inscripción a un evento académico de la Universidad Patito.

import os

ventas_dia = []

while True:
    os.system("clear")
    print("Universidad Patito SA de CV")
    print("Sistema de Inscripción Congreso de Sistemas")
    
    tipo_usuario = int(input("Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500 ? "))
    tipo_paquete = int(input("Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900 ? "))
    cantidad = int(input("Cantidad ? "))

    if tipo_usuario == 1:
        precio_usuario = 100
    elif tipo_usuario == 2:
        precio_usuario = 200
    else:
        precio_usuario = 500

    if tipo_paquete == 1:
        precio_paquete = 600
    elif tipo_paquete == 2:
        precio_paquete = 800
    else:
        precio_paquete = 900

    subtotal = (precio_usuario + precio_paquete) * cantidad

    descuento = 0
    if subtotal > 5000:
        if tipo_usuario == 1:
            descuento = 0.20  # 20% para alumnos
        elif tipo_usuario == 2:
            descuento = 0.10  # 10% para trabajadores
        elif tipo_usuario == 3:
            descuento = 0.05  # 5% para docentes

    monto_descuento = subtotal * descuento
    total_con_descuento = subtotal - monto_descuento
    porcentaje_descuento = descuento * 100

    ventas_dia.append(total_con_descuento)

    tipos_usuarios = {1: "Alumno", 2: "Trabajador", 3: "Docente"}
    tipos_paquetes = {1: "Solo conferencias", 2: "Con eventos sociales", 3: "Con kit de acceso"}

    print(f"\nTu pedido fue: {cantidad}, Tipo de usuario: {tipos_usuarios[tipo_usuario]}, "
          f"Tipo de paquete: {tipos_paquetes[tipo_paquete]}")
    print(f"Subtotal: {subtotal} con un descuento de: {monto_descuento:.1f} ({porcentaje_descuento:.1f}%) "
          f"y un total de {total_con_descuento:.1f}")

    continuar = input("Deseas continuar (S/N) ? ").lower()
    if continuar != 's':
        break

total_ventas = sum(ventas_dia)

print(f"\nImporte Total de la Venta: {total_ventas:.2f}")
print("Proceso terminado ...")
