"""
palabra.py
==========
Módulo encargado de validar una nueva palabra antes de
insertarla en la base de datos del Ahorcado Medieval.

Responsabilidades:
    - Verificar que la palabra no esté vacía.
    - Verificar que solo contenga letras del alfabeto español.
    - Verificar que tenga una longitud mínima y máxima razonable.
    - Verificar que la categoría y dificultad sean valores válidos.

Importaciones necesarias:
    from src.validaciones.palabra import validar_palabra, validar_categoria, validar_dificultad
"""


# ── Constantes ────────────────────────────────────────────────

LONGITUD_MINIMA_PALABRA:  int = 3
LONGITUD_MAXIMA_PALABRA:  int = 30

CATEGORIAS_VALIDAS: frozenset[str] = frozenset({
    "animales",
    "armas",
    "lugares",
    "personajes",
})

DIFICULTADES_VALIDAS: frozenset[str] = frozenset({
    "facil",
    "medio",
    "dificil",
})

CARACTERES_VALIDOS_PALABRA: frozenset[str] = frozenset(
    "abcdefghijklmnñopqrstuvwxyzáéíóúü"
)


# ── Funciones públicas ────────────────────────────────────────

def validar_palabra(palabra: str) -> str | None:
    """
    Valida que una nueva palabra sea apta para insertarse
    en la base de datos.

    Comprueba longitud mínima, longitud máxima y que solo
    contenga letras del alfabeto español (sin números,
    espacios ni símbolos).

    Args:
        palabra (str): Palabra a validar (se evalúa en minúsculas).

    Returns:
        str | None: Mensaje de error si la palabra no es válida.
                    None si la palabra es correcta.

    Ejemplos:
        validar_palabra("dragon")     → None
        validar_palabra("ab")         → "La palabra debe tener al menos 3 letras."
        validar_palabra("dragon123")  → "La palabra solo puede contener letras."
        validar_palabra("")           → "La palabra no puede estar vacía."
    """
    palabra_normalizada = palabra.strip().lower()

    if not palabra_normalizada:
        return "La palabra no puede estar vacía."

    if len(palabra_normalizada) < LONGITUD_MINIMA_PALABRA:
        return (
            f"La palabra debe tener al menos "
            f"{LONGITUD_MINIMA_PALABRA} letras."
        )

    if len(palabra_normalizada) > LONGITUD_MAXIMA_PALABRA:
        return (
            f"La palabra no puede tener más de "
            f"{LONGITUD_MAXIMA_PALABRA} letras."
        )

    caracter_invalido = _buscar_caracter_invalido(palabra_normalizada)
    if caracter_invalido:
        return (
            f"La palabra solo puede contener letras. "
            f"Carácter no válido: '{caracter_invalido}'."
        )

    return None


def validar_categoria(categoria: str) -> str | None:
    """
    Valida que la categoría ingresada sea una de las
    categorías permitidas en la base de datos.

    Args:
        categoria (str): Categoría a validar.

    Returns:
        str | None: Mensaje de error si la categoría no es válida.
                    None si la categoría es correcta.

    Ejemplos:
        validar_categoria("animales")  → None
        validar_categoria("comida")    → "Categoría no válida. Elige entre: ..."
    """
    categoria_normalizada = categoria.strip().lower()

    if not categoria_normalizada:
        return "La categoría no puede estar vacía."

    if categoria_normalizada not in CATEGORIAS_VALIDAS:
        opciones = ", ".join(sorted(CATEGORIAS_VALIDAS))
        return f"Categoría no válida. Elige entre: {opciones}."

    return None


def validar_dificultad(dificultad: str) -> str | None:
    """
    Valida que la dificultad ingresada sea uno de los
    valores permitidos: facil, medio o dificil.

    Args:
        dificultad (str): Dificultad a validar.

    Returns:
        str | None: Mensaje de error si la dificultad no es válida.
                    None si la dificultad es correcta.

    Ejemplos:
        validar_dificultad("facil")    → None
        validar_dificultad("imposible") → "Dificultad no válida. Elige entre: ..."
    """
    dificultad_normalizada = dificultad.strip().lower()

    if not dificultad_normalizada:
        return "La dificultad no puede estar vacía."

    if dificultad_normalizada not in DIFICULTADES_VALIDAS:
        opciones = ", ".join(sorted(DIFICULTADES_VALIDAS))
        return f"Dificultad no válida. Elige entre: {opciones}."

    return None


# ── Función privada ───────────────────────────────────────────

def _buscar_caracter_invalido(palabra: str) -> str | None:
    """
    Recorre la palabra y devuelve el primer carácter que
    no pertenezca al alfabeto español permitido.

    Args:
        palabra (str): Palabra ya normalizada a minúsculas.

    Returns:
        str | None: El primer carácter inválido encontrado,
                    o None si todos son válidos.
    """
    for caracter in palabra:
        if caracter not in CARACTERES_VALIDOS_PALABRA:
            return caracter
    return None