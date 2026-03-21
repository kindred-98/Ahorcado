"""
inicializar_base_datos.py
=========================
Función pública para inicializar la base de datos al arranque.
"""

import sqlite3

from src.base_datos.conexion.obtener_conexion             import obtener_conexion
from src.base_datos.inicializar.crear_tabla_palabras      import _crear_tabla_palabras
from src.base_datos.inicializar.poblar_palabras_iniciales import _poblar_palabras_iniciales


def inicializar_base_datos() -> None:
    """
    Crea la tabla palabras si no existe y la puebla con las
    palabras iniciales. La operación es idempotente gracias
    a CREATE TABLE IF NOT EXISTS e INSERT OR IGNORE.

    Raises:
        sqlite3.Error: Si ocurre un error al crear o poblar la tabla.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            _crear_tabla_palabras(cursor)
            _poblar_palabras_iniciales(cursor)
            conexion.commit()

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo inicializar la base de datos: {error_bd}")