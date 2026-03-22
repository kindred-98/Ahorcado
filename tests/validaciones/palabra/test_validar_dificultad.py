"""
test_validar_dificultad.py
==========================
Tests para src/validaciones/palabra/validar_dificultad.py
"""

from src.validaciones.palabra.validar_dificultad import validar_dificultad


# ── Casos válidos ─────────────────────────────────────────────

def test_dificultad_facil_valida():
    assert validar_dificultad("facil") is None

def test_dificultad_medio_valida():
    assert validar_dificultad("medio") is None

def test_dificultad_dificil_valida():
    assert validar_dificultad("dificil") is None

def test_dificultad_legendario_valida():
    assert validar_dificultad("legendario") is None

def test_dificultad_mayusculas_valida():
    assert validar_dificultad("FACIL") is None


# ── Casos inválidos ───────────────────────────────────────────

def test_dificultad_invalida_devuelve_error():
    assert validar_dificultad("imposible") is not None

def test_dificultad_vacia_devuelve_error():
    assert validar_dificultad("") is not None

def test_dificultad_con_tilde_devuelve_error():
    assert validar_dificultad("difícil") is not None