"""
mostrar_menu_principal.py
=========================
Función para limpiar pantalla y mostrar el menú principal.
"""

from src.interfaz.pantalla.limpiar_pantalla import limpiar_pantalla
from src.interfaz.menu.construir_menu       import _construir_menu


def mostrar_menu_principal() -> None:
    """
    Limpia la pantalla y muestra las opciones del menú principal.
    """
    limpiar_pantalla()
    print(_construir_menu())