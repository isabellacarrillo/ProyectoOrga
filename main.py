from funciones import *

def main():

    lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota = descifrar_txt()
    print(lista_ordenada_cota, lista_ordenada_nombre)
    
    while True:

        option = input ("\nSeleccione una opción:\n1. Agregar Pintura\n2. Buscar Pintura\n3. Cambiar estado de la obra \n4. Eliminar Obra\n5. Compactar\n6. Salir del sistema\n==>")

        if option == "1":
            lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota = agregar_obra(lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota)
            print("Pintura Agregada Exitosamente!\n")

        elif option == "2" or  option == "3" or option == "4":
            pintura_buscada = buscar_pintura(lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota)
            if option == "2":
                if pintura_buscada != None:
                    if pintura_buscada.eliminado == "False":
                        print("""La pintura encontrada fue:
                        Cota: {}
                        Nombre: {}
                        Precio: {}
                        Año: {}
                        Status: {}
                        """.format(pintura_buscada.cota,pintura_buscada.nombre,pintura_buscada.precio,pintura_buscada.ano,pintura_buscada.status))

            elif option == "3":
                if pintura_buscada != None:
                    if pintura_buscada.eliminado == "False":
                        if pintura_buscada.status == "EN EXHIBICION":
                            pintura_buscada.status = "EN MANTENIMIENTO"
                        else:
                            pintura_buscada.status = "EN EXHIBICION"
                        print("Se ha realizado el cambio de manera exitosa.")
        
            elif option == "4":
                if pintura_buscada != None:
                    if pintura_buscada.eliminado == "False":
                        pintura_buscada.eliminado = "True"
                        print("Se elimino de manera exitosa.")
        
        elif option == "5":
            lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota = compactar_txt(lista_pinturas)
            print("Tanto la base de datos como las varibables locales han sido actualizadas")

        elif option == "6":
            guardar_txt(lista_pinturas)
            print("Adios!")
            break    
main()