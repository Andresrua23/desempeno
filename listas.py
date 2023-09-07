concesionario = []

def agregar(marca):
    concesionario.append(marca)

def eliminar(marca):
    if marca in concesionario:
        concesionario.remove(marca)
        print(f"El carro de marca '{marca}' ha sido eliminado")
    else:
        print(f"No existe un vehículo de marca '{marca}' que desee borrar")

def menu():
    print("\nOpciones:")
    print("1. Agregar carro")
    print("2. Eliminar carro")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        marca = input("Ingrese marca del carro: ")
        agregar(marca)
    elif opcion == '2':
        marca = input("Ingrese marca del carro que desea eliminar: ")
        eliminar(marca)
    else:
        print("Opción no válida. Intente de nuevo.")
    
    print("Concesionario:")
    print(concesionario)
