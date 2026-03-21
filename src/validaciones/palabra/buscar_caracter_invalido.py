"""
buscar_caracter_invalido.py
===========================
Función privada para detectar caracteres inválidos en una palabra.
"""

from src.validaciones.palabra.constantes import CARACTERES_VALIDOS_PALABRA


def _buscar_caracter_invalido(palabra: str) -> str | None:
    """
    Recorre la palabra y devuelve el primer carácter inválido.

    Args:
        palabra (str): Palabra ya normalizada a minúsculas.

    Returns:
        str | None: Primer carácter inválido o None si todos son válidos.
    """
    for caracter in palabra:
        if caracter not in CARACTERES_VALIDOS_PALABRA:
            return caracter
    return None