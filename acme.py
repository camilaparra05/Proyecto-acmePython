from interfaz.menu import menu
from modelo import funciones
from interfaz.Inicio import inicio_sesion

print(" ***BIENVENIDO*** ")


inicio_sesion()
 

arch = funciones.cargar_archivo()
    
while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            funciones.registrar_grupo(arch)
            input("Ingrese una letra para volver al menù")
            
        elif opcion == "2":
            funciones.registrar_modulo(arch)
            input("Ingrese una letra para volver al menù")

        elif opcion == "3":
            funciones.registrar_estudiante(arch)
            input("Ingrese una letra para volver al menù")

        elif opcion == "4":
            funciones.registrar_docente(arch)
            input("Ingrese una letra para volver al menù")

        elif opcion == "5":
            funciones.registrar_asistencia(arch)
            input("Ingrese una letra para volver al menù")

        elif opcion == "6":
            funciones.consultar_estudiantes_por_grupo()
            input("Ingrese una letra para volver al menù")

        elif opcion == "7":
            funciones.consultar_estudiantes_por_modulo()
            input("Ingrese una letra para volver al menù")

        elif opcion == "8":
            funciones.consultar_docentes_por_modulo()
            input("Ingrese una letra para volver al menù")

        elif opcion == "9":
            funciones.consultar_estudiantes_por_docente()
            input("Ingrese una letra para volver al menù")

        elif opcion == "10":
            funciones.generar_informe_asistencia()
            input("Ingrese una letra para volver al menù")

        elif opcion == "11":
            print("Saliendo del sistema...")
            funciones.guardar_informacion(arch)
            break
        else:
            print("Opción no válida. Intente nuevamente.")


 

menu()

print("Gracias por usar")