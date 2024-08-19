class PHR():
    TipoProducto=""
    Modelo=""
    Almacenamiento=0
    RAM=0
    PrecioCosto=0
    PrecioVenta=0
#constructor
    def __init__(self):
        self.PrecioCosto=0
        self.PrecioVenta=0
        self.Almacenamiento=0
        self.RAM=0
#la informacion del pago
    def InfoDelProducto(self):
        self.PrecioVenta=self.PrecioCosto*1.7
        print(f"El Articulo fue comprado a: ${self.PrecioCosto}")
        print(f"El Articulo queda a: ${self.PrecioVenta}")
        
#como se registraran los datos que digite el usuario a la hora de la compra
    def RegistrarProducto(self):
        print("*****************BIENVENIDOS A PHR**************")
        self.TipoProducto=input("Tipo de Producto: ")
        self.Modelo=input("Modelo: ")
        self.Almacenamiento=int(input("Almacenamiento: "))
        self.RAM=int(input("RAM: "))
        self.PrecioCosto=int(input("Precio Proveedor: $"))
        
    def DatosPHR(self,PrecioCosto,PrecioVenta,TipoProducto,Modelo,Almacenamiento,RAM):    
        self.TipoProducto=TipoProducto
        self.Modelo=Modelo
        self.Almacenamiento=Almacenamiento
        self.RAM=RAM
        self.PrecioCosto=PrecioCosto
        self.PrecioVenta=PrecioVenta

#la salida de los datos       
    def MostrarDatos(self):
        print("Tipo de producto: ",self.TipoProducto)
        print(f"Modelo del {self.TipoProducto}: ",self.Modelo)
        print("Almacenamiento: ",self.Almacenamiento," Gigas")
        print("RAM: ",self.RAM, " Gigas")
        self.InfoDelProducto()

Articulo=PHR()
Articulo.RegistrarProducto()
print("**********************************************************")
Articulo.MostrarDatos()
print("*****************************************")
        
