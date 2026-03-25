"""
test_eliminar_palabra.py
========================
Tests para src/base_datos/insercion/eliminar_palabra.py
"""

from src.base_datos.insercion.eliminar_palabra import eliminar_palabra


def test_eliminar_palabra_existente_devuelve_true(bd_prueba):
    assert eliminar_palabra("dragon") is True

def test_eliminar_palabra_ya_no_existe_en_bd(bd_prueba):
    eliminar_palabra("dragon")
    cursor = bd_prueba.execute("SELECT palabra FROM palabras WHERE palabra = 'dragon'")
    assert cursor.fetchone() is None

def test_eliminar_palabra_inexistente_devuelve_false(bd_prueba):
    assert eliminar_palabra("unicornio") is False

def test_eliminar_normaliza_mayusculas(bd_prueba):
    assert eliminar_palabra("DRAGON") is True

def test_eliminar_normaliza_espacios(bd_prueba):
    assert eliminar_palabra("  dragon  ") is True