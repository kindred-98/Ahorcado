"""
ejecutar_menu_principal.py
==========================
Función pública — bucle principal del menú.
"""

from src.interfaz.menu.constantes_menu           import (
    OPCION_JUGAR,
    OPCION_GESTIONAR_PALABRAS,
    OPCION_SALIR,
)
from src.interfaz.menu.mostrar_menu_principal    import mostrar_menu_principal
from src.interfaz.menu.pedir_opcion_menu         import pedir_opcion_menu
from src.interfaz.menu.accion_jugar              import _accion_jugar
from src.interfaz.menu.accion_gestionar_palabras import _accion_gestionar_palabras
from src.interfaz.menu.accion_salir              import _accion_salir


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

        elif opcion == OPCION_GESTIONAR_PALABRAS:
            _accion_gestionar_palabras()

        elif opcion == OPCION_SALIR:
            _accion_salir()
            break