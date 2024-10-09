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
            pass
        case "3":
            pass
        case "4": 
            pass
        case "5":
            pass
        case "6": 
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            print("¡Hasta luego!")
        case _:
            print("Error, opción incorrecta. Vuelva a seleccionar una opción:")