"""
validar_letra.py
================
Función pública para validar la letra ingresada por el jugador.
"""

from src.validaciones.letra.alfabeto import ALFABETO_ESPAÑOL


def validar_letra(entrada: str) -> str | None:
    """
    Valida que la entrada del jugador sea una sola letra
    del alfabeto español.

    Args:
        entrada (str): Texto ingresado por el jugador.

    Returns:
        str | None: Mensaje de error o None si es válida.
    """
    if not entrada:
        return "Debes ingresar una letra."

    if len(entrada) > 1:
        return "Ingresa solo una letra, no varias."

    if entrada.lower() not in ALFABETO_ESPAÑOL:
        return f"El carácter '{entrada}' no es una letra válida."

    return None