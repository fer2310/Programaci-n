class SistemaNumeracion:

# Metodo para validar y convertir un numero de una base.
    def pedir_numero(self, mensaje, digitos, base):  #metotodo para mostrar mensaje. q caracter ta permitido u q base esta
        while True: #bucle infinito
            numero = input(mensaje).strip().upper() # Muestra el mensaje .strip() y quita los espacios en blanco y .upper convierte a mayusculas 

            if numero != "" and all(
                letra in digitos for letra in numero
            ): #valida dos cosas q no este vacio y q todos los caracteres esten en la lista de digitos permitidos
                return int(numero, base) #si es valido convierte el numero a entero en la base especificada y lo retorna
            else:  
                print("\nError no leiste el ejemplo? ese numero no es valido para la base") # Muestra un mensaje de error si el numero no es valido

# Metodo para validar la opcion del menu.
    def pedir_opcion(self):
        while True:
            opcion = input("Elige una opcion del 1 al 9 pliis :D : ").strip() #muestra mensaje y quita espacios en blanco

            if opcion.isdigit() and 1 <= int(opcion) <= 9: #valida que la opcion sea un numero del 1 al 9
                return int(opcion) #si es valido convierte la opcion a entero y la retorna
            else:
                print("Error te dije elige un numero del 1 al 9 D:< ")

# Opcion 1: binario a octal.
    def binario_a_octal(self):
        numero = self.pedir_numero(
            "=== Conversion de Bina a Octa ==="
            "\nejemlo: 01101101"
            "\nPor favor escribe el numero binario:", "01", 2
        ) # llama al metodo pedir_numero para obtener el numero binario
        print("Binario:", format(numero, "b")) # muestra el numero binario en formato binario
        print("Octal:", format(numero, "o"))# muestra el numero en formato octal                

# Todo desde la linea 26 hasta la 33 oython usa la funcion return int(numero, base) ya q ocupa la  funcion int con base 2 para traducirlo y guardarlo en la memoria como un numero entero y corriente
# Una vez q ya esta guardado en la memoria como un numero entero y corriente se puede usar la funcion format para mostrarlo en cualquier base q se quiera, en este caso binario y octal

# Opcion 2: binario a hexadecimal.
    def binario_a_hexadecimal(self):
        numero = self.pedir_numero(
            "===== Binario a Hexa ====="
            "\nEJEMPLITO: 10010101"
            "\nEscribe el numero binario como en el ejemplo: ", "01", 2
        )
        print("Binario:", format(numero, "b")) #el format(numero, "b") convierte el numero a binario y lo muestra en pantalla
        print("Hexadecimal:", format(numero, "X")) #el format(numero, "X") toma el mismo numero entero have internamente divisiones y saca el resultado en hexadecimal y lo muestra en pantalla 

#format se ocupa gracias a la documentacion oficial de python y es la forma mas facil de mostrar un numero en cualquier base sin tener q hacer conversiones manuales y se ocupa de la siguiente manera: format(numero, "b") para binario, format(numero, "o") para octal y format(numero, "X") para hexadecimal
#ya q la chompu no muestra las cosas en binario u octal por iniciativa propia 

# Opcion 3: octal a hexadecimal.
    def octal_a_hexadecimal(self):
        numero = self.pedir_numero(
            "==== De Octal a Hexadecimal ===="
            "\nHi aqui si puedes poner cualquier numero del 0 al 7"
            "\nEscribe el numero octal: ", "01234567", 8 #el 8 es la base octal y los digitos permitidos son del 0 al 7 , si no las cambia la base solo nos da un resultado erroneo
        )
        print("Octal:", format(numero, "o"))
        print("Hexadecimal:", format(numero, "X"))

# Opcion 4: hexadecimal a octal.
    def hexadecimal_a_octal(self):
        numero = self.pedir_numero(
            "==== Hexadecimal a Octal"
            "\nAqui puedes ocupar del 0 al 9 y despues son A=10 , B= 11, C=12 , D=13, E=14, F=15 pero en mayusculas"
            "\nEscribe un numero hexadecimal: ",
            "0123456789ABCDEF", 16
        )
        print("Hexadecimal:", format(numero, "X"))
        print("Octal:", format(numero, "o"))

# Opcion 5: sumar dos numeros binarios.
    def sumar_binarios(self):
        primero = self.pedir_numero(
            "==== Sumaa de binarios ===="
            "\nPor favor todo en binario"
            "\nEjemplo: 10100110"
            "\nPrimer numero binario plis: ", "01", 2
        )
        segundo = self.pedir_numero(
            "Segundo numero binario: ", "01", 2
        )

        resultado = primero + segundo
        print("Resultado binario:", format(resultado, "b"))

# Opcion 6: restar dos numeros binarios.
    def restar_binarios(self):
        while True:
            primero = self.pedir_numero(
               " === Resta binario ==="
                "\nEl mismo ejemplo solo numeros del 0 a 1 "
                "\nPrimer numero binario: ", "01", 2
            )
            segundo = self.pedir_numero(
                "Segundo numero binario: ", "01", 2
            )

            if primero >= segundo:
                break
            else:
                print("Se me olvido decirte jejeje el primer numero debe ser mayor"
                      "\no igual que el segundo. Intenta de nuevo otra vez y perdon :p ")

        resultado = primero - segundo
        print("Resultado binario:", format(resultado, "08b"))

