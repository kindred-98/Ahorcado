"""
menu.py
=======
Módulo que gestiona el menú principal del Ahorcado Medieval.

Responsabilidades:
    - Mostrar las opciones disponibles al jugador.
    - Capturar y validar la elección del usuario.
    - Dirigir el flujo hacia jugar, añadir palabra,
      ver palabras o salir.

Importaciones necesarias:
    from src.interfaz.menu import ejecutar_menu_principal
"""

from src.interfaz.pantalla     import limpiar_pantalla, mostrar_mensaje, mostrar_error
from src.juego.bucle            import iniciar_partida
from src.base_datos.consultas   import obtener_todas_las_palabras, obtener_categorias
from src.base_datos.insercion   import insertar_palabra, palabra_ya_existe
from src.validaciones.palabra   import validar_palabra, validar_categoria, validar_dificultad


# ── Constantes de opciones ────────────────────────────────────

OPCION_JUGAR:          str = "1"
OPCION_AÑADIR_PALABRA: str = "2"
OPCION_VER_PALABRAS:   str = "3"
OPCION_SALIR:          str = "4"

OPCIONES_VALIDAS: tuple[str, ...] = (
    OPCION_JUGAR,
    OPCION_AÑADIR_PALABRA,
    OPCION_VER_PALABRAS,
    OPCION_SALIR,
)


# ── Funciones públicas ────────────────────────────────────────

def mostrar_menu_principal() -> None:
    """
    Limpia la pantalla y muestra las opciones del menú principal
    con formato medieval.
    """
    limpiar_pantalla()
    print(_construir_menu())


def pedir_opcion_menu() -> str:
    """
    Solicita al jugador que elija una opción del menú principal.
    Repite la solicitud hasta recibir una entrada válida.

    Returns:
        str: Opción elegida por el jugador ("1", "2", "3" o "4").
    """
    while True:
        opcion = input("  Tu elección > ").strip()

        if opcion in OPCIONES_VALIDAS:
            return opcion

        mostrar_error("Opción no válida. Elige entre 1 y 4.")


def ejecutar_menu_principal() -> None:
    """
    Bucle principal del menú. Muestra las opciones, recoge
    la elección y ejecuta la acción correspondiente.

    El bucle continúa hasta que el jugador elige salir.
    """
    while True:
        mostrar_menu_principal()
        opcion = pedir_opcion_menu()

        if opcion == OPCION_JUGAR:
            _accion_jugar()

        elif opcion == OPCION_AÑADIR_PALABRA:
            _accion_añadir_palabra()

        elif opcion == OPCION_VER_PALABRAS:
            _accion_ver_palabras()

        elif opcion == OPCION_SALIR:
            _accion_salir()
            break


# ── Funciones privadas — acciones ─────────────────────────────

def _accion_jugar() -> None:
    """
    Acción del menú: iniciar una partida.

    Muestra las categorías disponibles y permite al jugador
    elegir una o jugar con cualquier palabra.
    """
    limpiar_pantalla()
    categoria_elegida = _pedir_categoria_opcional()
    iniciar_partida(categoria=categoria_elegida)


def _accion_añadir_palabra() -> None:
    """
    Acción del menú: añadir una nueva palabra a la base de datos.

    Solicita palabra, categoría y dificultad al jugador,
    valida cada campo y confirma si fue insertada correctamente.
    """
    limpiar_pantalla()
    print("\n  ╔══════════════════════════════════════════════╗")
    print("  ║       📖  AÑADIR NUEVA PALABRA               ║")
    print("  ╚══════════════════════════════════════════════╝\n")

    nueva_palabra = _pedir_campo_validado(
        etiqueta  = "Palabra",
        validador = validar_palabra,
    )

    nueva_categoria = _pedir_campo_validado(
        etiqueta  = "Categoría (animales / armas / lugares / personajes)",
        validador = validar_categoria,
    )

    nueva_dificultad = _pedir_campo_validado(
        etiqueta  = "Dificultad (facil / medio / dificil)",
        validador = validar_dificultad,
    )

    if palabra_ya_existe(nueva_palabra):
        mostrar_error(f"La palabra '{nueva_palabra}' ya existe en la base de datos.")
    else:
        fue_insertada = insertar_palabra(nueva_palabra, nueva_categoria, nueva_dificultad)
        if fue_insertada:
            mostrar_mensaje(f"✅  Palabra '{nueva_palabra.upper()}' añadida correctamente.")
        else:
            mostrar_error("No se pudo añadir la palabra. Inténtalo de nuevo.")

    input("\n  Presiona ENTER para volver al menú...")


