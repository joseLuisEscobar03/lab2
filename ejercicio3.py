#aqui lleva el nombre de las clases 
class Autos():
    Marca=""
    Modelo=""
    Año=0
    Color=""
    Tipo=""
    Placa=""
    Numero_Motor=""
    PrecioCosto=0
    PrecioVenta=0
    Asientos=0
    Ruedas=0

# aqui el Bob Constructor
    def __init__(self):
        self.PrecioCosto=0
        self.PrecioVenta=0
        self.Numero_Motor=""
        self.Año=0
        self.Asientos=0
        self.Ruedas=0

#como saldra el area de compra
    def InfoDelVehiCULO(self):
        self.PrecioVenta=self.PrecioCosto*1.4
        print(f"El vehiculo fue adquerido a: ${self.PrecioCosto}")
        print(f"El vehiculo queda a: ${self.PrecioVenta}")
        
 #aqui es donde el usuario ingresa los datos de la Compra  
    def RegistrarVehiculo(self):
        self.Marca=input("Marca del vehiculo: ")
        self.Modelo=input("Modelo del vehiculo: ")
        self.Año=int(input("Año del vehiculo: "))
        self.Color=input("Color del Vehiculo: ")
        self.Tipo=input("Tipo de vehiculo: ")
        self.Placa=input("Placa: ")
        self.Numero_Motor=input("Numero de Motor: ")
        self.Asientos=int(input("Cantidad de Asientos: "))
        self.Ruedas=int(input("Cantidad de Ruedas: "))
        self.PrecioCosto=int(input("Precio Costo: $"))

    def DatosRayoMcqueen(self,Marca,Modelo,Año,Color,Tipo,Vin,Numero_Motor,PrecioCosto,PrecioVenta,Asientos,Ruedas):    
        self.Marca=Marca
        self.Modelo=Modelo
        self.Año=Año
        self.Color=Color
        self.Tipo=Tipo
        self.Placa=Placa
        self.Numero_Motor=Numero_Motor
        self.PrecioCosto=PrecioCosto
        self.PrecioVenta=PrecioVenta
        self.Asientos=Asientos    
        self.Ruedas=Ruedas
#la salida de los datos       
    def MostrarDatos(self):
        print("Gracias por comprar en nuestro concecionario :D")
        print("Marca del vehiculo: ",self.Marca)
        print("Modelo del vehiculo: ",self.Modelo)
        print("Año del vehiculo: ",self.Año)
        print("Color del Vehiculo: ",self.Color)
        print("Tipo de vehiculo: ",self.Tipo)
        print("Placa: ",self.Placa)
        print("Numero de Motor: ",self.Numero_Motor)
        print("Cantidad de Asientos: ",self.Asientos)
        print("Cantidad de Ruedas: ",self.Ruedas)
        self.InfoDelVehiCULO()

Carro=Autos()
print("*********BIENVENIDOS AL CONSESIONARIO **************")
Carro.RegistrarVehiculo()
print("**********************************************************")
Carro.MostrarDatos()
