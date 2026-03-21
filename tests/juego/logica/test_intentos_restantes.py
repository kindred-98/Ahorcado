"""
test_intentos_restantes.py
==========================
Tests para src/juego/logica/intentos_restantes.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.logica.intentos_restantes    import intentos_restantes
from src.interfaz.dibujo.maximo_fallos              import MAXIMO_FALLOS


def test_cero_fallos_devuelve_maximo():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert intentos_restantes(estado) == MAXIMO_FALLOS

def test_tres_fallos_devuelve_tres():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           numero_fallos=3)
    assert intentos_restantes(estado) == 3

def test_derrota_devuelve_cero():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           numero_fallos=MAXIMO_FALLOS)
    assert intentos_restantes(estado) == 0

def test_devuelve_entero():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert isinstance(intentos_restantes(estado), int)