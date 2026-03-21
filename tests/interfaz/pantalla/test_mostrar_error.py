"""
test_mostrar_error.py
=====================
Tests para src/interfaz/pantalla/mostrar_error.py
"""

from src.interfaz.pantalla.mostrar_error import mostrar_error


def test_incluye_simbolo_advertencia(capsys):
    mostrar_error("Error de prueba")
    salida = capsys.readouterr().out
    assert "⚠" in salida

def test_incluye_mensaje(capsys):
    mostrar_error("Error de prueba")
    salida = capsys.readouterr().out
    assert "Error de prueba" in salida

def test_no_lanza_excepcion():
    mostrar_error("Cualquier error")