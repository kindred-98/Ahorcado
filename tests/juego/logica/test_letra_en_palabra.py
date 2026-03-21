"""
test_letra_en_palabra.py
========================
Tests para src/juego/logica/letra_en_palabra.py
"""

from src.juego.logica.letra_en_palabra import letra_en_palabra


def test_letra_presente_devuelve_true():
    assert letra_en_palabra("c", "castillo") is True

def test_letra_ausente_devuelve_false():
    assert letra_en_palabra("x", "castillo") is False

def test_mayuscula_normalizada():
    assert letra_en_palabra("C", "castillo") is True

def test_letra_repetida_devuelve_true():
    assert letra_en_palabra("l", "castillo") is True

def test_tilde_no_coincide_sin_tilde():
    assert letra_en_palabra("é", "caballero") is False