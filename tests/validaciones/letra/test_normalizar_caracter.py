"""
test_normalizar_caracter.py
===========================
Tests para src/validaciones/letra/normalizar_caracter.py
"""

from src.validaciones.letra.normalizar_caracter import _normalizar_caracter


# ── Casos normales ────────────────────────────────────────────

def test_letra_sin_tilde():
    assert _normalizar_caracter("a") == "a"

def test_letra_a_con_tilde():
    assert _normalizar_caracter("á") == "a"

def test_letra_e_con_tilde():
    assert _normalizar_caracter("é") == "e"

def test_letra_i_con_tilde():
    assert _normalizar_caracter("í") == "i"

def test_letra_o_con_tilde():
    assert _normalizar_caracter("ó") == "o"

def test_letra_u_con_tilde():
    assert _normalizar_caracter("ú") == "u"


# ── Casos edge ────────────────────────────────────────────────

def test_mayuscula_con_tilde():
    assert _normalizar_caracter("Á") == "a"

def test_mayuscula_sin_tilde():
    assert _normalizar_caracter("A") == "a"

def test_devuelve_string():
    assert isinstance(_normalizar_caracter("a"), str)