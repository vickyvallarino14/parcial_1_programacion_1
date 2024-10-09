#numero historia clinica, nombre paciente, edad paciente, diagnostico, cantidad de dias de internacion
pacientes=[]

def menu():
    """Función para mostrar el menú al usuario"""
    print("""Menu Principal:
    1.Cargar Pacientes
    2.Mostrar todos los pacientes
    3.Buscar pacientes por número de Historia Clinica
    4.Ordenar pacientes por número de historia clínica
    5.Mostrar paciente con más días de internación
    6.Mostrar paciente con menos días de internación
    7.Cantidad de pacientes con más de 5 días de internación
    8.Promedio de días de internación de todos los pacientes
    9.Salir    
    """) 

def cargar_pacientes(pacientes):
    """Función para cargar pacientes"""
    contador_ingresos=0
    cantidad_ingresos = int(input("Ingrese la cantidad de pacientes que desea cargar en la base de datos: "))
    while contador_ingresos < cantidad_ingresos:
        historia_clinica = int(input(f"Ingrese el numero de historia clinica del paciente {contador_ingresos+1}: "))
        nombre = input("Ingrese el nombre del paciente: ").capitalize()
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("Ingrese el diagnostico: ").capitalize()
        dias_internacion = int(input("Ingrese los días de internación: "))
        pacientes.append([historia_clinica,nombre,edad,diagnostico,dias_internacion])

        contador_ingresos+=1

        