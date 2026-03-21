"""
test_cobertura_completa.py
==========================
Tests adicionales para cubrir las ramas faltantes
e ir del 96% al 100% de cobertura.

Cubre:
    - Ramas except sqlite3.Error en base_datos/
    - ValueError en pantalla.mostrar_escena()
    - _normalizar_caracter() en validaciones/letra.py
    - _normalizar_dificultad() en base_datos/insercion.py
    - mostrar_escena() completa
"""

import sqlite3
import pytest

from src.base_datos.insercion  import insertar_palabra, palabra_ya_existe, _normalizar_dificultad
from src.base_datos.consultas  import obtener_palabra_aleatoria, obtener_todas_las_palabras, obtener_categorias
from src.base_datos.inicializar import inicializar_base_datos
from src.interfaz.pantalla     import mostrar_escena
from src.validaciones.letra.normalizar_caracter import _normalizar_caracter


# ── Tests _normalizar_dificultad ──────────────────────────────

def test_normalizar_dificultad_valida():
    assert _normalizar_dificultad("facil")   == "facil"
    assert _normalizar_dificultad("medio")   == "medio"
    assert _normalizar_dificultad("dificil") == "dificil"

def test_normalizar_dificultad_invalida():
    assert _normalizar_dificultad("imposible") is None

def test_normalizar_dificultad_mayusculas():
    assert _normalizar_dificultad("FACIL") == "facil"

def test_normalizar_dificultad_con_espacios():
    assert _normalizar_dificultad("  facil  ") == "facil"


# ── Tests except sqlite3.Error en insercion.py ───────────────

def test_insertar_palabra_error_bd(bd_prueba, monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error simulado")
    monkeypatch.setattr("src.base_datos.insercion.obtener_conexion", conexion_fallida)
    assert insertar_palabra("unicornio", "animales", "facil") is False

def test_palabra_ya_existe_error_bd(bd_prueba, monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error simulado")
    monkeypatch.setattr("src.base_datos.insercion.obtener_conexion", conexion_fallida)
    assert palabra_ya_existe("dragon") is False


# ── Tests except sqlite3.Error en consultas.py ───────────────

def test_obtener_palabra_aleatoria_error_bd(bd_prueba, monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error simulado")
    monkeypatch.setattr("src.base_datos.consultas.obtener_conexion", conexion_fallida)
    assert obtener_palabra_aleatoria() is None

def test_obtener_todas_error_bd(bd_prueba, monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error simulado")
    monkeypatch.setattr("src.base_datos.consultas.obtener_conexion", conexion_fallida)
    assert obtener_todas_las_palabras() == []

def test_obtener_categorias_error_bd(bd_prueba, monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error simulado")
    monkeypatch.setattr("src.base_datos.consultas.obtener_conexion", conexion_fallida)
    assert obtener_categorias() == []


# ── Tests except sqlite3.Error en inicializar.py ─────────────

def test_inicializar_error_bd(bd_prueba, monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error simulado")
    monkeypatch.setattr("src.base_datos.inicializar.obtener_conexion", conexion_fallida)
    inicializar_base_datos()  # no debe lanzar excepción


# ── Tests mostrar_escena ──────────────────────────────────────

def test_mostrar_escena_valor_invalido_lanza_error():
    with pytest.raises(ValueError):
        mostrar_escena(numero_fallos=7, palabra_oculta="_ _ _ _ _ _ _ _", letras_usadas=[])

def test_mostrar_escena_negativo_lanza_error():
    with pytest.raises(ValueError):
        mostrar_escena(numero_fallos=-1, palabra_oculta="_ _ _ _ _ _ _ _", letras_usadas=[])

def test_mostrar_escena_estado_cero(capsys):
    mostrar_escena(numero_fallos=0, palabra_oculta="_ _ _ _ _ _ _ _", letras_usadas=[])
    salida = capsys.readouterr().out
    assert "AHORCADO MEDIEVAL" in salida

def test_mostrar_escena_estado_seis(capsys):
    mostrar_escena(numero_fallos=6, palabra_oculta="castillo", letras_usadas=["a", "c"])
    salida = capsys.readouterr().out
    assert "castillo" in salida


# ── Tests _normalizar_caracter ────────────────────────────────

def test_normalizar_caracter_sin_tilde():
    assert _normalizar_caracter("a") == "a"

def test_normalizar_caracter_con_tilde():
    assert _normalizar_caracter("á") == "a"

def test_normalizar_caracter_e_tilde():
    assert _normalizar_caracter("é") == "e"

def test_normalizar_caracter_mayuscula_con_tilde():
    assert _normalizar_caracter("Á") == "a"