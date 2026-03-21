"""
limpiar_pantalla.py
===================
Función para limpiar la terminal.
"""

import os


def limpiar_pantalla() -> None:
    """
    Limpia la terminal de forma compatible con Windows y Unix.
    """
    os.system("cls" if os.name == "nt" else "clear")