"""
estado.py
=========
Módulo que define y gestiona el estado de una partida
del Ahorcado Medieval.

Responsabilidades:
    - Definir la estructura de datos de una partida activa.
    - Construir la representación visual de la palabra oculta.
    - Registrar letras usadas y actualizar el estado.

Importaciones necesarias:
    from src.juego.estado import EstadoPartida, crear_estado_inicial
"""

from dataclasses import dataclass, field


# ── Dataclass del estado ──────────────────────────────────────

@dataclass
class EstadoPartida:
    """
    Representa el estado completo de una partida activa.

    Attributes:
        palabra_secreta  (str):       La palabra a adivinar en minúsculas.
        categoria        (str):       Categoría de la palabra.
        dificultad       (str):       Dificultad de la palabra.
        letras_correctas (set[str]):  Letras acertadas hasta el momento.
        letras_fallidas  (set[str]):  Letras incorrectas hasta el momento.
        numero_fallos    (int):       Contador de fallos acumulados.
    """
    palabra_secreta:  str
    categoria:        str
    dificultad:       str
    letras_correctas: set[str] = field(default_factory=set)
    letras_fallidas:  set[str] = field(default_factory=set)
    numero_fallos:    int      = 0


# ── Funciones públicas ────────────────────────────────────────

def crear_estado_inicial(registro_palabra: dict) -> EstadoPartida:
    """
    Crea un estado de partida nuevo a partir de un registro
    de la base de datos.

    Args:
        registro_palabra (dict): Diccionario con las claves
                                 'palabra', 'categoria' y 'dificultad'
                                 tal como lo devuelve consultas.py.

    Returns:
        EstadoPartida: Estado inicial con sets vacíos y cero fallos.
    """
    return EstadoPartida(
        palabra_secreta = registro_palabra["palabra"],
        categoria       = registro_palabra["categoria"],
        dificultad      = registro_palabra["dificultad"],
    )


def construir_palabra_oculta(estado: EstadoPartida) -> str:
    """
    Construye la representación visual de la palabra oculta,
    revelando las letras acertadas y ocultando el resto con guiones.

    Ejemplo:
        palabra_secreta  = "castillo"
        letras_correctas = {"c", "a", "l"}
        resultado        = "c a _ _ i l l _"  ← espera, 'i' no está en correctas

        palabra_secreta  = "castillo"
        letras_correctas = {"c", "a", "l", "i"}
        resultado        = "c a _ _ i l l _"

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        str: Cadena con letras reveladas separadas por espacios.
             Las letras no adivinadas se muestran como guión bajo.
    """
    return " ".join(
        letra if letra in estado.letras_correctas else "_"
        for letra in estado.palabra_secreta
    )


def registrar_letra(estado: EstadoPartida, letra: str) -> EstadoPartida:
    """
    Registra una letra jugada actualizando el estado de la partida.

    Si la letra está en la palabra secreta se añade a letras_correctas.
    Si no está se añade a letras_fallidas y se incrementa numero_fallos.

    Args:
        estado (EstadoPartida): Estado actual de la partida.
        letra  (str):           Letra jugada en minúscula.

    Returns:
        EstadoPartida: El mismo estado mutado con la letra registrada.
    """
    letra_normalizada = letra.lower()

    if letra_normalizada in estado.palabra_secreta:
        estado.letras_correctas.add(letra_normalizada)
    else:
        estado.letras_fallidas.add(letra_normalizada)
        estado.numero_fallos += 1

    return estado


def letra_ya_usada(estado: EstadoPartida, letra: str) -> bool:
    """
    Comprueba si una letra ya fue jugada anteriormente,
    ya sea correcta o fallida.

    Args:
        estado (EstadoPartida): Estado actual de la partida.
        letra  (str):           Letra a comprobar.

    Returns:
        bool: True si la letra ya fue usada. False si es nueva.
    """
    letra_normalizada = letra.lower()
    return (
        letra_normalizada in estado.letras_correctas
        or letra_normalizada in estado.letras_fallidas
    )


def obtener_letras_usadas(estado: EstadoPartida) -> list[str]:
    """
    Devuelve todas las letras jugadas (correctas y fallidas)
    ordenadas alfabéticamente para mostrar en pantalla.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        list[str]: Lista ordenada de letras ya jugadas.
    """
    todas_las_letras = estado.letras_correctas | estado.letras_fallidas
    return sorted(todas_las_letras)