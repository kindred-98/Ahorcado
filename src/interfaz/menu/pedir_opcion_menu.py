"""
pedir_opcion_menu.py
====================
Función para capturar y validar la opción del menú.
"""

from src.interfaz.menu.constantes_menu   import OPCIONES_VALIDAS
from src.interfaz.pantalla.mostrar_error import mostrar_error


def pedir_opcion_menu() -> str:
    """
    Solicita al jugador que elija una opción del menú.
    Repite la solicitud hasta recibir una entrada válida.

    Returns:
        str: Opción elegida ("1", "2", "3" o "4").
    """
    while True:
        opcion = input("  Tu elección > ").strip()

        if opcion in OPCIONES_VALIDAS:
            return opcion

        mostrar_error("Opción no válida. Elige entre 1 y 3.")