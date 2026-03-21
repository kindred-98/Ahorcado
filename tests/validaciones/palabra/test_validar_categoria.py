"""
test_validar_categoria.py
=========================
Tests para src/validaciones/palabra/validar_categoria.py
"""

from src.validaciones.palabra.validar_categoria import validar_categoria


# ── Casos válidos ─────────────────────────────────────────────

def test_categoria_animales_valida():
    assert validar_categoria("animales") is None

def test_categoria_armas_valida():
    assert validar_categoria("armas") is None

def test_categoria_lugares_valida():
    assert validar_categoria("lugares") is None

def test_categoria_personajes_valida():
    assert validar_categoria("personajes") is None

def test_categoria_mayusculas_valida():
    assert validar_categoria("ANIMALES") is None


# ── Casos inválidos ───────────────────────────────────────────

def test_categoria_invalida_devuelve_error():
    assert validar_categoria("comida") is not None

def test_categoria_vacia_devuelve_error():
    assert validar_categoria("") is not None

def test_categoria_con_espacios_invalida():
    assert validar_categoria("   ") is not None