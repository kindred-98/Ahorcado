"""
poblar_palabras_iniciales.py
============================
Función privada para insertar las palabras iniciales en la BD.
"""

import sqlite3

from src.base_datos.inicializar.palabras_iniciales import PALABRAS_INICIALES


def _poblar_palabras_iniciales(cursor: sqlite3.Cursor) -> None:
    """
    Inserta las palabras de PALABRAS_INICIALES con INSERT OR IGNORE
    para no duplicar registros existentes.

    Args:
        cursor (sqlite3.Cursor): Cursor activo de la conexión.
    """
    cursor.executemany("""
        INSERT OR IGNORE INTO palabras (palabra, categoria, dificultad)
        VALUES (?, ?, ?)
    """, PALABRAS_INICIALES)