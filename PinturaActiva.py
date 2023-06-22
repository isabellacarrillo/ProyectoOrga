from Pintura import Pintura

class PinturaActiva(Pintura):

    def __init__(self,cota,nombre,precio,year):
        Pintura.__init__(self,cota,nombre,precio,year)
        self.status = "En Exhibicion"

    def getCota(self):
        return self.cota

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getYear(self):
        return self.year

    def getStatus(self):
        return self.status

    def getInfo(self):
        print("""  
{}

Cota: {}
Precio: ${}
Año: {}
Status: {}   
        """.format(self.nombre,self.cota,self.precio,self.year,self.status))

    