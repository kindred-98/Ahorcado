"""
validar_categoria.py
====================
Función pública para validar la categoría de una palabra.
"""

from src.validaciones.palabra.constantes import CATEGORIAS_VALIDAS


def validar_categoria(categoria: str) -> str | None:
    """
    Valida que la categoría sea una de las permitidas.

    Args:
        categoria (str): Categoría a validar.

    Returns:
        str | None: Mensaje de error o None si es válida.
    """
    categoria_normalizada = categoria.strip().lower()

    if not categoria_normalizada:
        return "La categoría no puede estar vacía."

    if categoria_normalizada not in CATEGORIAS_VALIDAS:
        opciones = ", ".join(sorted(CATEGORIAS_VALIDAS))
        return f"Categoría no válida. Elige entre: {opciones}."

    return None