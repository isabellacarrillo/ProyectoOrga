from functions import *
from Pintura import Pintura

print("¡Bienvenido!")

while True:

    option = input ("\nSeleccione una opción:\n1. Agregar Pintura\n2. Buscar Pintura\n3. Mostrar todas las pinturas \n4. Salir del sistema\n==>")
    if option == "1":
        nueva_pintura()
        print("Pintura Agregada Exitosamente!\n")

    elif option == "2":
        buscar_pintura()

    elif option == "3":
        mostrar()
    
    elif option == "4":
        print("Chao!")
        break
    
    else:
        print("Seleccione una opción válida")