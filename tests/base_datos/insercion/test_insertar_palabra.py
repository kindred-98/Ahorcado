"""
test_insertar_palabra.py
========================
Tests para src/base_datos/insercion/insertar_palabra.py
"""

from src.base_datos.insercion.insertar_palabra import insertar_palabra


def test_nueva_palabra_devuelve_true(bd_prueba):
    assert insertar_palabra("unicornio", "animales", "dificil") is True

def test_nueva_palabra_existe_en_bd(bd_prueba):
    insertar_palabra("unicornio", "animales", "dificil")
    cursor = bd_prueba.execute("SELECT palabra FROM palabras WHERE palabra = 'unicornio'")
    assert cursor.fetchone() is not None

def test_duplicada_devuelve_false(bd_prueba):
    insertar_palabra("unicornio", "animales", "dificil")
    assert insertar_palabra("unicornio", "animales", "dificil") is False

def test_normaliza_mayusculas(bd_prueba):
    insertar_palabra("UNICORNIO", "animales", "dificil")
    cursor = bd_prueba.execute("SELECT palabra FROM palabras WHERE palabra = 'unicornio'")
    assert cursor.fetchone() is not None

def test_mayuscula_duplica_minuscula(bd_prueba):
    assert insertar_palabra("DRAGON", "animales", "dificil") is False

def test_espacios_extremos(bd_prueba):
    insertar_palabra("  pegaso  ", "animales", "medio")
    cursor = bd_prueba.execute("SELECT palabra FROM palabras WHERE palabra = 'pegaso'")
    assert cursor.fetchone() is not None

def test_no_duplica_distinta_capitalizacion(bd_prueba):
    insertar_palabra("fenix", "animales", "dificil")
    assert insertar_palabra("FENIX", "animales", "dificil") is False