"""
conexion.py
===========
Módulo encargado exclusivamente de gestionar la conexión
a la base de datos SQLite del Ahorcado Medieval.

Responsabilidades:
    - Definir la ruta absoluta de la base de datos.
    - Crear el directorio data/ si no existe.
    - Abrir y devolver la conexión configurada.

Este módulo es importado por inicializar.py, consultas.py
e insercion.py. Nunca debe importar de otros módulos
de base_datos para evitar dependencias circulares.
"""

import os
import sqlite3


# ── Constantes ────────────────────────────────────────────────

# Ruta absoluta hacia data/palabras.db desde este archivo
RUTA_BASE_DATOS: str = os.path.join(
    os.path.dirname(__file__),  # src/base_datos/
    "..",                        # src/
    "..",                        # raíz del proyecto
    "data",
    "palabras.db",
)


# ── Función pública ───────────────────────────────────────────

def obtener_conexion() -> sqlite3.Connection:
    """
    Abre y devuelve una conexión activa a la base de datos SQLite.

    Crea el directorio data/ automáticamente si no existe.
    Configura row_factory para que cada fila devuelta pueda
    accederse como diccionario mediante dict(fila).

    Returns:
        sqlite3.Connection: Conexión activa lista para usar.

    Raises:
        sqlite3.Error: Si no es posible conectarse a la base de datos.
    """
    ruta_directorio = os.path.dirname(RUTA_BASE_DATOS)
    os.makedirs(ruta_directorio, exist_ok=True)

    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row

    return conexion