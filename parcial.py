from funciones import *
#numero historia clinica, nombre paciente, edad paciente, diagnostico, cantidad de dias de internacion
pacientes=[
    [12, "juan", 34, "hepatitis", 9],
    [13, "lucia", 21, "fiebre", 0],
    [14, "horacio", 11, "leucemia", 60],
    [15, "pepe", 45, "fractura", 2]
]
seleccion=0
while seleccion !="9":
    menu()
    seleccion=input("Ingrese su opcion: ")
    match seleccion:
        case "1": 
            cargar_pacientes(pacientes)
        case "2":
            mostrar_pacientes(pacientes)
        case "3":
            buscar_pacientes_numero_historial(pacientes)
        case "4": 
            ordernar_historial_ascendente(pacientes)
        case "5":
            paciente_mayor_dias_internación(pacientes)
        case "6": 
            paciente_menor_dias_internación(pacientes)
        case "7":
            pass
        case "8":
            pass
        case "9":
            print("¡Hasta luego!")
        case _:
            print("Error, opción incorrecta. Vuelva a seleccionar una opción:")