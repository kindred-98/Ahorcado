"""
construir_menu.py
=================
Función privada para construir el bloque visual del menú.
"""


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