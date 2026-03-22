"""
accion_salir.py
===============
Acción del menú: despedirse del jugador y cerrar el programa.
"""

from src.interfaz.pantalla.limpiar_pantalla import limpiar_pantalla


def _accion_salir() -> None:
    """
    Limpia la pantalla y muestra el mensaje de despedida.
    """
    limpiar_pantalla()
    print("\n╔══════════════════════════════════════════════╗")
    print("  ║   ⚔  Hasta la próxima, gran jugador...  ⚔    ║")
    print("  ╚══════════════════════════════════════════════╝\n")