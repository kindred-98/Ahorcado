"""
test_crear_estado_inicial.py
============================
Tests para src/juego/estado/crear_estado_inicial.py
"""

from src.juego.estado.crear_estado_inicial  import crear_estado_inicial
from src.juego.estado.clase_estado_partida  import EstadoPartida


def test_crea_estado_con_palabra():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert estado.palabra_secreta == "espada"

def test_crea_estado_con_categoria():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert estado.categoria == "armas"

def test_crea_estado_con_dificultad():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert estado.dificultad == "facil"

def test_crea_estado_sin_letras_correctas():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert len(estado.letras_correctas) == 0

def test_crea_estado_sin_letras_fallidas():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert len(estado.letras_fallidas) == 0

def test_crea_estado_con_cero_fallos():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert estado.numero_fallos == 0

def test_devuelve_estado_partida():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    assert isinstance(crear_estado_inicial(registro), EstadoPartida)