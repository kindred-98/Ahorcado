"""
pedir_campo_validado.py
=======================
Función privada para pedir un campo con validación en bucle.
"""

from src.interfaz.pantalla.mostrar_error import mostrar_error


def _pedir_campo_validado(etiqueta: str, validador) -> str:
    """
    Solicita un campo al jugador en bucle hasta recibir
    un valor que pase la validación.

    Args:
        etiqueta  (str):      Texto descriptivo del campo.
        validador (callable): Función que devuelve str con error
                              o None si es válido.

    Returns:
        str: Valor ingresado normalizado a minúsculas.
    """
    while True:
        valor = input(f"  {etiqueta} > ").strip().lower()
        error = validador(valor)
        if error is None:
            return valor
        mostrar_error(error)