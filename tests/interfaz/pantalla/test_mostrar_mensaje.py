"""
test_mostrar_mensaje.py
=======================
Tests para src/interfaz/pantalla/mostrar_mensaje.py
"""

from src.interfaz.pantalla.mostrar_mensaje import mostrar_mensaje


def test_mensaje_aparece_en_salida(capsys):
    mostrar_mensaje("Hola caballero")
    salida = capsys.readouterr().out
    assert "Hola caballero" in salida

def test_no_lanza_excepcion():
    mostrar_mensaje("Cualquier mensaje")