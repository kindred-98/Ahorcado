"""
normalizar_caracter.py
======================
Función privada para eliminar tildes de un carácter.
"""

import unicodedata


def _normalizar_caracter(caracter: str) -> str:
    """
    Elimina la tilde de un carácter y lo devuelve en minúscula.

    Args:
        caracter (str): Carácter a normalizar.

    Returns:
        str: Carácter sin tilde en minúscula.
    """
    return (
        unicodedata.normalize("NFD", caracter)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .lower()
    )