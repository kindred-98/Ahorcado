"""
test_construir_cabecera.py
==========================
Tests para src/interfaz/pantalla/construir_cabecera.py
"""

from src.interfaz.pantalla.construir_cabecera import construir_cabecera


def test_contiene_titulo():
    assert "AHORCADO MEDIEVAL" in construir_cabecera("_ _ _ _ _ _ _ _", [])

def test_contiene_palabra_oculta():
    assert "c _ s t _ _ _ o" in construir_cabecera("c _ s t _ _ _ o", [])

def test_sin_letras_muestra_ninguna():
    assert "ninguna" in construir_cabecera("_ _ _ _ _ _ _ _", [])

def test_con_letras_las_muestra():
    cabecera = construir_cabecera("_ _ _ _ _ _ _ _", ["a", "c"])
    assert "A" in cabecera
    assert "C" in cabecera

def test_devuelve_string():
    assert isinstance(construir_cabecera("_ _ _", []), str)

def test_tiene_bordes():
    cabecera = construir_cabecera("_ _ _", [])
    assert "╔" in cabecera
    assert "╚" in cabecera