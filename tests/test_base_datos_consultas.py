"""
test_base_datos_consultas.py
============================
Tests para src/base_datos/consultas.py
"""

from src.base_datos.consultas import (
    obtener_palabra_aleatoria,
    obtener_todas_las_palabras,
    obtener_categorias,
)


# ── Tests obtener_palabra_aleatoria ───────────────────────────

def test_obtener_palabra_aleatoria_devuelve_dict(bd_prueba):
    resultado = obtener_palabra_aleatoria()
    assert isinstance(resultado, dict)

def test_obtener_palabra_aleatoria_tiene_claves(bd_prueba):
    resultado = obtener_palabra_aleatoria()
    assert "palabra"    in resultado
    assert "categoria"  in resultado
    assert "dificultad" in resultado

def test_obtener_palabra_por_categoria(bd_prueba):
    resultado = obtener_palabra_aleatoria(categoria="animales")
    assert resultado["categoria"] == "animales"

def test_obtener_palabra_categoria_inexistente_devuelve_none(bd_prueba):
    resultado = obtener_palabra_aleatoria(categoria="comida")
    assert resultado is None

def test_obtener_palabra_bd_vacia_devuelve_none(bd_prueba):
    bd_prueba.execute("DELETE FROM palabras")
    bd_prueba.commit()
    resultado = obtener_palabra_aleatoria()
    assert resultado is None

def test_obtener_palabra_por_dificultad(bd_prueba):
    resultado = obtener_palabra_aleatoria(dificultad="facil")
    assert resultado["dificultad"] == "facil"

def test_obtener_palabra_con_filtros_combinados(bd_prueba):
    resultado = obtener_palabra_aleatoria(categoria="animales", dificultad="facil")
    if resultado:
        assert resultado["categoria"]  == "animales"
        assert resultado["dificultad"] == "facil"


# ── Tests obtener_todas_las_palabras ──────────────────────────

def test_obtener_todas_devuelve_lista(bd_prueba):
    resultado = obtener_todas_las_palabras()
    assert isinstance(resultado, list)

def test_obtener_todas_no_vacia(bd_prueba):
    resultado = obtener_todas_las_palabras()
    assert len(resultado) > 0

def test_obtener_todas_cada_elemento_es_dict(bd_prueba):
    resultado = obtener_todas_las_palabras()
    for palabra in resultado:
        assert isinstance(palabra, dict)

def test_obtener_todas_ordenadas_por_categoria(bd_prueba):
    resultado = obtener_todas_las_palabras()
    categorias = [r["categoria"] for r in resultado]
    assert categorias == sorted(categorias)

def test_obtener_todas_bd_vacia_devuelve_lista_vacia(bd_prueba):
    bd_prueba.execute("DELETE FROM palabras")
    bd_prueba.commit()
    resultado = obtener_todas_las_palabras()
    assert resultado == []


# ── Tests obtener_categorias ──────────────────────────────────

def test_obtener_categorias_devuelve_lista(bd_prueba):
    resultado = obtener_categorias()
    assert isinstance(resultado, list)

def test_obtener_categorias_tiene_claves(bd_prueba):
    resultado = obtener_categorias()
    for categoria in resultado:
        assert "categoria" in categoria
        assert "total"     in categoria

def test_obtener_categorias_total_es_entero(bd_prueba):
    resultado = obtener_categorias()
    for categoria in resultado:
        assert isinstance(categoria["total"], int)

def test_obtener_categorias_bd_vacia_devuelve_lista_vacia(bd_prueba):
    bd_prueba.execute("DELETE FROM palabras")
    bd_prueba.commit()
    resultado = obtener_categorias()
    assert resultado == []