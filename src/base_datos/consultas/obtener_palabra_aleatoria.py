"""
obtener_palabra_aleatoria.py
============================
Función para obtener una palabra aleatoria de la base de datos.
"""

import sqlite3
from typing import Optional

from src.base_datos.conexion.obtener_conexion                    import obtener_conexion
from src.base_datos.consultas.construir_consulta_aleatoria       import _construir_consulta_aleatoria


def obtener_palabra_aleatoria(
    categoria:  Optional[str] = None,
    dificultad: Optional[str] = None,
) -> Optional[dict]:
    """
    Devuelve una palabra aleatoria con filtros opcionales.

    Args:
        categoria  (str | None): Filtra por categoría.
        dificultad (str | None): Filtra por dificultad.

    Returns:
        dict | None: Diccionario con la palabra o None si no hay resultados.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            consulta, parametros = _construir_consulta_aleatoria(categoria, dificultad)
            cursor.execute(consulta, parametros)
            fila = cursor.fetchone()
            return dict(fila) if fila else None

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo obtener una palabra aleatoria: {error_bd}")
        return None