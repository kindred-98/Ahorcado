"""
construir_consulta_aleatoria.py
================================
Función privada para construir la consulta SQL dinámica
con filtros opcionales de categoría y dificultad.
"""

from typing import Optional


def _construir_consulta_aleatoria(
    categoria:  Optional[str],
    dificultad: Optional[str],
) -> tuple[str, list]:
    """
    Construye dinámicamente la consulta SQL para obtener
    una palabra aleatoria según los filtros recibidos.

    Args:
        categoria  (str | None): Filtro de categoría.
        dificultad (str | None): Filtro de dificultad.

    Returns:
        tuple[str, list]: La consulta SQL y sus parámetros.
    """
    consulta    = "SELECT id, palabra, categoria, dificultad FROM palabras WHERE 1=1"
    parametros: list = []

    if categoria:
        consulta += " AND categoria = ?"
        parametros.append(categoria.lower())

    if dificultad:
        consulta += " AND dificultad = ?"
        parametros.append(dificultad.lower())

    consulta += " ORDER BY RANDOM() LIMIT 1"

    return consulta, parametros