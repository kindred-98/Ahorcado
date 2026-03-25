"""
eliminar_palabra.py
===================
Función para eliminar una palabra de la base de datos.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion import obtener_conexion


def eliminar_palabra(palabra: str) -> bool:
    """
    Elimina una palabra de la base de datos.

    Args:
        palabra (str): Palabra a eliminar.

    Returns:
        bool: True si fue eliminada. False si no existía o hubo error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM palabras WHERE palabra = ?",
                (palabra.lower().strip(),)
            )
            conexion.commit()
            return cursor.rowcount > 0

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo eliminar la palabra: {error_bd}")
        return False