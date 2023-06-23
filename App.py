import pickle
from Pintura import Pintura
from PinturaActiva import PinturaActiva
from PinturaMantenimiento import PinturaMantenimiento

class App():

    def __init__(self):
        self.pinturas = []
        self.pinturasactivas = []
        self.pinturasmantenimiento = []
        self.letras = ["A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.numeros = ["0","1","2","3","4","5","6","7","8","9"]

    def registrar_pinturas(self):

        while True:
            cota = input("""
Ingrese la cota de la pintura (Debe contener 4 letras mayusculas seguidas de 4 numeros)
>>> """)
            if len(cota) != 8:
                print("Error.")
                continue
            elif cota[0] not in self.letras or cota[1] not in self.letras or cota[2] not in self.letras or cota[3] not in self.letras:
                print("Error.")
                continue
            elif cota[4] not in self.numeros or cota[5] not in self.numeros or cota[6] not in self.numeros or cota[7] not in self.numeros:
                print("Error.")
                continue
            elif self.pinturas != []:
                comprobar = 0
                for i in range(len(self.pinturas)):
                    if cota == self.pinturas[i].getCota():
                        print("Error. 2 pinturas no deben tener la misma cota.")
                        comprobar = 1
                        break
                if comprobar == 0:
                    break
                elif comprobar == 1:
                    continue
            else:
                break

        while True:
            nombre = input("""
Ingrese el nombre de la pintura que desea ingresas (debe contener maximo 10 caracteres y todos deben ser letras mayusculas)
>>> """)
            if len(nombre) > 10:
                print("Error. El nombre debe tener menos de 10 caracteres.")
                continue

            comprobar = 1

            for i in range(len(nombre)):
                if nombre[i] not in self.letras:
                    print("Error. El nombre no debe contener numeros, letras minusculas o caracteres especiales.")
                    comprobar = 0
                    break

            comprobar1 = 1

            if self.pinturas != []:
                for i in range(len(self.pinturas)):
                    if nombre == self.pinturas[i].getNombre():
                        print("Error. Dos pinturas no deben tener el mismo nombre.")
                        comprobar1 = 0
                        break

            if comprobar == 0 or comprobar1 == 0:
                continue
            else:
                break

        while True:
            try: 
                precio = int(input("""
Ingrese el precio de la pintura: 
>>> """))
                if precio < 0:
                    print("Error. El precio no debe ser negativo.")
                    continue
                else:
                    break
            except:
                print("Error. Ingrese un numero valido.")
                continue

        while True:
            try: 
                year = int(input("""
Ingrese el año en que se realizo la pintura: 
>>> """))
                if year < 0:
                    print("Error. El año no debe ser negativo.")
                    continue
                else:
                    break
            except:
                print("Error. Ingrese un numero valido.")
                continue

        self.pinturas.append(PinturaActiva(cota,nombre,precio,year))
        self.pinturasactivas.append(PinturaActiva(cota,nombre,precio,year))

    def consultar_pintura(self):
        comprobar = 0
        if self.pinturasactivas == [] and self.pinturasmantenimiento == []:
            print("No se encuentra ninguna pintura registrada en este momento.")
        else:
            while True:
                opcion = input("""\nIngrese el numero correspondiente al metodo por el cual desea buscar la pintura:
1. Cota
2. Nombre
>>> """)
                if opcion != "1" and opcion != "2":
                    print("Error.")
                    continue
                else:
                    if opcion =="1":
                        while True:
                            opcion1 = input("\nIngrese la cota de la pintura que desea buscar:\n>>> ")
                            if len(opcion1) != 8:
                                print("Error.")
                                continue
                            elif opcion1[0] not in self.letras or opcion1[1] not in self.letras or opcion1[2] not in self.letras or opcion1[3] not in self.letras:
                                print("Error.")
                                continue
                            elif opcion1[4] not in self.numeros or opcion1[5] not in self.numeros or opcion1[6] not in self.numeros or opcion1[7] not in self.numeros:
                                print("Error.")
                                continue
                            else:
                                for i in range(len(self.pinturas)):
                                    if self.pinturas[i].getCota() != opcion1:
                                        continue
                                    elif self.pinturas[i].getCota() == opcion1:
                                        comprobar = 1
                                        print(self.pinturas[i].getInfo())
                                if comprobar == 0:
                                    print("No se ha registrado ninguna pintura con la cota que ha introducido.")
                                break
                        break
                    if opcion == "2":
                        while True:
                            opcion1 = input("\nIngrese el nombre correspondiente a la pintura que desea buscar:\n>>> ")
                            if len(opcion1) > 10:
                                print("Error. El nombre debe tener menos de 10 caracteres.")
                                continue
                            comprobar1 = 1
                            while True:
                                for i in range(len(opcion1)):
                                    if opcion1[i] not in self.letras:
                                        print("Error. El nombre no debe contener numeros.")
                                        comprobar1 = 0
                                        break
                                break
                            if comprobar1 == 0:
                                continue

                            for i in range(len(self.pinturas)):
                                if self.pinturas[i].getNombre() != opcion1:
                                    continue
                                elif self.pinturas[i].getNombre() == opcion1:
                                    comprobar = 1
                                    print(self.pinturas[i].getInfo())
                            if comprobar == 0:
                                print("No se ha registrado ninguna pintura con este nombre.")
                            break
                        break

    def cambiar_status(self):
        while True:
            opcion = input("""\nIngrese el numero correspondiente a la accion que desea realizar:
1. Cambiar el status de una pintura en exhibicion a una en mantenimiento.
2. Cambiar el status de una pintura en mantenimiento a una en exhibicion.
>>> """)
            if opcion != "1" and opcion != "2":
                print("Error. ")
                continue
            else:
                if opcion == "1":
                    if self.pinturasactivas == []:
                        print("No se encuentran pinturas en exhibicion actualmente")
                        break
                    else:
                        print("A continuacion se le mostrara las pinturas que se encuentra actualmente en exhibicion:\n")
                        for i in range(len(self.pinturasactivas)):
                            print(f"{i+1}. {self.pinturasactivas[i].getInfo()}")
                        try:
                            opcion1 = int(input("\nIngrese el numero correspondiente a la pintura que desea colocar en mantenimiento:\n>>> "))
                            pintura = self.pinturasactivas[opcion1-1]
                            self.pinturasmantenimiento.append(PinturaMantenimiento(pintura.getCota(),pintura.getNombre(),pintura.getPrecio(),pintura.getYear()))
                            self.pinturasactivas.remove(pintura)
                            for i in range(len(self.pinturas)):
                                if pintura.getNombre() == self.pinturas[i].getNombre():
                                    self.pinturas.remove(self.pinturas[i])
                                    self.pinturas.append(PinturaMantenimiento(pintura.getCota(),pintura.getNombre(),pintura.getPrecio(),pintura.getYear()))
                            break
                        except:
                            print("Error. Debe ingresar un numero valido.")
                            continue
                elif opcion == "2":
                    if self.pinturasmantenimiento == []:
                        print("No se encuentran pinturas en mantenimiento actualmente")
                        break
                    else:
                        print("A continuacion se le mostrara las pinturas que se encuentra actualmente en mantenimiento:\n")
                        for i in range(len(self.pinturasmantenimiento)):
                            print(f"{i+1}. {self.pinturasmantenimiento[i].getInfo()}")
                        try:
                            opcion1 = int(input("\nIngrese el numero correspondiente a la pintura que desea colocar en exhibicion:\n>>> "))
                            pintura = self.pinturasmantenimiento[opcion1-1]
                            self.pinturasactivas.append(PinturaActiva(pintura.getCota(),pintura.getNombre(),pintura.getPrecio(),pintura.getYear()))
                            self.pinturasmantenimiento.remove(pintura)
                            for i in range(len(self.pinturas)):
                                if pintura.getNombre() == self.pinturas[i].getNombre():
                                    self.pinturas.remove(self.pinturas[i])
                                    self.pinturas.append(PinturaActiva(pintura.getCota(),pintura.getNombre(),pintura.getPrecio(),pintura.getYear()))
                            break
                        except:
                            print("Error. Debe ingresar un numero valido.")
                            continue
                break

    def escribir_objetos(self,archivo,datos):
        escribir = open(archivo,"wb")
        datos = pickle.dump(datos,escribir)
        escribir.close()

    def guardar_datos(self):
        """Esta funcion permitira guardar todo lo que haya realizado el usuario"""
        pintura = []
        for x in self.pinturas:
            pintura.append(x)
        self.escribir_objetos("pinturas.pickle",self.pinturas)

    def leer_objetos(self,archivo,datos):
        with open(archivo,"rb") as x:
            datos = pickle.load(x)
            return datos

    def leer_datos(self):
        """Esta funcion leera los datos que haya proporcionado el usuario anterior para preservarlos"""
        self.pinturas = self.leer_objetos("pinturas.pickle", self.pinturas)

    def start(self):
#        self.leer_datos()
        for i in range(len(self.pinturas)):
            print(self.pinturas[i].getInfo())
        print("BIENVENIDO AL MUSEO SAMAN")

        while True:
            opcion = input("""
Ingrese el numero correspondiente a la accion que desea realizar:
1. Registrar nueva pintura
2. Consultar una pintura
3. Cambiar el status de una pintura
4. Eliminar una pintura       
5. Salir  
>>> """)

            if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
                print("Error.")
                continue

            else:
                if opcion == "1":
                    self.registrar_pinturas()

                elif opcion == "2":
                    self.consultar_pintura()

                elif opcion == "3":
                    self.cambiar_status()

                elif opcion == "4":
                    continue

                else:
                    self.guardar_datos()
                    break
                    
