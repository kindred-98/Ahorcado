"""
test_palabra_ya_existe.py
=========================
Tests para src/base_datos/insercion/palabra_ya_existe.py
"""

from src.base_datos.insercion.palabra_ya_existe import palabra_ya_existe


def test_existente_devuelve_true(bd_prueba):
    assert palabra_ya_existe("dragon") is True

def test_inexistente_devuelve_false(bd_prueba):
    assert palabra_ya_existe("unicornio") is False

def test_mayuscula_detecta_existente(bd_prueba):
    assert palabra_ya_existe("DRAGON") is True

def test_espacios_se_ignoran(bd_prueba):
    assert palabra_ya_existe("  dragon  ") is True

def test_devuelve_bool(bd_prueba):
    assert isinstance(palabra_ya_existe("dragon"), bool)