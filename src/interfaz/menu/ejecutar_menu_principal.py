"""
ejecutar_menu_principal.py
==========================
Función pública — bucle principal del menú.
"""

from src.interfaz.menu.constantes_menu          import (
    OPCION_JUGAR,
    OPCION_AÑADIR_PALABRA,
    OPCION_VER_PALABRAS,
    OPCION_SALIR,
)
from src.interfaz.menu.mostrar_menu_principal   import mostrar_menu_principal
from src.interfaz.menu.pedir_opcion_menu        import pedir_opcion_menu
from src.interfaz.menu.accion_jugar             import _accion_jugar
from src.interfaz.menu.accion_añadir_palabra    import _accion_añadir_palabra
from src.interfaz.menu.accion_ver_palabras      import _accion_ver_palabras
from src.interfaz.menu.accion_salir             import _accion_salir


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