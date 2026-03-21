"""
test_base_datos_insercion.py
============================
Tests para src/base_datos/insercion.py
"""

from src.base_datos.insercion import insertar_palabra, palabra_ya_existe


# ── Tests insertar_palabra ────────────────────────────────────

def test_insertar_palabra_nueva_devuelve_true(bd_prueba):
    resultado = insertar_palabra("unicornio", "animales", "dificil")
    assert resultado is True

def test_insertar_palabra_nueva_existe_en_bd(bd_prueba):
    insertar_palabra("unicornio", "animales", "dificil")
    cursor = bd_prueba.execute(
        "SELECT palabra FROM palabras WHERE palabra = 'unicornio'"
    )
    assert cursor.fetchone() is not None

def test_insertar_palabra_duplicada_devuelve_false(bd_prueba):
    insertar_palabra("unicornio", "animales", "dificil")
    resultado = insertar_palabra("unicornio", "animales", "dificil")
    assert resultado is False

def test_insertar_palabra_normaliza_mayusculas(bd_prueba):
    insertar_palabra("UNICORNIO", "animales", "dificil")
    cursor = bd_prueba.execute(
        "SELECT palabra FROM palabras WHERE palabra = 'unicornio'"
    )
    assert cursor.fetchone() is not None

def test_insertar_palabra_mayuscula_duplica_minuscula(bd_prueba):
    # "dragon" ya existe en bd_prueba, "DRAGON" debe ser duplicado
    resultado = insertar_palabra("DRAGON", "animales", "dificil")
    assert resultado is False

def test_insertar_palabra_con_espacios_extremos(bd_prueba):
    insertar_palabra("  pegaso  ", "animales", "medio")
    cursor = bd_prueba.execute(
        "SELECT palabra FROM palabras WHERE palabra = 'pegaso'"
    )
    assert cursor.fetchone() is not None

def test_insertar_no_duplica_con_distinta_capitalizacion(bd_prueba):
    insertar_palabra("fenix", "animales", "dificil")
    resultado = insertar_palabra("FENIX", "animales", "dificil")
    assert resultado is False


# ── Tests palabra_ya_existe ───────────────────────────────────

def test_palabra_ya_existe_true(bd_prueba):
    assert palabra_ya_existe("dragon") is True

def test_palabra_ya_existe_false(bd_prueba):
    assert palabra_ya_existe("unicornio") is False

def test_palabra_ya_existe_mayuscula(bd_prueba):
    # "dragon" existe, "DRAGON" debe encontrarse igual
    assert palabra_ya_existe("DRAGON") is True

def test_palabra_ya_existe_con_espacios(bd_prueba):
    assert palabra_ya_existe("  dragon  ") is True

def test_palabra_ya_existe_devuelve_bool(bd_prueba):
    assert isinstance(palabra_ya_existe("dragon"), bool)