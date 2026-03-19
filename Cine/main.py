from models import *

print("=========== SISTEMA DE CINE ^u^ ===========\n")

usuarios = [
    Usuario(1,"Diego","d@gmail.com","222"),
    Usuario(2,"Ana","a@gmail.com","222"),
    Usuario(3,"Luis","l@gmail.com","222"),
    Usuario(4,"Maria","m@gmail.com","222"),
    Usuario(5,"Carlos","c@gmail.com","222"),
    Usuario(6,"Sofia","s@gmail.com","222"),
    Usuario(7,"Pedro","p@gmail.com","222"),
    Usuario(8,"Lucia","lu@gmail.com","222"),
    Usuario(9,"Jorge","j@gmail.com","222"),
    Usuario(10,"Elena","e@gmail.com","222")
]

print("Usuarios creados:")
for u in usuarios:
    print(u.nombre)

empleados = [
    Empleado(1,"Juan","j@gmail.com","111","Taquillero"),
    Empleado(2,"Laura","l@gmail.com","111","Admin"),
    Empleado(3,"Miguel","m@gmail.com","111","Limpieza"),
    Empleado(4,"Carmen","c@gmail.com","111","Taquillero"),
    Empleado(5,"Raul","r@gmail.com","111","Admin"),
    Empleado(6,"Paola","p@gmail.com","111","Limpieza"),
    Empleado(7,"Mario","m@gmail.com","111","Taquillero"),
    Empleado(8,"Fernanda","f@gmail.com","111","Admin"),
    Empleado(9,"Victor","v@gmail.com","111","Limpieza"),
    Empleado(10,"Andrea","a@gmail.com","111","Taquillero")
]

print("\nEmpleados creados:")
for e in empleados:
    print(e.nombre, "-", e.rol)

salas = [
    Sala("Sala1",50,"2D",False),
    Sala("Sala2",60,"3D",False),
    Sala("Sala3",40,"IMAX",True),
    Sala("Sala4",55,"2D",False),
    Sala("Sala5",45,"3D",True),
    Sala("Sala6",70,"IMAX",True),
    Sala("Sala7",50,"2D",False),
    Sala("Sala8",60,"3D",False),
    Sala("Sala9",40,"IMAX",True),
    Sala("Sala10",55,"2D",False)
]

peliculas = [
    Pelicula("Avengers",120,"Accion"),
    Pelicula("Batman",130,"Accion"),
    Pelicula("Frozen",100,"Animacion"),
    Pelicula("Titanic",150,"Drama"),
    Pelicula("Joker",140,"Drama"),
    Pelicula("Cars",90,"Animacion"),
    Pelicula("Spiderman",110,"Accion"),
    Pelicula("Avatar",160,"SciFi"),
    Pelicula("Coco",105,"Animacion"),
    Pelicula("Matrix",135,"SciFi")
]

print("\nPeliculas:")
for p in peliculas:
    print(p.titulo)

funciones = []
for i in range(10):
    f = Funcion(i+1, peliculas[i], salas[i], "8:00 PM", 50)
    funciones.append(f)

reservas = []
for i in range(10):
    r = Reserva(i+1, usuarios[i], funciones[i], ["A1","A2"])
    r.calcular_total()
    reservas.append(r)

print("\nReservas creadas correctamente ✔")

print("\n===== PRUEBAS DE METODOS =====")

reservas[0].confirmar_pago()
reservas[0].mostrar()
usuarios[0].crear_reserva(reservas[0])
usuarios[0].cancelar_reserva(reservas[0])
usuarios[0].crear_reserva(reservas[0])


# Menu
opcion = 0

while opcion != 6:

    print("\n====== MENU ======")
    print("1. Ver usuarios")
    print("2. Ver peliculas")
    print("3. Ver funciones")
    print("4. Ver reservas")
    print("5. Probar flujo completo")
    print("6. Salir")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("\nUsuarios:")
        for u in usuarios:
            print(u.nombre)

    elif opcion == 2:
        print("\nPeliculas:")
        for p in peliculas:
            print(p.titulo)

    elif opcion == 3:
        print("\nFunciones:")
        for f in funciones:
            f.detalles()

    elif opcion == 4:
        print("\nReservas:")
        for r in reservas:
            r.mostrar()

    elif opcion == 5:
        print("\n--- Flujo completo ---")

        r = reservas[1]

        print("\nAntes de pagar:")
        r.mostrar()

        print("\nPagando...")
        r.confirmar_pago()

        print("\nDespues de pagar:")
        r.mostrar()

    elif opcion == 6:
        print("\nFin del programa :)")

    else:
        print("Opcion invalida")