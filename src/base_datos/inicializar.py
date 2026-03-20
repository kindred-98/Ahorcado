"""
inicializar.py
==============
Módulo encargado de preparar la base de datos del
Ahorcado Medieval en el primer arranque.

Responsabilidades:
    - Crear la tabla 'palabras' si no existe.
    - Poblar la tabla con las palabras iniciales del juego.

La operación es idempotente: si la tabla ya existe y tiene
datos, no se duplican registros gracias a INSERT OR IGNORE.

Importaciones necesarias:
    from src.base_datos.conexion import obtener_conexion
"""

import sqlite3

from src.base_datos.conexion import obtener_conexion


# ── Palabras iniciales ────────────────────────────────────────

PALABRAS_INICIALES: list[tuple[str, str, str]] = [
    # (palabra, categoria, dificultad)

    # Animales
    ("dragon",      "animales",   "dificil"),
    ("lobo",        "animales",   "facil"),
    ("cuervo",      "animales",   "medio"),
    ("jabali",      "animales",   "medio"),
    ("serpiente",   "animales",   "dificil"),

    # Armas
    ("espada",      "armas",      "facil"),
    ("lanza",       "armas",      "facil"),
    ("escudo",      "armas",      "medio"),
    ("ballesta",    "armas",      "medio"),
    ("mandoble",    "armas",      "dificil"),

    # Lugares
    ("castillo",    "lugares",    "medio"),
    ("mazmorra",    "lugares",    "dificil"),
    ("aldea",       "lugares",    "facil"),
    ("fortaleza",   "lugares",    "dificil"),
    ("taberna",     "lugares",    "medio"),

    # Personajes
    ("caballero",   "personajes", "medio"),
    ("rey",         "personajes", "facil"),
    ("hechicero",   "personajes", "dificil"),
    ("arquero",     "personajes", "medio"),
    ("herrero",     "personajes", "dificil"),
]


# ── Función pública ───────────────────────────────────────────

def inicializar_base_datos() -> None:
    """
    Crea la tabla 'palabras' si no existe y la puebla con
    las palabras definidas en PALABRAS_INICIALES.

    La tabla tiene los campos:
        - id         : clave primaria autoincremental.
        - palabra    : texto único en minúsculas.
        - categoria  : categoría temática de la palabra.
        - dificultad : nivel facil, medio o dificil.

    Si la tabla ya existe y contiene datos, la función
    no duplica registros gracias a INSERT OR IGNORE.

    Raises:
        sqlite3.Error: Si ocurre un error al crear o poblar
                       la tabla.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            _crear_tabla_palabras(cursor)
            _poblar_palabras_iniciales(cursor)
            conexion.commit()

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo inicializar la base de datos: {error_bd}")


# ── Funciones privadas ────────────────────────────────────────

def _crear_tabla_palabras(cursor: sqlite3.Cursor) -> None:
    """
    Ejecuta el CREATE TABLE IF NOT EXISTS para la tabla 'palabras'.

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


def _poblar_palabras_iniciales(cursor: sqlite3.Cursor) -> None:
    """
    Inserta las palabras de PALABRAS_INICIALES en la tabla.
    Usa INSERT OR IGNORE para no duplicar registros existentes.

    Args:
        cursor (sqlite3.Cursor): Cursor activo de la conexión.
    """
    cursor.executemany("""
        INSERT OR IGNORE INTO palabras (palabra, categoria, dificultad)
        VALUES (?, ?, ?)
    """, PALABRAS_INICIALES)