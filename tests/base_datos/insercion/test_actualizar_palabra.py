"""
test_actualizar_palabra.py
==========================
Tests para src/base_datos/insercion/actualizar_palabra.py
"""

from src.base_datos.insercion.actualizar_palabra import actualizar_palabra


def test_actualizar_palabra_existente_devuelve_true(bd_prueba):
    assert actualizar_palabra("dragon", "fenix", "animales", "dificil") is True

def test_actualizar_cambia_nombre_en_bd(bd_prueba):
    actualizar_palabra("dragon", "fenix", "animales", "dificil")
    cursor = bd_prueba.execute("SELECT palabra FROM palabras WHERE palabra = 'fenix'")
    assert cursor.fetchone() is not None

def test_actualizar_elimina_nombre_anterior(bd_prueba):
    actualizar_palabra("dragon", "fenix", "animales", "dificil")
    cursor = bd_prueba.execute("SELECT palabra FROM palabras WHERE palabra = 'dragon'")
    assert cursor.fetchone() is None

def test_actualizar_palabra_inexistente_devuelve_false(bd_prueba):
    assert actualizar_palabra("unicornio", "fenix", "animales", "dificil") is False

def test_actualizar_normaliza_mayusculas(bd_prueba):
    assert actualizar_palabra("DRAGON", "fenix", "animales", "dificil") is True