import os; os.system("clear")

empleados = []

def capturar_datos():
    while True:
        nombre = input("Nombre del empleado (* para terminar): ")
        if nombre == "*":
            break
        edad = int(input("Edad: "))
        sexo = input("Sexo (h/m): ")
        pasatiempos = input("Pasatiempos (separados por comas): ").split(",")
        sueldo = float(input("Sueldo: "))
        
        empleado = {
            "nombre": nombre,
            "edad": edad,
            "sexo": sexo,
            "pasatiempos": pasatiempos,
            "sueldo": sueldo
        }
        
        empleados.append(empleado)

def imprimir_tabla():
    print("\nTabla de datos:")
    print("{:<10} {:<5} {:<5} {:<10} {:<30}".format("Nombre", "Edad", "Sexo", "Sueldo", "Pasatiempos"))
    for emp in empleados:
        print("{:<10} {:<5} {:<5} {:<10.2f} {:<30}".format(emp["nombre"], emp["edad"], emp["sexo"], emp["sueldo"], ", ".join(emp["pasatiempos"])))

def resumen():
    total_empleados = len(empleados)
    hombres = sum(1 for emp in empleados if emp["sexo"] == "h")
    mujeres = sum(1 for emp in empleados if emp["sexo"] == "m")

    pasatiempos_contador = {}
    for emp in empleados:
        for pasatiempo in emp["pasatiempos"]:
            if pasatiempo.strip() in pasatiempos_contador:
                pasatiempos_contador[pasatiempo.strip()] += 1
            else:
                pasatiempos_contador[pasatiempo.strip()] = 1
    
    suma_edad = sum(emp["edad"] for emp in empleados)
    promedio_edad = suma_edad / total_empleados
    suma_sueldo = sum(emp["sueldo"] for emp in empleados)
    promedio_sueldo = suma_sueldo / total_empleados
    
    mayor = max(empleados, key=lambda emp: emp["edad"])
    menor = min(empleados, key=lambda emp: emp["edad"])
    
    print("\nResumen:")
    print(f"Empleados: {total_empleados}")
    print(f"Hombres: {hombres}")
    print(f"Mujeres: {mujeres}")
    print("Pasatiempos: ", ", ".join([f"{key}/{value}" for key, value in pasatiempos_contador.items()]))
    print(f"Edad -> suma: {suma_edad}, promedio: {promedio_edad:.1f}")
    print(f"Sueldo -> suma: {suma_sueldo:.2f}, promedio: {promedio_sueldo:.2f}")
    print(f"{mayor['nombre']} de {mayor['edad']} es el mayor, {menor['nombre']} de {menor['edad']} es el menor.")

print("Mueblería Muebles FANYs")
print("Sistema de Procesamiento de Empleados")

capturar_datos()
imprimir_tabla()
resumen()


