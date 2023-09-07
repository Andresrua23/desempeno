concesionario = {}
contador = 0

#definir las indicaciones 

def agregar(marca, referencia):
    concesionario[marca]=referencia
    
def eliminar(marca):
    if marca in concesionario:
        del concesionario [marca]
        print(f"el carro {marca}ha sido eliminado")
    else:
        print(f"no existe el vehiculo de {marca} que desea borrar")
    
def menu():
    print("\nOpciones:")
    print("1. Agregar carro")
    print("2. Eliminar carro")
    
    #EVALUAR CADA OPCION
    
    while True:
        menu()
        opcion= input("Seleccione una opcion: ")
        if opcion==1:
            marca = input("Ingrese marca del carro: ")
            referencia = input(f"Ingrese la referencia de la marca '{marca}': ")
            agregar(marca,referencia)
        
        elif opcion==2:
            marca = input("Ingrese marca del carroque desea eliminar: ")
            eliminar(marca)
            
        break
    else:
        print("Opción no válida. Intente de nuevo.")
            
            
        

        # concesionario[marca] = referencia
        # contador += 1   
    
    
        # contador += 1

        # if contador >= 3:
        #     respuesta = input("¿Desea continuar ingresando datos? (Sí/No): ").lower()
        # if respuesta != 'si':
        #     print("Saliste del diccionario")
        # break

print("Concesionario:")
print(concesionario)

    
   
    
    
        