"""
test_obtener_todas_las_palabras.py
===================================
Tests para src/base_datos/consultas/obtener_todas_las_palabras.py
"""

from src.base_datos.consultas.obtener_todas_las_palabras import obtener_todas_las_palabras


def test_devuelve_lista(bd_prueba):
    assert isinstance(obtener_todas_las_palabras(), list)

def test_lista_no_vacia(bd_prueba):
    assert len(obtener_todas_las_palabras()) > 0

def test_cada_elemento_es_dict(bd_prueba):
    for palabra in obtener_todas_las_palabras():
        assert isinstance(palabra, dict)

def test_ordenadas_por_categoria(bd_prueba):
    resultado = obtener_todas_las_palabras()
    categorias = [r["categoria"] for r in resultado]
    assert categorias == sorted(categorias)

def test_bd_vacia_devuelve_lista_vacia(bd_prueba):
    bd_prueba.execute("DELETE FROM palabras")
    bd_prueba.commit()
    assert obtener_todas_las_palabras() == []