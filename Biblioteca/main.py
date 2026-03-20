from models import *

print("=== Usuarios ===\n")

u1 = Usuario(1,"Marco")
u2 = Usuario(2,"Valeria")
u3 = Usuario(3,"Rodrigo")
u4 = Usuario(4,"Fernanda")
u5 = Usuario(5,"Alonso")
u6 = Usuario(6,"Sofia")
u7 = Usuario(7,"Mateo")
u8 = Usuario(8,"Camila")
u9 = Usuario(9,"Sebastian")
u10 = Usuario(10,"Renata")

for u in [u1,u2,u3,u4,u5,u6,u7,u8,u9,u10]:
    print(u.nombre)

print("\n=== Bibliotecarios ===\n")

b1 = Bibliotecario(1,"Luis")
b2 = Bibliotecario(2,"Ana")
b3 = Bibliotecario(3,"Carlos")
b4 = Bibliotecario(4,"Diana")
b5 = Bibliotecario(5,"Pedro")
b6 = Bibliotecario(6,"Daniel")
b7 = Bibliotecario(7,"Mariana")
b8 = Bibliotecario(8,"Jorge")
b9 = Bibliotecario(9,"Lucia")
b10 = Bibliotecario(10,"Andres")

for b in [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]:
    print(b.nombre)

print("\n=== Materiales ===\n")

lib1 = Libro(1,"Python",2020,"Juan")
lib2 = Libro(2,"Java",2019,"Pedro")
lib3 = Libro(3,"C++",2018,"Luis")
lib4 = Libro(4,"HTML",2021,"Ana")
lib5 = Libro(5,"CSS",2022,"Carlos")
lib6 = Libro(6,"JavaScript",2021,"Maria")
lib7 = Libro(7,"Bases de Datos",2020,"Jose")

rev1 = Revista(8,"Tech",2024,10)
rev2 = Revista(9,"Ciencia",2023,5)
rev3 = Revista(10,"Historia",2022,3)
rev4 = Revista(11,"Arte",2021,8)
rev5 = Revista(12,"Salud",2020,6)
rev6 = Revista(13,"Gaming",2024,2)
rev7 = Revista(14,"Musica",2023,7)

materiales = [
    lib1,lib2,lib3,lib4,lib5,lib6,lib7,
    rev1,rev2,rev3,rev4,rev5,rev6,rev7
]

for m in materiales:
    print(m.titulo)

print("\n=== Prestamos ===\n")

p1 = Prestamo(1); p1.agregarMaterial(lib1)
p2 = Prestamo(2); p2.agregarMaterial(lib2)
p3 = Prestamo(3); p3.agregarMaterial(lib3)
p4 = Prestamo(4); p4.agregarMaterial(lib4)
p5 = Prestamo(5); p5.agregarMaterial(lib5)
p6 = Prestamo(6); p6.agregarMaterial(rev1)
p7 = Prestamo(7); p7.agregarMaterial(rev2)
p8 = Prestamo(8); p8.agregarMaterial(rev3)
p9 = Prestamo(9); p9.agregarMaterial(rev4)
p10 = Prestamo(10); p10.agregarMaterial(rev5)

prestamos = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

for p in prestamos:
    p.mostrar()

print("\n=== Historial ===\n")

usuarios = [u1,u2,u3,u4,u5,u6,u7,u8,u9,u10]

for i in range(10):
    usuarios[i].realizarPrestamo(prestamos[i])

for u in usuarios:
    u.historial()

# Menu
while True:

    print("\n=== Menu ===")
    print("1. Ver usuarios")
    print("2. Ver bibliotecarios")
    print("3. Ver materiales")
    print("4. Ver prestamos")
    print("5. Ver historial")
    print("6. Aprobar prestamo")
    print("7. Buscar material")
    print("8. Validar usuario")
    print("9. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        for u in usuarios:
            print(u.nombre)

    elif opcion == "2":
        for b in [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]:
            print(b.nombre)

    elif opcion == "3":
        for m in materiales:
            print(m.titulo)

    elif opcion == "4":
        for p in prestamos:
            p.mostrar()

    elif opcion == "5":
        for u in usuarios:
            u.historial()

    elif opcion == "6":
        print("\nAprobando prestamo 1...")
        b1.aprobarPrestamo(p1)
        p1.mostrar()

    elif opcion == "7":
        buscar = input("\nBuscar material: ").lower()

        encontrado = False

        for m in materiales:
            if buscar in m.titulo.lower():
                print("Encontrado:", m.titulo)
                encontrado = True

        if not encontrado:
            print("No encontrado")

    elif opcion == "8":
        if len(u1.prestamos) > 0:
            print(u1.nombre, "tiene prestamos")
        else:
            print(u1.nombre, "no tiene prestamos")

    elif opcion == "9":
        print("Fin del programa")
        break

    else:
        print("Opcion no valida")