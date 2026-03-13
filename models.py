class Persona():

    def __init__(self, ID, nombre, correo):
        self.IDPersona = ID
        self.nombre = nombre
        self.email = correo

    def login(self):
        print(self.nombre, "inicio sesion")

    def actualizar(self, nuevocorreo):
        self.email = nuevocorreo


class Cliente(Persona):

    def __init__(self, ID, nombre, correo):
        super().__init__(ID, nombre, correo)
        self.puntFidelidad = 0
        self.Pedidos = []

    def realizarPedido(self, pedido):
        self.Pedidos.append(pedido)
        print("Pedido completado")

    def Historial(self):
        for p in self.Pedidos:
            print("Numero de Pedido:", p.idPedido)


class Empleado(Persona):

    def __init__(self, idPersona, nombre, correo, idEmpleado, rol):
        super().__init__(idPersona, nombre, correo)
        self.idEmpleado = idEmpleado
        self.rol = rol

    def cambiarEstadoPedido(self, pedido, estado):
        pedido.estado = estado


class ProductoB():

    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase


class Bebida(ProductoB):

    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura


class Postre(ProductoB):

    def __init__(self, idProducto, nombre, precioBase, esVegano):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano


class Pedido():

    def __init__(self, idPedido):
        self.idPedido = idPedido
        self.productos = []
        self.estado = "PENDIENTE"
        self.total = 0

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        self.total = 0
        for p in self.productos:
            self.total += p.precioBase

    def validar_stock(self):
        print("Stock validado")

    def mostrar_detalle(self):

        print("Pedido:", self.idPedido)
        print("Estado:", self.estado)

        print("Productos:")
        for p in self.productos:
            print("-", p.nombre, "$", p.precioBase)

        print("Total:", self.total)

        return ""


class Inventario():

    def __init__(self):
        self.cafe_americano = 5
        self.leche = 5
        self.cafe_helado = 5
        self.capuchino = 5
        self.frappe = 5
        self.te_helado = 5
        self.latte = 5
        self.matcha = 5
        self.cafe_expresso = 5
        self.chocolate = 5

    def reducirStock(self):
        self.cafe_americano -= 1
        self.leche -= 1
        self.cafe_helado -= 1
        self.capuchino -= 1
        self.frappe -= 1
        self.te_helado -= 1
        self.latte -= 1
        self.matcha -= 1
        self.cafe_expresso -= -1
        self.chocolate -= 1