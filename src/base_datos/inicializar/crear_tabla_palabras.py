"""
crear_tabla_palabras.py
=======================
Función privada para crear la tabla palabras si no existe.
"""

import sqlite3


def _crear_tabla_palabras(cursor: sqlite3.Cursor) -> None:
    """
    Ejecuta el CREATE TABLE IF NOT EXISTS para la tabla palabras.

    Args:
        cursor (sqlite3.Cursor): Cursor activo de la conexión.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS palabras (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra    TEXT    NOT NULL UNIQUE,
            categoria  TEXT    NOT NULL,
            dificultad TEXT    NOT NULL
        )
    """)
    