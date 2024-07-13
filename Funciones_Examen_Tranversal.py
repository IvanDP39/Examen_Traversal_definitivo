import random 
Trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez", "Ana Martinez","Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

def menu():
    print("1. Asignar sueldos aleatorios" )
    print("2. Clasificar Sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def Asignacion_de_Sueldos(): 
    Sueldo_Final = []
    while len(Sueldo_asignado) < 10:
        Sueldo_asignado = random.randint(300000, 2500000)
        Sueldo_asignado.append(Sueldo_Final)
        print(Sueldo_Final)
    return Sueldo_Final


def Clasificar_sueldos():
    print("Sueldos menores a $800.000")
    
    print("Nombre Empleado    Sueldo")