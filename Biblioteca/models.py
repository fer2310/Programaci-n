class Persona:
    
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Usuario(Persona):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.prestamos = []

    def realizarPrestamo(self, prestamo):
        self.prestamos.append(prestamo)
        print("Prestamo realizado")

    def historial(self):
        for p in self.prestamos:
            print("Prestamo:", p.idPrestamo)

class Bibliotecario(Persona):

    def aprobarPrestamo(self, prestamo):
        prestamo.estado = "APROBADO"

class Material:

    def __init__(self, idMaterial, titulo, año):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.año = año

class Libro(Material):

    def __init__(self, idMaterial, titulo, año, autor):
        super().__init__(idMaterial, titulo, año)
        self.autor = autor

class Revista(Material):

    def __init__(self, idMaterial, titulo, año, edicion):
        super().__init__(idMaterial, titulo, año)
        self.edicion = edicion

class Prestamo:

    def __init__(self, idPrestamo):
        self.idPrestamo = idPrestamo
        self.materiales = []
        self.estado = "PENDIENTE"

    def agregarMaterial(self, material):
        self.materiales.append(material)

    def mostrar(self):
        print("Prestamo:", self.idPrestamo)
        print("Estado:", self.estado)
        print("Materiales:")
        for m in self.materiales:
            print("-", m.titulo)
        return ""