"""
test_construir_etiqueta_fallos.py
==================================
Tests para src/interfaz/pantalla/construir_etiqueta_fallos.py
"""

from src.interfaz.pantalla.construir_etiqueta_fallos import _construir_etiqueta_fallos
from src.interfaz.dibujo.maximo_fallos               import MAXIMO_FALLOS


def test_cero_fallos_muestra_sin_fallos():
    assert "Sin fallos" in _construir_etiqueta_fallos(0)

def test_maximo_fallos_muestra_intentos():
    assert "intentos" in _construir_etiqueta_fallos(MAXIMO_FALLOS).lower()

def test_fallos_intermedios_muestra_numero():
    resultado = _construir_etiqueta_fallos(3)
    assert "3" in resultado
    assert str(MAXIMO_FALLOS) in resultado

def test_devuelve_string():
    assert isinstance(_construir_etiqueta_fallos(0), str)