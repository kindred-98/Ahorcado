"""
obtener_categorias.py
=====================
Función para obtener las categorías disponibles en la BD.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion import obtener_conexion


def obtener_categorias() -> list[dict]:
    """
    Devuelve las categorías únicas con el conteo de palabras
    de cada una, ordenadas alfabéticamente.

    Returns:
        list[dict]: Lista de dicts con claves 'categoria' y 'total'.
                    Lista vacía si no hay registros o hay error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT categoria, COUNT(*) AS total
                FROM palabras
                GROUP BY categoria
                ORDER BY categoria
            """)
            return [dict(fila) for fila in cursor.fetchall()]

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudieron obtener las categorías: {error_bd}")
        return []