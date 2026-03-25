"""
actualizar_palabra.py
=====================
Función para actualizar los datos de una palabra existente.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion import obtener_conexion


def actualizar_palabra(
    palabra_original: str,
    nueva_palabra:    str,
    nueva_categoria:  str,
    nueva_dificultad: str,
) -> bool:
    """
    Actualiza los datos de una palabra existente en la BD.

    Args:
        palabra_original (str): Palabra actual a modificar.
        nueva_palabra    (str): Nuevo valor para la palabra.
        nueva_categoria  (str): Nueva categoría.
        nueva_dificultad (str): Nueva dificultad.

    Returns:
        bool: True si fue actualizada. False si no existía o hubo error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE palabras
                SET palabra    = ?,
                    categoria  = ?,
                    dificultad = ?
                WHERE palabra  = ?
            """, (
                nueva_palabra.lower().strip(),
                nueva_categoria.lower().strip(),
                nueva_dificultad.lower().strip(),
                palabra_original.lower().strip(),
            ))
            conexion.commit()
            return cursor.rowcount > 0

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo actualizar la palabra: {error_bd}")
        return False