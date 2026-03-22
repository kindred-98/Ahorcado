"""
test_mostrar_victoria.py
========================
Tests para src/interfaz/pantalla/mostrar_victoria.py
"""

from unittest.mock import patch
from src.interfaz.pantalla.mostrar_victoria import mostrar_victoria, _mostrar_pantalla_final


def test_mostrar_victoria_no_lanza_excepcion(capsys):
    with patch("time.sleep"), patch("os.system"):
        mostrar_victoria("castillo")


def test_mostrar_victoria_muestra_palabra(capsys):
    with patch("time.sleep"), patch("os.system"):
        mostrar_victoria("castillo")
    salida = capsys.readouterr().out
    assert "CASTILLO" in salida


def test_pantalla_final_contiene_titulo(capsys):
    _mostrar_pantalla_final("dragon")
    salida = capsys.readouterr().out
    assert "VICTORIA" in salida

def test_pantalla_final_contiene_palabra(capsys):
    _mostrar_pantalla_final("dragon")
    salida = capsys.readouterr().out
    assert "DRAGON" in salida

def test_pantalla_final_contiene_mensaje_reino(capsys):
    _mostrar_pantalla_final("dragon")
    salida = capsys.readouterr().out
    assert "reino" in salida