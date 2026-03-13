from models import *

print("===Clientes===\n")

cli1 = Cliente(1,"Marco","marco@gmail.com")
cli2 = Cliente(2,"Valeria","valeria@gmail.com")
cli3 = Cliente(3,"Rodrigo","rodrigo@gmail.com")
cli4 = Cliente(4,"Fernanda","fernanda@gmail.com")
cli5 = Cliente(5,"Alonso","alonso@gmail.com")
cli6 = Cliente(6,"Sofia","sofia@gmail.com")
cli7 = Cliente(7,"Mateo","mateo@gmail.com")
cli8 = Cliente(8,"Camila","camila@gmail.com")
cli9 = Cliente(9,"Sebastian","sebastian@gmail.com")
cli10 = Cliente(10,"Renata","renata@gmail.com")

print(cli1.nombre)
print(cli2.nombre)
print(cli3.nombre)
print(cli4.nombre)
print(cli5.nombre)
print(cli6.nombre)
print(cli7.nombre)
print(cli8.nombre)
print(cli9.nombre)
print(cli10.nombre)

print("\n===Empleados===\n")

emp1 = Empleado(1,"Luis","luis@gmail.com",101,"Cajero")
emp2 = Empleado(2,"Ana","ana@gmail.com",102,"Barista")
emp3 = Empleado(3,"Carlos","carlos@gmail.com",103,"Gerente")
emp4 = Empleado(4,"Diana","diana@gmail.com",104,"Barista")
emp5 = Empleado(5,"Pedro","pedro@gmail.com",105,"Cajero")
emp6 = Empleado(6,"Daniel","daniel@gmail.com",106,"Barista")
emp7 = Empleado(7,"Mariana","mariana@gmail.com",107,"Cajera")
emp8 = Empleado(8,"Jorge","jorge@gmail.com",108,"Supervisor")
emp9 = Empleado(9,"Lucia","lucia@gmail.com",109,"Barista")
emp10 = Empleado(10,"Andres","andres@gmail.com",110,"Cajero")

print(emp1.nombre)
print(emp2.nombre)
print(emp3.nombre)
print(emp4.nombre)
print(emp5.nombre)
print(emp6.nombre)
print(emp7.nombre)
print(emp8.nombre)
print(emp9.nombre)
print(emp10.nombre)

print("\n===Productos===\n")

prod1 = Bebida(1,"Cafe Americano",45,"Grande","Caliente")
prod2 = Bebida(2,"Capuchino",55,"Mediano","Caliente")
prod3 = Bebida(3,"Latte",60,"Grande","Caliente")
prod4 = Bebida(4,"Te Helado",50,"Grande","Frio")
prod5 = Bebida(5,"Frappe",70,"Grande","Frio")

prod6 = Postre(6,"Cheesecake",65,False)
prod7 = Postre(7,"Croissant",35,False)
prod8 = Postre(8,"Brownie",40,False)
prod9 = Postre(9,"Galleta",25,False)
prod10 = Postre(10,"Pastel Vegano",60,True)

print(prod1.nombre)
print(prod2.nombre)
print(prod3.nombre)
print(prod4.nombre)
print(prod5.nombre)
print(prod6.nombre)
print(prod7.nombre)
print(prod8.nombre)
print(prod9.nombre)
print(prod10.nombre)

print("\n===Inventario===\n")

inventario = Inventario()
print("Inventario inicial cargado")

print("\n===Pedidos===\n")

pedido1 = Pedido(1)
pedido1.agregarProducto(prod1)
pedido1.agregarProducto(prod6)

pedido2 = Pedido(2)
pedido2.agregarProducto(prod2)
pedido2.agregarProducto(prod7)

pedido3 = Pedido(3)
pedido3.agregarProducto(prod3)
pedido3.agregarProducto(prod8)

pedido4 = Pedido(4)
pedido4.agregarProducto(prod4)
pedido4.agregarProducto(prod9)

pedido5 = Pedido(5)
pedido5.agregarProducto(prod5)
pedido5.agregarProducto(prod10)

