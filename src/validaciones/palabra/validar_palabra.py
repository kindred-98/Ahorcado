"""
validar_palabra.py
==================
Función pública para validar una nueva palabra antes de insertarla.
"""

from src.validaciones.palabra.constantes             import LONGITUD_MINIMA_PALABRA, LONGITUD_MAXIMA_PALABRA
from src.validaciones.palabra.buscar_caracter_invalido import _buscar_caracter_invalido


def validar_palabra(palabra: str) -> str | None:
    """
    Valida que una palabra sea apta para la base de datos.

    Args:
        palabra (str): Palabra a validar.

    Returns:
        str | None: Mensaje de error o None si es válida.
    """
    palabra_normalizada = palabra.strip().lower()

    if not palabra_normalizada:
        return "La palabra no puede estar vacía."

    if len(palabra_normalizada) < LONGITUD_MINIMA_PALABRA:
        return f"La palabra debe tener al menos {LONGITUD_MINIMA_PALABRA} letras."

    if len(palabra_normalizada) > LONGITUD_MAXIMA_PALABRA:
        return f"La palabra no puede tener más de {LONGITUD_MAXIMA_PALABRA} letras."

    caracter_invalido = _buscar_caracter_invalido(palabra_normalizada)
    if caracter_invalido:
        return f"La palabra solo puede contener letras. Carácter no válido: '{caracter_invalido}'."

    return None