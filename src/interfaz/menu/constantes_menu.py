"""
constantes_menu.py
==================
Constantes de opciones del menú principal.
"""

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