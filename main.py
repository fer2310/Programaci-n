import flet as ft
from enlaces import (
    categoria_elemento,
    clasificar_enlace,
    grupo_semiconductor,
    resolver_elemento,
)


def main(page: ft.Page):
    page.title = "Enlaces Químicos"
    page.padding = 20

    elem1 = ft.TextField(
        label="Primer elemento (símbolo, nombre o Z)",
        hint_text="Ej: Na, sodio o 11",
    )
    elem2 = ft.TextField(
        label="Segundo elemento (símbolo, nombre o Z)",
        hint_text="Ej: Cl, cloro o 17",
    )
    resultado = ft.Text(value="", size=16)
    detalle = ft.Text(value="", size=14)

    def calcular(e):
        e1 = resolver_elemento(elem1.value or "")
        e2 = resolver_elemento(elem2.value or "")

        if not e1 or not e2:
            resultado.value = "Revisa los elementos ingresados (Z del 1 al 118, símbolo o nombre)."
            detalle.value = ""
        else:
            enlace, material = clasificar_enlace(e1, e2)
            extra = f" | Material: {material}" if material else ""
            resultado.value = f"Enlace: {enlace}{extra}"
            detalle.value = (
                f"1) {e1.nombre.title()} ({e1.simbolo}, Z={e1.numero_atomico}) - "
                f"{categoria_elemento(e1)} [{grupo_semiconductor(e1)}]\n"
                f"2) {e2.nombre.title()} ({e2.simbolo}, Z={e2.numero_atomico}) - "
                f"{categoria_elemento(e2)} [{grupo_semiconductor(e2)}]"
            )

        page.update()

    boton = ft.ElevatedButton("Clasificar enlace", on_click=calcular)

    page.add(elem1, elem2, boton, resultado, detalle)


ft.app(target=main)
