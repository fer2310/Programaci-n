# Hecho por: alumnos: Angel Daniel Hernandez Arteaga y Fernando Cruz Calderon

from dataclasses import dataclass


@dataclass(frozen=True)
class Elemento:
    numero_atomico: int
    simbolo: str
    nombre: str


ELEMENTOS = [
    (1, "H", "hidrogeno"),
    (2, "He", "helio"),
    (3, "Li", "litio"),
    (4, "Be", "berilio"),
    (5, "B", "boro"),
    (6, "C", "carbono"),
    (7, "N", "nitrogeno"),
    (8, "O", "oxigeno"),
    (9, "F", "fluor"),
    (10, "Ne", "neon"),
    (11, "Na", "sodio"),
    (12, "Mg", "magnesio"),
    (13, "Al", "aluminio"),
    (14, "Si", "silicio"),
    (15, "P", "fosforo"),
    (16, "S", "azufre"),
    (17, "Cl", "cloro"),
    (18, "Ar", "argon"),
    (19, "K", "potasio"),
    (20, "Ca", "calcio"),
    (21, "Sc", "escandio"),
    (22, "Ti", "titanio"),
    (23, "V", "vanadio"),
    (24, "Cr", "cromo"),
    (25, "Mn", "manganeso"),
    (26, "Fe", "hierro"),
    (27, "Co", "cobalto"),
    (28, "Ni", "niquel"),
    (29, "Cu", "cobre"),
    (30, "Zn", "zinc"),
    (31, "Ga", "galio"),
    (32, "Ge", "germanio"),
    (33, "As", "arsenico"),
    (34, "Se", "selenio"),
    (35, "Br", "bromo"),
    (36, "Kr", "kripton"),
    (37, "Rb", "rubidio"),
    (38, "Sr", "estroncio"),
    (39, "Y", "itrio"),
    (40, "Zr", "zirconio"),
    (41, "Nb", "niobio"),
    (42, "Mo", "molibdeno"),
    (43, "Tc", "tecnecio"),
    (44, "Ru", "rutenio"),
    (45, "Rh", "rodio"),
    (46, "Pd", "paladio"),
    (47, "Ag", "plata"),
    (48, "Cd", "cadmio"),
    (49, "In", "indio"),
    (50, "Sn", "estano"),
    (51, "Sb", "antimonio"),
    (52, "Te", "telurio"),
    (53, "I", "yodo"),
    (54, "Xe", "xenon"),
    (55, "Cs", "cesio"),
    (56, "Ba", "bario"),
    (57, "La", "lantano"),
    (58, "Ce", "cerio"),
    (59, "Pr", "praseodimio"),
    (60, "Nd", "neodimio"),
    (61, "Pm", "prometio"),
    (62, "Sm", "samario"),
    (63, "Eu", "europio"),
    (64, "Gd", "gadolinio"),
    (65, "Tb", "terbio"),
    (66, "Dy", "disprosio"),
    (67, "Ho", "holmio"),
    (68, "Er", "erbio"),
    (69, "Tm", "tulio"),
    (70, "Yb", "iterbio"),
    (71, "Lu", "lutecio"),
    (72, "Hf", "hafnio"),
    (73, "Ta", "tantalio"),
    (74, "W", "wolframio"),
    (75, "Re", "renio"),
    (76, "Os", "osmio"),
    (77, "Ir", "iridio"),
    (78, "Pt", "platino"),
    (79, "Au", "oro"),
    (80, "Hg", "mercurio"),
    (81, "Tl", "talio"),
    (82, "Pb", "plomo"),
    (83, "Bi", "bismuto"),
    (84, "Po", "polonio"),
    (85, "At", "astato"),
    (86, "Rn", "radon"),
    (87, "Fr", "francio"),
    (88, "Ra", "radio"),
    (89, "Ac", "actinio"),
    (90, "Th", "torio"),
    (91, "Pa", "protactinio"),
    (92, "U", "uranio"),
    (93, "Np", "neptunio"),
    (94, "Pu", "plutonio"),
    (95, "Am", "americio"),
    (96, "Cm", "curio"),
    (97, "Bk", "berkelio"),
    (98, "Cf", "californio"),
    (99, "Es", "einstenio"),
    (100, "Fm", "fermio"),
    (101, "Md", "mendelevio"),
    (102, "No", "nobelio"),
    (103, "Lr", "lawrencio"),
    (104, "Rf", "rutherfordio"),
    (105, "Db", "dubnio"),
    (106, "Sg", "seaborgio"),
    (107, "Bh", "bohrio"),
    (108, "Hs", "hassio"),
    (109, "Mt", "meitnerio"),
    (110, "Ds", "darmstadtio"),
    (111, "Rg", "roentgenio"),
    (112, "Cn", "copernicio"),
    (113, "Nh", "nihonio"),
    (114, "Fl", "flerovio"),
    (115, "Mc", "moscovio"),
    (116, "Lv", "livermorio"),
    (117, "Ts", "tenesino"),
    (118, "Og", "oganeson"),
]

