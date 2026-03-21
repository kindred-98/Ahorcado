"""
clase_estado_partida.py
=======================
Dataclass que representa el estado completo de una partida.
"""

from dataclasses import dataclass, field


@dataclass
class EstadoPartida:
    """
    Representa el estado completo de una partida activa.

    Attributes:
        palabra_secreta  (str):      La palabra a adivinar en minúsculas.
        categoria        (str):      Categoría de la palabra.
        dificultad       (str):      Dificultad de la palabra.
        letras_correctas (set[str]): Letras acertadas hasta el momento.
        letras_fallidas  (set[str]): Letras incorrectas hasta el momento.
        numero_fallos    (int):      Contador de fallos acumulados.
    """
    palabra_secreta:  str
    categoria:        str
    dificultad:       str
    letras_correctas: set[str] = field(default_factory=set)
    letras_fallidas:  set[str] = field(default_factory=set)
    numero_fallos:    int      = 0