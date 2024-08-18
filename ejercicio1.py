#aqui inicie la clase 
class ElPerroj():
    Tipo = "Perro"
    NombrePerro = ""
    Edad = 0
    Peso = 0
    Estado = "No Atendido"
    
    def __init__(self):
        self.Tipo = "Perro"
        self.Peso = 0
    
    def RegistrarPerro(self):
        self.Estado = "Atendido"
        print("ATENDIDO ")
#usare esta parte para ver si es perro grande o pequeño    
    def PesoPerro(self):
        if self.Peso > 10:
            print(f"Perro Grande su peso es: {self.Peso} kg")
        else:
            print(f"Perro Pequeño su peso es: {self.Peso} kg")
    
    def DatosPerro(self, Tipo, NomPer, Edad, PesoPerro,Estado):
        self.Tipo = Tipo
        self.NombrePerro = NomPer
        self.Edad = Edad
        self.Peso = PesoPerro
        self.Estado=Estado
#aqui es donde el usuario ingresa los datos de la mascota
    def RecibirDatosDelPerro(self):
        print("**************BIENVENIDOS****************")
        NomPer = input("Nombre de la Mascota: ")
        Edad = int(input("¿Cuál es la edad?: "))
        PesoPerro = int(input("¿Cuánto pesa en kg?: "))
        Estado=input("El perro ya Fue atendido? (S/N): ").lower()
        print("*********************************************")
        self.DatosPerro("Perro", NomPer, Edad, PesoPerro,Estado)
#aqui el usuario se le mostraran los datos en consola   
    def MostrarDatosPerro(self):
        print("**************BIENVENIDOS****************")
        print("El Nombre del perro es: ", self.NombrePerro)
        print("Edad del perro es: ", self.Edad)
        print("Peso del perro es: ", self.Peso, "kg")
        if self.Peso > 10:
            print("Este es un perro grande.")
        else:
            print("Este es un perro pequeño.")
        print("Estado: ", self.Estado)
        if self.Estado=="s":
            print("Su estado es Atendido.")
        else:
            print("Aun no fue atendido ")

# Creación de una instancia de ElPerro
perro1 = ElPerroj()
perro1.RecibirDatosDelPerro() 
perro1.MostrarDatosPerro() 
print("*****************************************")
