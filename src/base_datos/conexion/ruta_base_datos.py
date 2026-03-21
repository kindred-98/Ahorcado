"""
ruta_base_datos.py
==================
Constante con la ruta absoluta a la base de datos SQLite.
"""

import os

RUTA_BASE_DATOS: str = os.path.join(
    os.path.dirname(__file__),  # src/base_datos/conexion/
    "..",                        # src/base_datos/
    "..",                        # src/
    "..",                        # raíz del proyecto
    "data",
    "palabras.db",
)