from funciones import *
#numero historia clinica, nombre paciente, edad paciente, diagnostico, cantidad de dias de internacion
pacientes=[]

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
            cantidad_pacientes_mas_5_dias_internacion(pacientes)
        case "8":
            promedio_dias_internacion(pacientes)
        case "9":
            print("¡Hasta luego!")
        case _:
            print("Error, opción incorrecta. Vuelva a seleccionar una opción:")