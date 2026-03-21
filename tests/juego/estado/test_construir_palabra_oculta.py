"""
test_construir_palabra_oculta.py
================================
Tests para src/juego/estado/construir_palabra_oculta.py
"""

from src.juego.estado.clase_estado_partida    import EstadoPartida
from src.juego.estado.construir_palabra_oculta import construir_palabra_oculta


def test_sin_letras_muestra_solo_guiones():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert construir_palabra_oculta(estado) == "_ _ _ _ _ _ _ _"

def test_con_una_letra_correcta():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c"})
    assert construir_palabra_oculta(estado) == "c _ _ _ _ _ _ _"

def test_letra_repetida_se_revela_todas():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"l"})
    assert construir_palabra_oculta(estado) == "_ _ _ _ _ l l _"

def test_palabra_completa_revelada():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas=set("castillo"))
    assert construir_palabra_oculta(estado) == "c a s t i l l o"

def test_devuelve_string():
    estado = EstadoPartida(palabra_secreta="rey", categoria="personajes", dificultad="facil")
    assert isinstance(construir_palabra_oculta(estado), str)