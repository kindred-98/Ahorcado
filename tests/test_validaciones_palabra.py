"""
test_validaciones_palabra.py
============================
Tests unitarios para src/validaciones/palabra.py
"""

from src.validaciones.palabra import (
    validar_palabra,
    validar_categoria,
    validar_dificultad,
)


# ── Tests validar_palabra — casos válidos ─────────────────────

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


# ── Tests validar_palabra — casos inválidos ───────────────────

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


# ── Tests validar_palabra — casos edge ───────────────────────

def test_palabra_solo_espacios_devuelve_error():
    assert validar_palabra("   ") is not None

def test_palabra_con_espacios_extremos_valida():
    # strip elimina espacios, "dragon" tiene 6 letras válidas
    assert validar_palabra("  dragon  ") is None

def test_palabra_mayusculas_valida():
    assert validar_palabra("DRAGON") is None

def test_mensaje_error_es_string():
    resultado = validar_palabra("")
    assert isinstance(resultado, str)


# ── Tests validar_categoria — casos válidos ───────────────────

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


# ── Tests validar_categoria — casos inválidos ────────────────

def test_categoria_invalida_devuelve_error():
    assert validar_categoria("comida") is not None

def test_categoria_vacia_devuelve_error():
    assert validar_categoria("") is not None

def test_categoria_con_espacios_invalida():
    assert validar_categoria("   ") is not None


# ── Tests validar_dificultad — casos válidos ──────────────────

def test_dificultad_facil_valida():
    assert validar_dificultad("facil") is None

def test_dificultad_medio_valida():
    assert validar_dificultad("medio") is None

def test_dificultad_dificil_valida():
    assert validar_dificultad("dificil") is None

def test_dificultad_mayusculas_valida():
    assert validar_dificultad("FACIL") is None


# ── Tests validar_dificultad — casos inválidos ───────────────

def test_dificultad_invalida_devuelve_error():
    assert validar_dificultad("imposible") is not None

def test_dificultad_vacia_devuelve_error():
    assert validar_dificultad("") is not None

def test_dificultad_con_tilde_devuelve_error():
    assert validar_dificultad("difícil") is not None