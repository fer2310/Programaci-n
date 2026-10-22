class SistemaNumeracion:

# Metodo para validar y convertir un numero de una base.
    def pedir_numero(self, mensaje, digitos, base):
        while True:
            numero = input(mensaje).strip().upper()

            if numero != "" and all(
                letra in digitos for letra in numero
            ):
                return int(numero, base)
            else:  
                print("\nError no leiste el ejemplo? ese numero no es valido para la base")

# Metodo para validar la opcion del menu.
    def pedir_opcion(self):
        while True:
            opcion = input("Elige una opcion del 1 al 9 pliis :D : ").strip()

            if opcion.isdigit() and 1 <= int(opcion) <= 9:
                return int(opcion)
            else:
                print("Error te dije elige un numero del 1 al 9 D:< ")

# Opcion 1: binario a octal.
    def binario_a_octal(self):
        numero = self.pedir_numero(
            "=== Conversion de Bina a Octa ==="
            "\nejemlo: 01101101"
            "\nPor favor escribe el numero binario:", "01", 2
        )
        print("Binario:", format(numero, "b"))
        print("Octal:", format(numero, "o"))

# Opcion 2: binario a hexadecimal.
    def binario_a_hexadecimal(self):
        numero = self.pedir_numero(
            "===== Binario a Hexa ====="
            "\nEJEMPLITO: 10010101"
            "\nEscribe el numero binario como en el ejemplo: ", "01", 2
        )
        print("Binario:", format(numero, "b"))
        print("Hexadecimal:", format(numero, "X"))

# Opcion 3: octal a hexadecimal.
    def octal_a_hexadecimal(self):
        numero = self.pedir_numero(
            "==== De Octal a Hexadecimal ===="
            "\nHi aqui si puedes poner cualquier numero del 0 al 7"
            "\nEscribe el numero octal: ", "01234567", 8
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

            if numero.isdigit() and 1 <= int(numero) <= 127:
                numero = int(numero)
                break
            else:
                print("\nError compañer@ dije del 1 al 127 intenta de nuevo :D ")

        binario = format(numero, "08b")

        complemento1 = ""
        for bit in binario:
            if bit == "0":
                complemento1 += "1"
            else:
                complemento1 += "0"

        valor_complemento1 = int(complemento1, 2)
        complemento2 = format(valor_complemento1 + 1, "08b")

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

        for letra in letras:
            decimal = ord(letra)
            binario = format(decimal, "08b")

            print("Letra:", letra)
            print("ASCII decimal:", decimal)
            print("ASCII binario:", binario)

# Metodo del menu principal
    def menu(self):
        while True:
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

            opcion = self.pedir_opcion()

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

sistema = SistemaNumeracion()
sistema.menu()
