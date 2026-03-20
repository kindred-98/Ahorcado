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
    from interfaz.pantalla import limpiar_pantalla, mostrar_mensaje, mostrar_error
"""

from interfaz.pantalla import limpiar_pantalla, mostrar_mensaje, mostrar_error


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
    Por ahora muestra un placeholder hasta que
    juego/bucle.py esté implementado.
    """
    # TODO: reemplazar con llamada a juego.bucle.iniciar_partida()
    limpiar_pantalla()
    mostrar_mensaje("⚔  Iniciando partida... (módulo juego pendiente)")
    input("  Presiona ENTER para volver al menú...")


def _accion_añadir_palabra() -> None:
    """
    Acción del menú: añadir una nueva palabra a la base de datos.
    Por ahora muestra un placeholder hasta que
    base_datos/insercion.py esté implementado.
    """
    # TODO: reemplazar con llamada a base_datos.insercion.insertar_palabra()
    limpiar_pantalla()
    mostrar_mensaje("📖  Añadir palabra... (módulo base_datos pendiente)")
    input("  Presiona ENTER para volver al menú...")


def _accion_ver_palabras() -> None:
    """
    Acción del menú: mostrar todas las palabras almacenadas.
    Por ahora muestra un placeholder hasta que
    base_datos/consultas.py esté implementado.
    """
    # TODO: reemplazar con llamada a base_datos.consultas.obtener_todas_las_palabras()
    limpiar_pantalla()
    mostrar_mensaje("📜  Ver palabras... (módulo base_datos pendiente)")
    input("  Presiona ENTER para volver al menú...")


def _accion_salir() -> None:
    """
    Acción del menú: despedirse del jugador y cerrar el programa.
    """
    limpiar_pantalla()
    print("\n  ╔══════════════════════════════════════════════╗")
    print("  ║   ⚔  Hasta la próxima, caballero...  ⚔      ║")
    print("  ╚══════════════════════════════════════════════╝\n")


# ── Funciones privadas — construcción visual ──────────────────

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