import os

aprendices = {}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("Pulse una tecla para continuar...")

def listar_aprendices():
    limpiar_pantalla()
    print("-------------------")
    print("LISTA DE APRENDICES")
    print("-------------------\n")

    for aprendiz_id, aprendiz_data in aprendices.items():
        nombre = aprendiz_data["Nombre"]
        apellido = aprendiz_data["Apellido"]

        print(f"{aprendiz_id}. {nombre} {apellido}")
    pausa()

contador_aprendiz = 1

def registrar_aprendices():
    nombre = input("Ingrese el nombre del aprendiz: ")
    apellido = input("Ingrese el apellido del aprendiz: ")
    global contador_aprendiz
    nuevo_aprendiz = {"Nombre": nombre, "Apellido": apellido}
    aprendices[contador_aprendiz] = nuevo_aprendiz
    contador_aprendiz += 1
    limpiar_pantalla()
    print("Nombre del aprendiz: ", nombre)
    print("Apellido del aprendiz: ", apellido)
    pausa()

def editar_aprendices():
    while True:
        try:
            limpiar_pantalla()
            submenu = int(input("MENU DE OPCIONES\n" + 
                "1. Editar nombre\n" +
                "2. Editar apellido\n" +
                "3. Regresar al menu anterior\n" +
                "Ingrese una opción: "))
            return submenu
        except ValueError:
            limpiar_pantalla()
            print("No se permite el ingreso de dato vacío.")
            pausa()

def eliminar_aprendiz():
    while True:
            try:
                limpiar_pantalla()
                listar_aprendices()
                codigo_aprendiz = int(input("Ingrese el código del aprendiz: "))
                if codigo_aprendiz in aprendices:
                    del aprendices[codigo_aprendiz]
                    return codigo_aprendiz
                else:
                    print("El código de aprendiz ingresado no existe.")
                    pausa()
                return codigo_aprendiz
            except ValueError:
                limpiar_pantalla()
                print("No se permite el ingreso de dato vacío.")
                pausa()

def menu(): 
    while True:
        try:
            limpiar_pantalla()
            print("------------------------------------------------------")
            print("BIENVENIDO A NUESTRO SOFTWARE DE GESTION DE APRENDICES")
            print("------------------------------------------------------\n")

            opcion = int(input("MENU DE OPCIONES\n" + 
                "1. Listar aprendices\n" +
                "2. Registrar aprendices\n" +
                "3. Editar aprendices\n" +
                "4. Eliminar aprendices\n" +
                "5. Salir del programa\n" +
                "Ingrese una opción: "))
            return opcion
        except ValueError:
            print("No se permite el ingreso de dato vacío.")
            pausa()

while True:
    opcion = menu()

    if opcion == 1:  
        listar_aprendices()
    elif opcion == 2:
        registrar_aprendices()
    elif opcion == 3:
        editar_aprendices()
    elif opcion == 4:
        eliminar_aprendiz()
    elif opcion == 5:
        limpiar_pantalla()
        print("Saliendo del programa...")
        break
    else:
        limpiar_pantalla()
        print("Opción no válida, intente de nuevo.")
