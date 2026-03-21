"""
consultas.py
============
Módulo encargado de todas las operaciones de lectura
sobre la base de datos del Ahorcado Medieval.

Responsabilidades:
    - Obtener una palabra aleatoria con filtros opcionales.
    - Obtener todas las palabras almacenadas.
    - Obtener las categorías disponibles con su conteo.

Importaciones necesarias:
    from src.base_datos.conexion import obtener_conexion
"""

import sqlite3
from typing import Optional

# después
from src.base_datos.conexion.obtener_conexion import obtener_conexion


# ── Funciones públicas ────────────────────────────────────────

def obtener_palabra_aleatoria(
    categoria:  Optional[str] = None,
    dificultad: Optional[str] = None,
) -> Optional[dict]:
    """
    Devuelve una palabra aleatoria de la base de datos.

    Se pueden aplicar filtros opcionales por categoría
    y/o dificultad. Si no se pasan filtros, se elige
    de entre todas las palabras disponibles.

    Args:
        categoria  (str, opcional): Filtra por categoría.
                                    Ejemplo: "animales"
        dificultad (str, opcional): Filtra por dificultad.
                                    Valores: "facil", "medio", "dificil"

    Returns:
        dict | None: Diccionario con las claves 'id', 'palabra',
                     'categoria' y 'dificultad', o None si no
                     hay palabras que coincidan con los filtros
                     o si ocurre un error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()

            consulta, parametros = _construir_consulta_aleatoria(
                categoria, dificultad
            )
            cursor.execute(consulta, parametros)
            fila = cursor.fetchone()

            return dict(fila) if fila else None

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudo obtener una palabra aleatoria: {error_bd}")
        return None


def obtener_todas_las_palabras() -> list[dict]:
    """
    Devuelve todas las palabras almacenadas en la base de datos,
    ordenadas por categoría y luego alfabéticamente por palabra.

    Returns:
        list[dict]: Lista de diccionarios con los campos de cada
                    palabra. Lista vacía si no hay registros o
                    si ocurre un error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id, palabra, categoria, dificultad
                FROM palabras
                ORDER BY categoria, palabra
            """)
            return [dict(fila) for fila in cursor.fetchall()]

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudieron obtener las palabras: {error_bd}")
        return []


def obtener_categorias() -> list[dict]:
    """
    Devuelve las categorías únicas disponibles en la base de datos
    junto con el número de palabras que contiene cada una.

    Returns:
        list[dict]: Lista de diccionarios con las claves 'categoria'
                    y 'total', ordenados alfabéticamente.
                    Lista vacía si no hay registros o si ocurre un error.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT categoria, COUNT(*) AS total
                FROM palabras
                GROUP BY categoria
                ORDER BY categoria
            """)
            return [dict(fila) for fila in cursor.fetchall()]

    except sqlite3.Error as error_bd:
        print(f"  [ERROR] No se pudieron obtener las categorías: {error_bd}")
        return []


# ── Funciones privadas ────────────────────────────────────────

def _construir_consulta_aleatoria(
    categoria:  Optional[str],
    dificultad: Optional[str],
) -> tuple[str, list]:
    """
    Construye dinámicamente la consulta SQL para obtener
    una palabra aleatoria según los filtros recibidos.

    Args:
        categoria  (str | None): Filtro de categoría.
        dificultad (str | None): Filtro de dificultad.

    Returns:
        tuple[str, list]: La consulta SQL y la lista de
                          parámetros para ejecutarla.
    """
    consulta    = "SELECT id, palabra, categoria, dificultad FROM palabras WHERE 1=1"
    parametros: list = []

    if categoria:
        consulta += " AND categoria = ?"
        parametros.append(categoria.lower())

    if dificultad:
        consulta += " AND dificultad = ?"
        parametros.append(dificultad.lower())

    consulta += " ORDER BY RANDOM() LIMIT 1"

    return consulta, parametros