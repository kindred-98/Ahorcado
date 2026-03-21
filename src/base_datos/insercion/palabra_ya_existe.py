"""
palabra_ya_existe.py
====================
Función para comprobar si una palabra ya existe en la base de datos.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion import obtener_conexion


def palabra_ya_existe(palabra: str) -> bool:
    """
    Comprueba si una palabra ya existe en la base de datos.

    Args:
        palabra (str): La palabra a buscar (sin distinguir mayúsculas).

    Returns:
        bool: True si ya existe. False si no existe o hay error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT 1 FROM palabras
                WHERE palabra = ?
                LIMIT 1
            """, (palabra.lower().strip(),))
            return cursor.fetchone() is not None

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo verificar la palabra: {error_bd}")
        return False