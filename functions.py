from Pintura import Pintura
db = {}

# CREAR LA NUEVA PINTURA
def nueva_pintura():

    while True:
        leer_db()
        cota = input("Ingrese la cota de la pintura: ")
        cota = cota.upper()

        cont = 0 
        for key,value in db.items():
            if value.cota == cota:
                print("La cota '", cota, "' ya esta registrada a otra pintura, ingrese una distinta")
                cont+=1

        if cont > 0:
            continue

        entero = 0
        string = 0

        for i in cota:

            try:
                a = int(i)
                entero += 1
            except:
                string += 1

        if (string == 4 and entero == 4):

            break
        
        print("La cota debe estar conformada por 4 letras y 4 numeros")

    while True:
        nombre = input("Ingrese el nombre de la pintura: ")
        if len(nombre) > 10:
            print("Ingrese un nombre de máximo 30 caracteres")
        elif nombre in db:
            print("El nombre ingresado ya existe")
        else:
            break

    while True:
        try:
            precio = float(input("Ingrese el precio de la pintura: "))
            if precio < 0:
                print("Ingrese un valor numérico válido")
            else:
                break
        except:
            print("Ingrese un valor numérico válido")
    
    
    while True:
        try:
            año = int(input("Ingrese el año de la pintura: "))
            if año < 0:
                print("Ingrese un valor numérico válido")
            if len(año)>4:
                 print("Ingrese un año válido")
            else:
                break
        except:
            print("Ingrese un valor numérico válido")

    while True:
        status = input("Seleccione el estado actual de la pintura dentro de la galería:\n1. EN EXHIBICIÓN\n2. EN MANTENIMIENTO\n")
        if status == "1":
            status = "EN EXHIBICIÓN"
            break
        elif status == "2":
            status = "EN MANTENIMIENTO"
            break
        else:
            print("Ingrese una opción válida")
        
    eliminado = False
    nueva_pintura = [cota.upper(),nombre,precio,año,status,eliminado]
    agregar_db(nueva_pintura)
    return nueva_pintura

# Agregar la pintura al txt

def agregar_db(lista):

    f = open("bd.txt", "a")   #cuando uso esto, cualquier cosa que agregue se va a agregar al final

    f.write("\n")    
    for i in lista:

        f.write(str(i) + "\n")   #convertimos los elementos de la lista en string

    f.close()

    return True

# aqui esta todo lo de cambio de status, eliminacion logica y eliminacion en fisico
def buscar_pintura():

    leer_db()

    encontrada = False
    while True:

        option = input("Seleccione una opción\n1. Buscar por cota\n2. Buscar por nombre\n3. Regresar\n")

        if option == "1":
            busqueda = input("Ingrese la cota de la pintura a buscar: ")

            for key, value in db.items():
                cota = value.cota

                if cota.lower() == busqueda.lower():
                    pintura = value
                    encontrada = True

            break

        elif option == "2":
            busqueda = input("Ingrese el nombre de la pintura a buscar: ")

            for key, value in db.items():
                name = value.nombre
                
                if name.lower() == busqueda.lower():
                    pintura = value
                    encontrada = True
            
            break

        elif option == "3":
            return True

        else:
            print("Seleccione una opción válida")

    if encontrada == False:
        print('No se han encontrado resultados de tu busqueda:' + ' "' + busqueda + '"\n')
    
    if encontrada == True:

        print("\nPintura encontrada!\nCota:", pintura.cota, "\n Nombre:",pintura.nombre, "\n Precio:",pintura.precio, "\n Año:",pintura.año, "\n Status:",pintura.status)

        while True:
            option = input("\n¿Qué desea hacer con esta pintura?\nSeleccione una opción:\n1. Cambiar Status\n2. Eliminar lógicamente\n3. Eliminar Físicamente\n4. Regresar\n")

            if option == "1":

                option2 = input("Seleccione el estado actual de la pintura dentro de la galería:\n1. EN EXHIBICIÓN\n2. EN MANTENIMIENTO\n3. Regresar\n")

                while True:

                    if option2 == "1":
                        status = "EN EXHIBICION"

                        pintura.status = status

                        overwrite()
                        print("Status cambiado exitosamente!\n")
                        break

                    elif option2 == "2":
                        status = "EN MANTENIMIENTO"
                        pintura.status = status

                        overwrite()
                        print("Status cambiado exitosamente!\n")
                        break

                    elif option2 == "3":

                        break

                    else:
                        print("Ingrese una opción válida")

                break

            elif option == "2":
                
                if pintura.eliminado == True:
                    print("La pintura ya se encuentra eliminada lógicamente")
                    break
                else:
                    eliminacion_logica(pintura)
                    break
                   
            elif option == "3":
                eliminacion_fisica(pintura)
                break
                   
            elif option == "4":
                
                break
                
    return True

def mostrar():
    leer_db()

    id = 1
    for key, value in db.items():
        if value.eliminado == True:
            condicion = "ELIMINADA"
        elif value.eliminado == False:
            condicion = "ACTIVA"

        print(str(id) + ".", "\nCota:",value.cota, "\nNombre:",value.nombre, "\nPrecio:",value.precio,"\nAño:",value.año,"\nStatus:",value.status, "\nCondicion:", condicion)
        id = int(id) + 1

    return True

def eliminacion_logica(pintura):

    pintura.eliminado = True
    overwrite()

    print("\nEliminada lógicamente con éxito\n")

    return True

def eliminacion_fisica(pintura):
    if pintura.eliminado == True:
        del db[pintura.nombre]
        overwrite()

        print("\n¡Pintura eliminada con éxito!\n")
    
    else:

        print("Primero se debe eliminar lógicamente\n")

    return True

def overwrite():
    f = open("bd.txt", "w")

    for key, value in db.items():
        f.write("\n")
        f.write(value.cota + "\n")
        f.write(value.nombre + "\n")
        f.write(str(value.precio) + "\n")
        f.write(value.status + "\n")
        f.write(str(value.eliminado) + "\n")

    return True


# LEER TXT

def leer_db():
    f = open("bd.txt", "r")

    next_cota = False
    next_nombre = False
    next_precio = False
    next_año = False
    next_status = False

    for line in f.readlines():
        
        if line.strip():

            if next_cota:

                cota = line.strip('\n')

                next_cota = False
                next_nombre = True

            elif next_nombre:

                nombre = line.strip('\n')

                next_nombre = False
                next_precio = True

            elif next_precio:

                precio = line.strip('\n')
                
                next_precio = False
                next_año = True

            elif next_año:

                año = line.strip('\n')
                
                next_año = False
                next_status = True

            elif next_status:

                status = line.strip('\n')
                
                next_status= False
                next_eliminado = True


            elif next_eliminado:

                eliminado = line.strip('\n')

                if eliminado == "False":
                    eliminado = False
                elif eliminado == "True":
                    eliminado = True
                    
                db[nombre] = Pintura(cota,nombre,float(precio),año,status,eliminado)        

        elif not line.strip():
            next_cota = True


    return True