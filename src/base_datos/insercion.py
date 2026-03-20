"""
insercion.py
============
Módulo encargado de todas las operaciones de escritura
sobre la base de datos del Ahorcado Medieval.

Responsabilidades:
    - Insertar una nueva palabra validando que no exista ya.
    - Informar si la palabra fue insertada o ya existía.

Importaciones necesarias:
    from src.base_datos.conexion import obtener_conexion
"""

import sqlite3
from typing import Optional

from src.base_datos.conexion import obtener_conexion


# ── Constantes ────────────────────────────────────────────────

DIFICULTADES_VALIDAS: tuple[str, ...] = ("facil", "medio", "dificil")


# ── Funciones públicas ────────────────────────────────────────

def insertar_palabra(
    palabra:    str,
    categoria:  str,
    dificultad: str,
) -> bool:
    """
    Inserta una nueva palabra en la base de datos.

    La palabra se normaliza a minúsculas antes de insertarse.
    Si la palabra ya existe, no se inserta ni se lanza error
    gracias a INSERT OR IGNORE.

    Args:
        palabra    (str): La palabra a insertar.
        categoria  (str): Categoría temática de la palabra.
                          Ejemplo: "animales", "armas", "lugares"
        dificultad (str): Nivel de dificultad de la palabra.
                          Valores válidos: "facil", "medio", "dificil"

    Returns:
        bool: True si la palabra fue insertada correctamente.
              False si ya existía en la base de datos o si
              ocurrió un error.
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


def palabra_ya_existe(palabra: str) -> bool:
    """
    Comprueba si una palabra ya existe en la base de datos.

    Args:
        palabra (str): La palabra a buscar (sin distinguir mayúsculas).

    Returns:
        bool: True si la palabra ya existe. False si no existe
              o si ocurre un error.
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


# ── Funciones privadas ────────────────────────────────────────

def _normalizar_dificultad(dificultad: str) -> Optional[str]:
    """
    Valida y normaliza el valor de dificultad recibido.

    Args:
        dificultad (str): Valor de dificultad a normalizar.

    Returns:
        str | None: El valor normalizado si es válido,
                    None si no pertenece a DIFICULTADES_VALIDAS.
    """
    valor_normalizado = dificultad.lower().strip()

    if valor_normalizado not in DIFICULTADES_VALIDAS:
        return None

    return valor_normalizado