def _accion_ver_palabras() -> None:
    """
    Acción del menú: mostrar todas las palabras almacenadas
    agrupadas por categoría con su dificultad.
    """
    limpiar_pantalla()
    print("\n  ╔══════════════════════════════════════════════╗")
    print("  ║       📜  PALABRAS EN LA BASE DE DATOS       ║")
    print("  ╚══════════════════════════════════════════════╝\n")

    lista_palabras = obtener_todas_las_palabras()

    if not lista_palabras:
        mostrar_error("No hay palabras en la base de datos.")
    else:
        categoria_actual = ""
        for registro in lista_palabras:
            if registro["categoria"] != categoria_actual:
                categoria_actual = registro["categoria"]
                print(f"\n  ── {categoria_actual.upper()} ──")
            print(
                f"     {registro['palabra']:<20} "
                f"{registro['dificultad']}"
            )
        print(f"\n  Total: {len(lista_palabras)} palabras\n")

    input("  Presiona ENTER para volver al menú...")


def _accion_salir() -> None:
    """
    Acción del menú: despedirse del jugador y cerrar el programa.
    """
    limpiar_pantalla()
    print("\n  ╔══════════════════════════════════════════════╗")
    print("  ║   ⚔  Hasta la próxima, caballero...  ⚔      ║")
    print("  ╚══════════════════════════════════════════════╝\n")


# ── Funciones privadas — helpers ──────────────────────────────

def _pedir_categoria_opcional() -> str | None:
    """
    Muestra las categorías disponibles y permite al jugador
    elegir una o jugar con todas.

    Returns:
        str | None: Nombre de la categoría elegida o None
                    si el jugador prefiere cualquier categoría.
    """
    categorias = obtener_categorias()

    if not categorias:
        return None

    print("\n  ── Categorías disponibles ──\n")
    print("  0)  Cualquier categoría")
    for indice, registro in enumerate(categorias, start=1):
        print(
            f"  {indice})  {registro['categoria'].capitalize()}"
            f"  ({registro['total']} palabras)"
        )

    opciones_validas = ["0"] + [str(i) for i in range(1, len(categorias) + 1)]

    while True:
        eleccion = input("\n  Elige una categoría > ").strip()
        if eleccion in opciones_validas:
            break
        mostrar_error(f"Elige un número entre 0 y {len(categorias)}.")

    if eleccion == "0":
        return None

    return categorias[int(eleccion) - 1]["categoria"]


def _pedir_campo_validado(etiqueta: str, validador) -> str:
    """
    Solicita un campo al jugador en bucle hasta recibir
    un valor que pase la validación.

    Args:
        etiqueta  (str):      Texto descriptivo del campo a pedir.
        validador (callable): Función de validación que devuelve
                              str con el error o None si es válido.

    Returns:
        str: Valor ingresado normalizado a minúsculas.
    """
    while True:
        valor = input(f"  {etiqueta} > ").strip().lower()
        error = validador(valor)
        if error is None:
            return valor
        mostrar_error(error)


# ── Función privada — construcción visual ─────────────────────

def _construir_menu() -> str:
    """
    Construye el bloque visual del menú principal.

    Returns:
        str: Texto completo del menú listo para imprimir.
    """
    return (
        "\n"
        "  ╔══════════════════════════════════════════════╗\n"
        "  ║       ⚔   EL AHORCADO MEDIEVAL   ⚔          ║\n"
        "  ╠══════════════════════════════════════════════╣\n"
        "  ║                                              ║\n"
        "  ║   1)  ⚔  Jugar                              ║\n"
        "  ║   2)  📖  Añadir palabra                    ║\n"
        "  ║   3)  📜  Ver palabras                      ║\n"
        "  ║   4)  🚪  Salir                             ║\n"
        "  ║                                              ║\n"
        "  ╚══════════════════════════════════════════════╝\n"
    )