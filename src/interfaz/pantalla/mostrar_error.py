"""
mostrar_error.py
================
Función para mostrar mensajes de error en pantalla.
"""


def mostrar_error(mensaje_error: str) -> None:
    """
    Imprime un mensaje de error con símbolo de advertencia.

    Args:
        mensaje_error (str): Descripción del error ocurrido.
    """
    print(f"\n  ⚠  {mensaje_error}\n")