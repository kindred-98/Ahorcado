"""
obtener_todas_las_palabras.py
=============================
Función para obtener todas las palabras de la base de datos.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion import obtener_conexion


def obtener_todas_las_palabras() -> list[dict]:
    """
    Devuelve todas las palabras ordenadas por categoría y palabra.

    Returns:
        list[dict]: Lista de diccionarios con cada palabra.
                    Lista vacía si no hay registros o hay error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id, palabra, categoria, dificultad
                FROM palabras
                ORDER BY categoria, palabra
            """)
            return [dict(fila) for fila in cursor.fetchall()]

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudieron obtener las palabras: {error_bd}")
        return []