pedido6 = Pedido(6)
pedido6.agregarProducto(prod1)

pedido7 = Pedido(7)
pedido7.agregarProducto(prod2)

pedido8 = Pedido(8)
pedido8.agregarProducto(prod3)

pedido9 = Pedido(9)
pedido9.agregarProducto(prod4)

pedido10 = Pedido(10)
pedido10.agregarProducto(prod5)

pedido1.calcularTotal()
pedido2.calcularTotal()
pedido3.calcularTotal()
pedido4.calcularTotal()
pedido5.calcularTotal()
pedido6.calcularTotal()
pedido7.calcularTotal()
pedido8.calcularTotal()
pedido9.calcularTotal()
pedido10.calcularTotal()

print("\n===Detalle de Pedidos===\n")

print(pedido1.mostrar_detalle())
print(pedido2.mostrar_detalle())
print(pedido3.mostrar_detalle())
print(pedido4.mostrar_detalle())
print(pedido5.mostrar_detalle())
print(pedido6.mostrar_detalle())
print(pedido7.mostrar_detalle())
print(pedido8.mostrar_detalle())
print(pedido9.mostrar_detalle())
print(pedido10.mostrar_detalle())

print("\n===Historial de Clientes===\n")

cli1.realizarPedido(pedido1)
cli2.realizarPedido(pedido2)
cli3.realizarPedido(pedido3)
cli4.realizarPedido(pedido4)
cli5.realizarPedido(pedido5)

cli1.Historial()
cli2.Historial()
cli3.Historial()
cli4.Historial()
cli5.Historial()

# ===== Menu interactivo=====
while True:

    print("\n=== Menu del sistema ===")
    print("1. Ver clientes")
    print("2. Ver empleados")
    print("3. Ver productos")
    print("4. Ver detalle de pedidos")
    print("5. Ver historial de clientes")
    print("6. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":

        print("\n=== Clientes ===\n")

        print(cli1.nombre)
        print(cli2.nombre)
        print(cli3.nombre)
        print(cli4.nombre)
        print(cli5.nombre)
        print(cli6.nombre)
        print(cli7.nombre)
        print(cli8.nombre)
        print(cli9.nombre)
        print(cli10.nombre)

    elif opcion == "2":

        print("\n===Empleados===\n")

        print(emp1.nombre)
        print(emp2.nombre)
        print(emp3.nombre)
        print(emp4.nombre)
        print(emp5.nombre)
        print(emp6.nombre)
        print(emp7.nombre)
        print(emp8.nombre)
        print(emp9.nombre)
        print(emp10.nombre)

    elif opcion == "3":

        print("\n===Productos===\n")

        print(prod1.nombre)
        print(prod2.nombre)
        print(prod3.nombre)
        print(prod4.nombre)
        print(prod5.nombre)
        print(prod6.nombre)
        print(prod7.nombre)
        print(prod8.nombre)
        print(prod9.nombre)
        print(prod10.nombre)

    elif opcion == "4":

        print("\n===Detalle de Pedidos===\n")

        print(pedido1.mostrar_detalle())
        print(pedido2.mostrar_detalle())
        print(pedido3.mostrar_detalle())
        print(pedido4.mostrar_detalle())
        print(pedido5.mostrar_detalle())
        print(pedido6.mostrar_detalle())
        print(pedido7.mostrar_detalle())
        print(pedido8.mostrar_detalle())
        print(pedido9.mostrar_detalle())
        print(pedido10.mostrar_detalle())

    elif opcion == "5":

        print("\n===Historial de Clientes===\n")

        cli1.Historial()
        cli2.Historial()
        cli3.Historial()
        cli4.Historial()
        cli5.Historial()

    elif opcion == "6":

        print("\n===== Fin del programa :3 =====")
        print("Programa ejecutado correctamente ^u^")
        break

    else:

        print("Opcion no valida")

print("\n===== Fin del programa :3 =====")
print("Programa ejecutado correctamente ^u^")