from Pintura import Pintura
import re

def validar_input(input_usuario):
    patron = r'^[a-zA-Z]{4}\d{4}$'
    if re.match(patron, input_usuario):
        return True
    else:
        return False
    

def leer_txt():
    with open('pinturas.txt', 'r') as archivo:
    # Leer todo el contenido del archivo
        contenido = archivo.read()
    return contenido

def descifrar_txt():
    contenido=leer_txt()
    lista_pinturas = []
    lista_ordenada_nombre = []
    lista_ordenada_cota = []
    lista_de_obras_desordenada = contenido.split("\n")
    for obra in lista_de_obras_desordenada:
        propiedades_obra = obra.split("//")
        eliminado = propiedades_obra[5]
        obra_aux = Pintura(propiedades_obra[0],propiedades_obra[1],propiedades_obra[2],propiedades_obra[3],propiedades_obra[4],propiedades_obra[5])
        cota = propiedades_obra[0]
        nombre = propiedades_obra[1]
        indice = len(lista_pinturas)
        nodo_cota = [cota,indice]
        nodo_nombre = [nombre,indice]
        lista_ordenada_nombre = insertar_ordenado(lista_ordenada_nombre,nodo_nombre)
        lista_ordenada_cota = insertar_ordenado(lista_ordenada_cota,nodo_cota)
        lista_pinturas.append(obra_aux)
    return lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota


def insertar_ordenado(lista_ordenada, nodo):
    if len(lista_ordenada) == 0:
        lista_ordenada.append(nodo)
    else:
        indice_insertar = len(lista_ordenada)
        for i, nodo_aux in enumerate(lista_ordenada):
            if nodo[0] < nodo_aux[0]:
                indice_insertar = i
                break
        lista_ordenada.insert(indice_insertar, nodo)
    return lista_ordenada

#Sirve.
def agregar_obra(lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota):

    #Escribir cota
    while True:
        cota = input("\nIngrese la cota de la pintura: ")
        cota = cota.upper()
        

        verificacion = busqueda_binaria(lista_ordenada_cota , cota)
        if verificacion == -1:
            if validar_input(cota):
                break
            else:
                print("Formato inválido. Asegurese de que el formato sean cuatro letras seguidas de cuatro números.")
        else:
            print("Cota ya registrado. Ingresar otro valor.")


    #Escribir nombre
    while True:
        nombre = input("Ingrese el nombre de la pintura: ")
        nombre = nombre.upper()
        verificacion = busqueda_binaria(lista_ordenada_cota , nombre)
        if verificacion == -1:
            if len(nombre) < 10:
                break
            else: 
                print("El nombre debe de tener menos de 10 caracteres.")
        else:
            print("Nombre ya registrado. Ingresar otro valor")

    #Escribir precio
    while True:
        try:
            precio = float(input("Ingrese el precio de la pintura: "))
            if precio > 0:
                break
        except:
            print("Ingrese un dato númerico")

    #Escribir año
    while True:
        try:
            ano = int(input("Ingrese el año de la pintura: "))
            break
        except:
            print("Ingrese un valor numérico válido")

    #Escribir estado
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
    
    #Escribir eliminado
    eliminado = "False"

    #Agregar nueva Pintura
    nueva_pintura = Pintura(cota,nombre,precio,ano,status,eliminado)
    indice = len(lista_pinturas)
    nodo_cota = [cota,indice]
    nodo_nombre = [nombre,indice]
    lista_ordenada_nombre = insertar_ordenado(lista_ordenada_nombre,nodo_nombre)
    lista_ordenada_cota = insertar_ordenado(lista_ordenada_cota,nodo_cota)
    lista_pinturas.append(nueva_pintura)
    return lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota

#Sirve.
def buscar_pintura(lista_pinturas,lista_ordenada_nombre,lista_ordenada_cota):
    while True:
        option = input("Seleccione una opción\n1. Buscar por cota\n2. Buscar por nombre\n3. Regresar\n")
        

        if option == "1":
            buscado = input("Introduce la cota de la obra: ").upper()
            indice = busqueda_binaria(lista_ordenada_cota, buscado)
            indice_final = lista_ordenada_cota[indice][1]
            break

        elif option == "2":
            buscado = input("Introduce el nombre de la obra: ").upper()
            indice = busqueda_binaria(lista_ordenada_nombre, buscado)
            indice_final = lista_ordenada_nombre[indice][1]
            break

        elif option == "3":
            return None
    if indice != -1:
        return lista_pinturas[indice_final]
    else:  
        print("No se encontro obra asociada a la clave ", buscado)
        return None
        

def guardar_txt(lista_pinturas):
    with open("pinturas.txt", "w") as archivo:
        lineas = ["{}//{}//{}//{}//{}//{}".format(pintura.cota, pintura.nombre, pintura.precio, pintura.ano, pintura.status, pintura.eliminado) for pintura in lista_pinturas]
        archivo.write("\n".join(lineas))

def compactar_txt(lista_pinturas):
    with open("pinturas.txt", "w") as archivo:
        lineas = []
        for pintura in lista_pinturas:
            if pintura.eliminado == "False":
                linea = "{}//{}//{}//{}//{}//{}".format(pintura.cota, pintura.nombre, pintura.precio, pintura.ano, pintura.status, pintura.eliminado)
                lineas.append(linea)
        archivo.write("\n".join(lineas))
    return descifrar_txt()
        
#Sirve.
def busqueda_binaria(lista, valor_buscado):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio][0] == valor_buscado:
            return medio
        
        elif lista[medio][0] > valor_buscado:
            fin = medio - 1

        else:
            inicio = medio + 1

    return -1