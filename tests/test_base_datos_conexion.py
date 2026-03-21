"""
test_base_datos_conexion.py
===========================
Tests para src/base_datos/conexion.py
"""

import sqlite3
from src.base_datos.conexion import obtener_conexion


def test_obtener_conexion_devuelve_connection(bd_prueba):
    conexion = obtener_conexion()
    assert isinstance(conexion, sqlite3.Connection)
    conexion.close()

def test_conexion_tiene_row_factory(bd_prueba):
    conexion = obtener_conexion()
    assert conexion.row_factory == sqlite3.Row
    conexion.close()

def test_conexion_es_funcional(bd_prueba):
    conexion = obtener_conexion()
    cursor = conexion.execute("SELECT 1")
    resultado = cursor.fetchone()
    assert resultado[0] == 1
    conexion.close()