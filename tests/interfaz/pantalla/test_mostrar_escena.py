"""
test_mostrar_escena.py
======================
Tests para src/interfaz/pantalla/mostrar_escena.py
"""

import pytest
from src.interfaz.pantalla.mostrar_escena import mostrar_escena


def test_valor_invalido_lanza_error():
    with pytest.raises(ValueError):
        mostrar_escena(numero_fallos=7, palabra_oculta="_ _ _", letras_usadas=[])

def test_negativo_lanza_error():
    with pytest.raises(ValueError):
        mostrar_escena(numero_fallos=-1, palabra_oculta="_ _ _", letras_usadas=[])

def test_estado_cero_renderiza(capsys):
    mostrar_escena(numero_fallos=0, palabra_oculta="_ _ _ _ _ _ _ _", letras_usadas=[])
    salida = capsys.readouterr().out
    assert "AHORCADO MEDIEVAL" in salida

def test_estado_seis_renderiza(capsys):
    mostrar_escena(numero_fallos=6, palabra_oculta="castillo", letras_usadas=["a", "c"])
    salida = capsys.readouterr().out
    assert "castillo" in salida