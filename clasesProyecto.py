from datetime import date

class Clientes:
    def __init__(self, IdClientes, TipoDocumento, PrimerNombre, OtrosNombres, PrimerApellido, SegundoApellido, CorreoElectronico, Celular, FechaNacimiento, Genero, Contrasena):
        self.IdClientes = IdClientes
        self.TipoDocumento = TipoDocumento
        self.PrimerNombre = PrimerNombre
        self.OtrosNombres = OtrosNombres
        self.PrimerApellido = PrimerApellido
        self.SegundoApellido = SegundoApellido
        self.CorreoElectronico = CorreoElectronico
        self.Celular = Celular
        self.FechaNacimiento = FechaNacimiento
        self.Genero = Genero
        self.Contrasena = Contrasena

    def realizarCompra(self):
        print(f"{self.PrimerNombre} está realizando una compra.")
        
    def verProductos(self):
        print(f"{self.PrimerNombre} está viendo los productos.")

    def verServicios(self):
        print(f"{self.PrimerNombre} está viendo los servicios.")
        
class Productos:
    def __init__(self, IdProductos, CategoriaProducto, nombre, FechaVencimiento, precio):
        self.IdProductos = IdProductos
        self.CategoriaProducto = CategoriaProducto
        self.nombre = nombre
        self.FechaVencimiento = FechaVencimiento
        self.precio = precio

    def mostrarDetalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Vence el: {self.FechaVencimiento}")

class Servicios:
    def __init__(self, IdServicios, CategoriaServicio, descripcion, precio):
        self.IdServicios = IdServicios
        self.CategoriaServicio = CategoriaServicio
        self.descripcion = descripcion
        self.precio = precio

    def mostrarDetalles(self):
        print(f"Servicio: {self.descripcion}, Precio: {self.precio}")

class Tiendas:
    def __init__(self, IdTiendas, Nit, NombreTiendas):
        self.IdTiendas = IdTiendas
        self.Nit = Nit
        self.NombreTiendas = NombreTiendas

    def listarProductos(self):
        print(f"Listando productos de {self.NombreTiendas}.")
        
    def listarServicios(self):
        print(f"Listando servicios de {self.NombreTiendas}.")

    def realizarVenta(self):
        print(f"Realizando una venta en {self.NombreTiendas}.")

class Repartidor:
    def __init__(self, IdRepartidor, TipoDocumento, PrimerNombre, OtrosNombres, PrimerApellido, SegundoApellido, CorreoElectronico, Celular, FechaNacimiento, Genero, Contrasena):
        self.IdRepartidor = IdRepartidor
        self.TipoDocumento = TipoDocumento
        self.PrimerNombre = PrimerNombre
        self.OtrosNombres = OtrosNombres
        self.PrimerApellido = PrimerApellido
        self.SegundoApellido = SegundoApellido
        self.CorreoElectronico = CorreoElectronico
        self.Celular = Celular
        self.FechaNacimiento = FechaNacimiento
        self.Genero = Genero
        self.Contrasena = Contrasena

    def asignarPedido(self):
        print(f"Pedido asignado a {self.PrimerNombre} {self.PrimerApellido}.")
        
    def entregarProducto(self):
        print(f"{self.PrimerNombre} está entregando un producto.")
        
class Ubicacion:
    def __init__(self, IdUbicacion, Direccion, IdTiendas, IdClientes):
        self.IdUbicacion = IdUbicacion
        self.Direccion = Direccion
        self.IdTiendas = IdTiendas
        self.IdClientes = IdClientes

    def asignarUbicacion(self):
        print(f"Ubicación asignada: {self.Direccion} para la tienda {self.IdTiendas} y cliente {self.IdClientes}.")
        

cliente1 = Clientes(1, 123456, "Juan", "Perez", "Lopez", "Gonzalez", "juan@mail.com", 123456789, date(1990, 5, 12), 1, "password123")
producto1 = Productos(1, 1, "Camiseta", date(2025, 5, 12), 15.99)

cliente1.realizarCompra()
cliente1.verProductos()

servicio1 = Servicios(1, 1, "Envío a domicilio", 5.99)
cliente1.verServicios()
ubicacion1 = Ubicacion(1, "Calle Falsa 123", 1, 1)
ubicacion1.asignarUbicacion()
tienda1 = Tiendas(1, 123456789, "Tienda XYZ")
repartidor1 = Repartidor(1, 987654321, "Carlos", "Diaz", "Martinez", "Rodriguez", "carlos@mail.com", 987654321, date(1985, 8, 15), 1, "repartidorpass")
tienda1.listarProductos()
tienda1.realizarVenta()
repartidor1.asignarPedido()
repartidor1.entregarProducto()
tienda1.listarServicios()