ELEMENTOS_POR_ATOMO = {numero: Elemento(numero, simbolo, nombre) for numero, simbolo, nombre in ELEMENTOS}
ELEMENTOS_POR_SIMBOLO = {elemento.simbolo.lower(): elemento for elemento in ELEMENTOS_POR_ATOMO.values()}
ELEMENTOS_POR_NOMBRE = {elemento.nombre.lower(): elemento for elemento in ELEMENTOS_POR_ATOMO.values()}

NO_METAL = {1, 6, 7, 8, 9, 15, 16, 17, 34, 35, 53, 54, 86, 118}
METALOIDES = {5, 14, 32, 33, 51, 52, 84, 85}
GASES_NOBLES = {2, 10, 18, 36, 54, 86, 118}

GRUPO_III = {5, 13, 31, 49, 81, 113}
GRUPO_IV = {6, 14, 32, 50, 82, 114}
GRUPO_V = {7, 15, 33, 51, 83, 115}


def normalizar(texto: str) -> str:
    return texto.strip().lower()


def quitar_acentos(texto: str) -> str:
    reemplazos = str.maketrans("áéíóúüñ", "aeiouun")
    return texto.translate(reemplazos)


def resolver_elemento(texto: str):
    bruto = texto.strip()
    if not bruto:
        return None

    if bruto.isdigit():
        return ELEMENTOS_POR_ATOMO.get(int(bruto))

    clave = quitar_acentos(normalizar(bruto))
    if clave in ELEMENTOS_POR_SIMBOLO:
        return ELEMENTOS_POR_SIMBOLO[clave]
    if clave in ELEMENTOS_POR_NOMBRE:
        return ELEMENTOS_POR_NOMBRE[clave]
    return None


def es_metal(elemento: Elemento) -> bool:
    return (
        elemento.numero_atomico not in NO_METAL
        and elemento.numero_atomico not in METALOIDES
        and elemento.numero_atomico not in GASES_NOBLES
    )


def es_no_metal(elemento: Elemento) -> bool:
    return elemento.numero_atomico in NO_METAL


def es_metaloide(elemento: Elemento) -> bool:
    return elemento.numero_atomico in METALOIDES


def es_gas_noble(elemento: Elemento) -> bool:
    return elemento.numero_atomico in GASES_NOBLES


def categoria_elemento(elemento: Elemento) -> str:
    if es_gas_noble(elemento):
        return "Gas noble"
    if es_metaloide(elemento):
        return "Metaloide"
    if es_no_metal(elemento):
        return "No metal"
    return "Metal"


def grupo_semiconductor(elemento: Elemento) -> str:
    z = elemento.numero_atomico
    if z in GRUPO_III:
        return "Grupo III"
    if z in GRUPO_IV:
        return "Grupo IV"
    if z in GRUPO_V:
        return "Grupo V"
    return "-"


def tipo_material_covalente(elemento1: Elemento, elemento2: Elemento) -> str:
    a = elemento1.numero_atomico
    b = elemento2.numero_atomico

    if (a in GRUPO_III and b in GRUPO_IV) or (b in GRUPO_III and a in GRUPO_IV):
        return "Extrinseco tipo P"
    if (a in GRUPO_V and b in GRUPO_IV) or (b in GRUPO_V and a in GRUPO_IV):
        return "Extrinseco tipo N"
    return "Intrinseco"


def clasificar_enlace(elemento1: Elemento, elemento2: Elemento):
    if es_gas_noble(elemento1) or es_gas_noble(elemento2):
        return "No es posible hacer un enlace estable en este modelo escolar.", None

    metal1 = es_metal(elemento1)
    metal2 = es_metal(elemento2)
    no_metal1 = es_no_metal(elemento1)
    no_metal2 = es_no_metal(elemento2)
    metaloide1 = es_metaloide(elemento1)
    metaloide2 = es_metaloide(elemento2)

    if metal1 and metal2:
        return "Metalico", None

    if (metal1 and no_metal2) or (metal2 and no_metal1):
        return "Ionico", None

    if (no_metal1 or metaloide1) and (no_metal2 or metaloide2):
        return "Covalente", tipo_material_covalente(elemento1, elemento2)

    if (metal1 and metaloide2) or (metal2 and metaloide1):
        return "Covalente", tipo_material_covalente(elemento1, elemento2)

    return "No es posible determinar un enlace simple con este par.", None
