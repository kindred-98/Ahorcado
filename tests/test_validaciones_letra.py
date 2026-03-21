"""
test_validaciones_letra.py
==========================
Tests unitarios para src/validaciones/letra.py
"""

import pytest
from src.validaciones.letra import validar_letra


# ── Tests casos válidos ───────────────────────────────────────

def test_letra_minuscula_valida():
    assert validar_letra("a") is None

def test_letra_mayuscula_valida():
    assert validar_letra("A") is None

def test_letra_con_tilde_valida():
    assert validar_letra("á") is None

def test_letra_tilde_mayuscula_valida():
    assert validar_letra("Á") is None

def test_enie_minuscula_valida():
    assert validar_letra("ñ") is None

def test_enie_mayuscula_valida():
    assert validar_letra("Ñ") is None


# ── Tests casos inválidos ─────────────────────────────────────

def test_entrada_vacia_devuelve_error():
    assert validar_letra("") is not None

def test_varias_letras_devuelve_error():
    assert validar_letra("ab") is not None

def test_numero_devuelve_error():
    assert validar_letra("3") is not None

def test_simbolo_devuelve_error():
    assert validar_letra("!") is not None

def test_espacio_devuelve_error():
    assert validar_letra(" ") is not None


# ── Tests casos edge ──────────────────────────────────────────

def test_espacios_en_blanco_devuelve_error():
    assert validar_letra("   ") is not None

def test_salto_de_linea_devuelve_error():
    assert validar_letra("\n") is not None

def test_tabulacion_devuelve_error():
    assert validar_letra("\t") is not None

def test_letra_mas_espacio_devuelve_error():
    assert validar_letra("a ") is not None

def test_mensaje_error_es_string():
    resultado = validar_letra("")
    assert isinstance(resultado, str)

def test_letra_valida_devuelve_none_no_string():
    resultado = validar_letra("a")
    assert resultado is None