# Opcion 7: complemento a 1 y a 2.
    def complementos(self):
        while True:
            numero = input(
                "==== Complemento 1 y 2 ===="
                "\nPor favor ingresa un numero desde el 1 al 127 plis"
                "\nNumero decimal entre 1 y 127: "
            ).strip()

            if numero.isdigit() and 1 <= int(numero) <= 127: # valida q el numero sea un digito y q este entre 1 y 127
                numero = int(numero) 
                break
            else:
                print("\nError compañer@ dije del 1 al 127 intenta de nuevo :D ")

        binario = format(numero, "08b") # convierte el numero a binario de 8 bits y lo guarda en la variable binario

        complemento1 = ""
        for bit in binario: # calcula el complemento a 1 invirtiendo los bits del numero binario
            if bit == "0": # si el bit es 0 lo cambia a 1 y si es 1 lo cambia a 0
                complemento1 += "1"
            else:
                complemento1 += "0"

        valor_complemento1 = int(complemento1, 2) # convierte el complemento a 1 a decimal para calcular el complemento a 2
        complemento2 = format(valor_complemento1 + 1, "08b") # calcula el complemento a 2 sumando 1 al valor decimal del complemento a 1 y lo convierte a binario de 8 bits

        print("Decimal:", numero)
        print("Binario de 8 bits:", binario)
        print("Complemento a 1:", complemento1)
        print("Complemento a 2:", complemento2)

# Opcion 8: letras mayusculas a codigo ASCII.
    def consultar_ascii(self):
        while True:
            letras = input(
                "===== Codigo ASCII ====="
                "\nHola aqui puedes desde una palbara sin espacios hasta una letra en mayusculas por fa"
                "\nEscribe letras mayusculas de la A a la Z: "
            )

            if letras != "" and all(
                "A" <= letra <= "Z" for letra in letras
            ):
                break
            else:
                print("\nError compañer@ utiliza solamente letras de la A a la Z Thanks ")

        for letra in letras: # funciona como un puntero imaginario q recorre cada letra ingresada por el usuario y obtiene su valor decimal y binario en codigo ASCII
            decimal = ord(letra) # obtiene el valor a decimal de la letra usando la funcion ord() y lo guarda en la variable decimal
            binario = format(decimal, "08b") # lo llama a traer y lo convierte el valor decimal a binario de 8 bits usando la funcion format() y lo guarda en la variable binario

            print("Letra:", letra)
            print("ASCII decimal:", decimal)
            print("ASCII binario:", binario)

# Metodo del menu principal
    def menu(self):# metodo para mostrar el menu principal
        while True: # }bucle infinito para mostrar el menu hasta que el usuario decida salir
            print("\n===== SISTEMA DE NUMERACION =====")
            print("1. Binario a octal")
            print("2. Binario a hexadecimal")
            print("3. Octal a hexadecimal")
            print("4. Hexadecimal a octal")
            print("5. Sumar numeros binarios")
            print("6. Restar numeros binarios")
            print("7. Complemento a 1 y a 2")
            print("8. Letras mayusculas a ASCII")
            print("9. Salir")

            opcion = self.pedir_opcion() # llama al metodo pedir_opcion para obtener la opcion del usuario
#utiliza estructura if-elif para llamar al metodo correspondiente segun la opcion elegida por el usuario
            if opcion == 1:
                self.binario_a_octal()
            elif opcion == 2:
                self.binario_a_hexadecimal()
            elif opcion == 3:
                self.octal_a_hexadecimal()
            elif opcion == 4:
                self.hexadecimal_a_octal()
            elif opcion == 5:
                self.sumar_binarios()
            elif opcion == 6:
                self.restar_binarios()
            elif opcion == 7:
                self.complementos()
            elif opcion == 8:
                self.consultar_ascii()
            elif opcion == 9:
                print("Si ves esto son las 3 de la madrugada y el programa sigue sin funcionar, espera asi no era"
                "\nGracias por ver y jugar con el programa, ante cualquier duda la mas.... con el profe , adio")
                break

sistema = SistemaNumeracion() # crea una instancia de la clase SistemaNumeracion y la guarda en la variable sistema
sistema.menu() # llama al metodo menu() de la instancia sistema para iniciar el programa y mostrar el menu principal

#Profesor (con los brazos cruzados): "A ver, equipo... Veo que estructuraron todo su código dentro de una clase (class SistemaNumeracion:) y al final crean un objeto para llamarlo (sistema = SistemaNumeracion()). ¿Por qué no hicieron funciones sueltas y qué ventaja real les da usar Programación Orientada a Objetos (POO) aquí?"
#"Profesor, decidimos usar una clase para encapsular todo el comportamiento del sistema de numeración en un solo módulo ordenado. Esto nos permite mantener limpias las variables (como los métodos de validación) y usar el self para que cualquier método pueda compartir y reutilizar el motor de validación pedir_numero sin andar declarando variables globales por todo el archivo."
