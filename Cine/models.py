class Persona:
    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        print(self.nombre, "inicio sesion")

    def actualizar(self, email, telefono):
        self.email = email
        self.telefono = telefono
        print("Datos actualizados")


class Usuario(Persona):
    def __init__(self, id, nombre, email, telefono):
        super().__init__(id, nombre, email, telefono)
        self.puntos = 0
        self.reservas = []

    def crear_reserva(self, reserva):
        self.reservas.append(reserva)
        print("Reserva creada")

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            print("Reserva cancelada")
        else:
            print("No se encontro la reserva")

    def ver_reservas(self):
        print("\nReservas de", self.nombre)
        for r in self.reservas:
            r.mostrar()


class Empleado(Persona):
    def __init__(self, id, nombre, email, telefono, rol):
        super().__init__(id, nombre, email, telefono)
        self.rol = rol

    def marcar_entrada(self):
        print(self.nombre, "marco entrada")

    def cambiar_rol(self, nuevoRol):
        self.rol = nuevoRol
        print("Rol actualizado")


class Sala:
    def __init__(self, nombre, capacidad, tipo, vip):
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo
        self.vip = vip

    def mostrar(self):
        print(self.nombre, "-", self.tipo, "- Capacidad:", self.capacidad)


class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def sinopsis(self):
        print("Sinopsis de", self.titulo)

    def mostrar(self):
        print(self.titulo, "-", self.genero, "-", self.duracion, "min")


class Funcion:
    def __init__(self, id, pelicula, sala, hora, precio):
        self.id = id
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora
        self.precio = precio

    def detalles(self):
        print("Pelicula:", self.pelicula.titulo)
        print("Sala:", self.sala.nombre)
        print("Hora:", self.hora)
        print("Precio: $", self.precio)


class Reserva:
    def __init__(self, id, usuario, funcion, asientos):
        self.id = id
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.estado = "PENDIENTE"
        self.total = 0

    def calcular_total(self):
        self.total = len(self.asientos) * self.funcion.precio

    def confirmar_pago(self):
        self.estado = "PAGADA"
        print("Pago confirmado")

    def mostrar(self):
        print("\n--- Reserva ---")
        print("Usuario:", self.usuario.nombre)
        print("Pelicula:", self.funcion.pelicula.titulo)
        print("Sala:", self.funcion.sala.nombre)
        print("Asientos:", self.asientos)
        print("Estado:", self.estado)
        print("Total: $", self.total)