"""
obtener_conexion.py
===================
Función para abrir y devolver la conexión a la base de datos.
"""

import os
import sqlite3

from src.base_datos.conexion.ruta_base_datos import RUTA_BASE_DATOS


def obtener_conexion() -> sqlite3.Connection:
    """
    Abre y devuelve una conexión activa a la base de datos SQLite.

    Crea el directorio data/ automáticamente si no existe.
    Configura row_factory para acceder a las filas como diccionario.

    Returns:
        sqlite3.Connection: Conexión activa lista para usar.

    Raises:
        sqlite3.Error: Si no es posible conectarse a la base de datos.
    """
    os.makedirs(os.path.dirname(RUTA_BASE_DATOS), exist_ok=True)
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion