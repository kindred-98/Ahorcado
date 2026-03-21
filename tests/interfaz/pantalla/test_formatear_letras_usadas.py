"""
test_formatear_letras_usadas.py
================================
Tests para src/interfaz/pantalla/formatear_letras_usadas.py
"""

from src.interfaz.pantalla.formatear_letras_usadas import _formatear_letras_usadas


def test_lista_vacia_devuelve_ninguna():
    assert _formatear_letras_usadas([]) == "Letras usadas: ninguna"

def test_letras_en_mayusculas():
    resultado = _formatear_letras_usadas(["a", "b"])
    assert "A" in resultado
    assert "B" in resultado

def test_separadas_por_coma():
    assert "," in _formatear_letras_usadas(["a", "b"])

def test_devuelve_string():
    assert isinstance(_formatear_letras_usadas(["a"]), str)