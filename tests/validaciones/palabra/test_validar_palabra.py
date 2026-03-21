"""
test_validar_palabra.py
=======================
Tests para src/validaciones/palabra/validar_palabra.py
"""

from src.validaciones.palabra.validar_palabra import validar_palabra


# ── Casos válidos ─────────────────────────────────────────────

def test_palabra_valida():
    assert validar_palabra("dragon") is None

def test_palabra_con_tilde_valida():
    assert validar_palabra("murciélago") is None

def test_palabra_con_enie_valida():
    assert validar_palabra("cabaña") is None

def test_palabra_longitud_minima_exacta():
    assert validar_palabra("rey") is None

def test_palabra_longitud_maxima_exacta():
    assert validar_palabra("a" * 30) is None


# ── Casos inválidos ───────────────────────────────────────────

def test_palabra_vacia_devuelve_error():
    assert validar_palabra("") is not None

def test_palabra_muy_corta_devuelve_error():
    assert validar_palabra("ab") is not None

def test_palabra_muy_larga_devuelve_error():
    assert validar_palabra("a" * 31) is not None

def test_palabra_con_numero_devuelve_error():
    assert validar_palabra("dragon123") is not None

def test_palabra_con_espacio_devuelve_error():
    assert validar_palabra("el dragon") is not None

def test_palabra_con_guion_devuelve_error():
    assert validar_palabra("semi-dragon") is not None

def test_palabra_con_simbolo_devuelve_error():
    assert validar_palabra("drag@n") is not None


# ── Casos edge ────────────────────────────────────────────────

def test_palabra_solo_espacios_devuelve_error():
    assert validar_palabra("   ") is not None

def test_palabra_con_espacios_extremos_valida():
    assert validar_palabra("  dragon  ") is None

def test_palabra_mayusculas_valida():
    assert validar_palabra("DRAGON") is None

def test_mensaje_error_es_string():
    assert isinstance(validar_palabra(""), str)