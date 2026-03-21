"""
insertar_palabra.py
===================
Función para insertar una nueva palabra en la base de datos.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion import obtener_conexion


def insertar_palabra(
    palabra:    str,
    categoria:  str,
    dificultad: str,
) -> bool:
    """
    Inserta una nueva palabra en la base de datos.

    La palabra se normaliza a minúsculas antes de insertarse.
    Si ya existe no se inserta gracias a INSERT OR IGNORE.

    Args:
        palabra    (str): La palabra a insertar.
        categoria  (str): Categoría temática de la palabra.
        dificultad (str): Nivel de dificultad: facil, medio o dificil.

    Returns:
        bool: True si se insertó. False si ya existía o hubo error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO palabras (palabra, categoria, dificultad)
                VALUES (?, ?, ?)
            """, (
                palabra.lower().strip(),
                categoria.lower().strip(),
                dificultad.lower().strip(),
            ))
            conexion.commit()
            return cursor.rowcount > 0

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo insertar la palabra: {error_bd}")
        return False