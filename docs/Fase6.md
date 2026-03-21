# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 6 — Tests con pytest y pytest-cov
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Este documento recoge el proceso de asistencia con IA para implementar
los tests del proyecto con `pytest` y cobertura con `pytest-cov`.
Los tests cubren todos los módulos con lógica testeable del proyecto
antes de proceder a la refactorización modular por función.

---

## INTERACCIÓN 1 — Decisión de estrategia de testing

### 🔵 S — Situación

Con el juego completo y funcionando se planteó continuar con dos tareas
pendientes: tests del proyecto y refactorización de módulos en archivos
individuales por función/clase.

### 🔴 P — Problema

Sin tests no hay forma de saber si algo se rompe durante la refactorización.
Era necesario decidir el orden correcto de ambas tareas.

### 🟠 E — Exploración

**Prompt enviado:**

> *"podemos pasar a los test pero quiero test de todo el proyecto no quiero
> dejar nada a la suerte. usemos pytest y pytest --cov"*

La IA explicó el razonamiento:

- **Tests primero** — se escriben sobre el código actual que funciona.
- **Refactorización después** — los tests actúan como red de seguridad,
  si algo se rompe al separar archivos el test lo detecta inmediatamente.

### 🟢 C — Cambios

Se definió el alcance completo de los tests:

| Módulo | Estrategia |
|---|---|
| `validaciones/letra.py` | Tests unitarios puros |
| `validaciones/palabra.py` | Tests unitarios puros |
| `juego/estado.py` | Tests unitarios puros |
| `juego/logica.py` | Tests unitarios puros |
| `base_datos/conexion.py` | BD de prueba separada |
| `base_datos/inicializar.py` | BD de prueba separada |
| `base_datos/consultas.py` | BD de prueba separada |
| `base_datos/insercion.py` | BD de prueba separada |
| `interfaz/pantalla.py` | Tests de cadenas generadas |
| `interfaz/menu.py` | ⏳ Mock de `input()` — fase posterior |
| `juego/bucle.py` | ⏳ Mock de `input()` — fase posterior |
| `interfaz/dibujo.py` | Sin lógica, no se testea |
| `ahorcado.py` | Sin lógica, no se testea |

### 🔵 A — Acuerdo

✅ Tests antes de refactorización.  
✅ `pytest` + `pytest-cov` ya instalados.  
✅ Base de datos de prueba separada para tests de `base_datos/`.  
✅ `conftest.py` con fixtures compartidos.  
✅ Casos edge incluidos en todos los módulos.  
❌ `menu.py` y `bucle.py` quedan fuera de esta fase (requieren mock de `input()`).

### 🟢 R — Resultado

Plan de tests definido. Estructura de la carpeta `tests/`:

```
tests/
├── __init__.py
├── conftest.py
├── test_validaciones_letra.py
├── test_validaciones_palabra.py
├── test_juego_estado.py
├── test_juego_logica.py
├── test_base_datos_conexion.py
├── test_base_datos_inicializar.py
├── test_base_datos_consultas.py
├── test_base_datos_insercion.py
├── test_interfaz_pantalla.py
└── test_cobertura_completa.py
```

---

## INTERACCIÓN 2 — Corrección de ModuleNotFoundError en pytest

### 🔵 S — Situación

Al ejecutar `pytest` por primera vez apareció el error:

```
ImportError while loading conftest 'tests\conftest.py'
ModuleNotFoundError: No module named 'src'
```

### 🔴 P — Problema

Pytest no sabía dónde estaba la raíz del proyecto y no podía resolver
los imports con prefijo `src.`.

### 🟠 E — Exploración

La IA propuso añadir un archivo `pytest.ini` en la raíz del proyecto
con la línea `pythonpath = .` para que pytest trate la raíz como punto
de partida de los imports, igual que cuando se ejecuta `python ahorcado.py`.

### 🟢 C — Cambios

Archivo `pytest.ini` añadido en la raíz:

```ini
[pytest]
testpaths = tests
pythonpath = .
```

### 🔵 A — Acuerdo

✅ `pytest.ini` en la raíz del proyecto.  
✅ `pythonpath = .` resuelve los imports con `src.`.

### 🟢 R — Resultado

Pytest arranca correctamente y detecta los 148 tests iniciales.

---

## INTERACCIÓN 3 — Primera ejecución: 148 passed, 96% cobertura

### 🔵 S — Situación

Con `pytest.ini` correcto se ejecutaron todos los tests por primera vez.

### 🔴 P — Problema

La cobertura llegó al 96% pero quedaron 4 módulos sin cubrir al 100%:

| Módulo | Cobertura | Líneas faltantes |
|---|---|---|
| `base_datos/insercion.py` | 64% | Ramas `except`, `_normalizar_dificultad()` |
| `base_datos/consultas.py` | 79% | Ramas `except` de las 3 funciones |
| `base_datos/inicializar.py` | 88% | Rama `except` |
| `interfaz/pantalla.py` | 79% | `mostrar_escena()` completa, `ValueError` |
| `validaciones/letra.py` | 92% | `_normalizar_caracter()` |

### 🟠 E — Exploración

**Prompt enviado:**

> *"si"*

La IA identificó que las líneas sin cubrir eran principalmente:
- Ramas `except sqlite3.Error` que requieren simular fallos de BD con `monkeypatch`
- Funciones privadas que no se llamaban desde ningún test
- El `ValueError` de `mostrar_escena()` con valores fuera de rango

### 🟢 C — Cambios

Se creó `test_cobertura_completa.py` con 18 tests adicionales usando
`monkeypatch` para simular errores de SQLite y cubrir todas las ramas
faltantes.

### 🔵 A — Acuerdo

✅ `monkeypatch` para simular errores de BD sin tocar el código de producción.  
✅ Tests de `ValueError` con `pytest.raises()`.  
✅ Tests directos sobre funciones privadas `_normalizar_caracter()` y `_normalizar_dificultad()`.

### 🟢 R — Resultado

166 tests, 100% de cobertura en todos los módulos.

---

## INTERACCIÓN 4 — Corrección de warnings de Ruff

### 🔵 S — Situación

Tras pasar al 100% de cobertura, Ruff reportó 12 advertencias en los
archivos de test.

### 🔴 P — Problema

Dos tipos de advertencias:

- **F401** — `import pytest` no usado en 6 archivos de test (los fixtures
  de `conftest.py` no requieren importar `pytest` explícitamente).
- **F401** — `unittest.mock.patch` y `MagicMock` importados pero no usados
  en `test_cobertura_completa.py` (se usó `monkeypatch` en su lugar).
- **E402** — imports no al inicio del archivo en `test_cobertura_completa.py`
  porque estaban organizados por secciones dentro del archivo.

### 🟠 E — Exploración

**Prompt enviado:**

> *(imagen con los 12 warnings de Ruff)*

### 🟢 C — Cambios

- Eliminado `import pytest` de los 6 archivos donde no se usaba.
- Eliminados `from unittest.mock import patch, MagicMock` de `test_cobertura_completa.py`.
- Todos los imports de `test_cobertura_completa.py` movidos al inicio del archivo.

### 🔵 A — Acuerdo

✅ Imports limpios en todos los archivos de test.  
✅ Sin advertencias de Ruff.

### 🟢 R — Resultado

**166 passed — 100% cobertura — 0 warnings de Ruff.**

```
Name                              Stmts   Miss  Cover
-----------------------------------------------------
src\base_datos\conexion.py            9      0   100%
src\base_datos\consultas.py          43      0   100%
src\base_datos\inicializar.py        16      0   100%
src\base_datos\insercion.py          28      0   100%
src\interfaz\dibujo.py                2      0   100%
src\interfaz\pantalla.py             34      0   100%
src\juego\estado.py                  23      0   100%
src\juego\logica.py                  13      0   100%
src\validaciones\letra.py            13      0   100%
src\validaciones\palabra.py          38      0   100%
-----------------------------------------------------
TOTAL                               750      0   100%
```

---

## Catálogo de tests — Fase 6

### `tests/conftest.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `bd_prueba` | fixture | BD SQLite temporal con `monkeypatch` sobre `RUTA_BASE_DATOS` |
| `estado_inicial` | fixture | `EstadoPartida` limpio con la palabra `castillo` |
| `estado_con_letras` | fixture | `EstadoPartida` con `c`, `a` correctas y `x`, `z` fallidas |

---

### `tests/test_validaciones_letra.py` — 17 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_letra_minuscula_valida` | normal | Letra minúscula devuelve `None` |
| `test_letra_mayuscula_valida` | normal | Mayúscula se acepta |
| `test_letra_con_tilde_valida` | normal | Letra con tilde es válida |
| `test_tilde_mayuscula_valida` | normal | Tilde en mayúscula es válida |
| `test_enie_minuscula_valida` | normal | `ñ` es válida |
| `test_enie_mayuscula_valida` | normal | `Ñ` es válida |
| `test_entrada_vacia_devuelve_error` | inválido | Cadena vacía devuelve error |
| `test_varias_letras_devuelve_error` | inválido | Más de una letra devuelve error |
| `test_numero_devuelve_error` | inválido | Número devuelve error |
| `test_simbolo_devuelve_error` | inválido | Símbolo devuelve error |
| `test_espacio_devuelve_error` | inválido | Espacio devuelve error |
| `test_espacios_en_blanco_devuelve_error` | edge | Varios espacios devuelven error |
| `test_salto_de_linea_devuelve_error` | edge | `\n` devuelve error |
| `test_tabulacion_devuelve_error` | edge | `\t` devuelve error |
| `test_letra_mas_espacio_devuelve_error` | edge | Letra + espacio devuelve error |
| `test_mensaje_error_es_string` | tipo | El error devuelto es `str` |
| `test_letra_valida_devuelve_none` | tipo | Letra válida devuelve `None`, no `str` |

---

### `tests/test_validaciones_palabra.py` — 31 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_palabra_valida` | normal | Palabra correcta devuelve `None` |
| `test_palabra_con_tilde_valida` | normal | Tilde en palabra es válida |
| `test_palabra_con_enie_valida` | normal | `ñ` en palabra es válida |
| `test_palabra_longitud_minima_exacta` | límite | 3 letras exactas es válido |
| `test_palabra_longitud_maxima_exacta` | límite | 30 letras exactas es válido |
| `test_palabra_vacia_devuelve_error` | inválido | Cadena vacía devuelve error |
| `test_palabra_muy_corta_devuelve_error` | inválido | 2 letras devuelve error |
| `test_palabra_muy_larga_devuelve_error` | inválido | 31 letras devuelve error |
| `test_palabra_con_numero_devuelve_error` | inválido | Número en palabra devuelve error |
| `test_palabra_con_espacio_devuelve_error` | inválido | Espacio interno devuelve error |
| `test_palabra_con_guion_devuelve_error` | inválido | Guión devuelve error |
| `test_palabra_con_simbolo_devuelve_error` | inválido | `@` devuelve error |
| `test_palabra_solo_espacios_devuelve_error` | edge | Solo espacios devuelve error |
| `test_palabra_con_espacios_extremos_valida` | edge | `strip()` elimina espacios y valida |
| `test_palabra_mayusculas_valida` | edge | Mayúsculas son válidas |
| `test_categoria_animales_valida` | normal | `animales` es válida |
| `test_categoria_armas_valida` | normal | `armas` es válida |
| `test_categoria_lugares_valida` | normal | `lugares` es válida |
| `test_categoria_personajes_valida` | normal | `personajes` es válida |
| `test_categoria_mayusculas_valida` | edge | `ANIMALES` se normaliza y es válida |
| `test_categoria_invalida_devuelve_error` | inválido | Categoría desconocida devuelve error |
| `test_categoria_vacia_devuelve_error` | inválido | Vacía devuelve error |
| `test_categoria_con_espacios_invalida` | edge | Solo espacios devuelve error |
| `test_dificultad_facil_valida` | normal | `facil` es válida |
| `test_dificultad_medio_valida` | normal | `medio` es válida |
| `test_dificultad_dificil_valida` | normal | `dificil` es válida |
| `test_dificultad_mayusculas_valida` | edge | `FACIL` se normaliza y es válida |
| `test_dificultad_invalida_devuelve_error` | inválido | Valor desconocido devuelve error |
| `test_dificultad_vacia_devuelve_error` | inválido | Vacía devuelve error |
| `test_dificultad_con_tilde_devuelve_error` | edge | `difícil` con tilde devuelve error |
| `test_mensaje_error_es_string` | tipo | Error devuelto es `str` |

---

### `tests/test_juego_estado.py` — 26 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_crear_estado_inicial_palabra` | normal | Palabra correcta en el estado |
| `test_crear_estado_inicial_categoria` | normal | Categoría correcta |
| `test_crear_estado_inicial_dificultad` | normal | Dificultad correcta |
| `test_crear_estado_inicial_sin_letras_correctas` | normal | Set vacío al inicio |
| `test_crear_estado_inicial_sin_letras_fallidas` | normal | Set vacío al inicio |
| `test_crear_estado_inicial_cero_fallos` | normal | Cero fallos al inicio |
| `test_crear_estado_desde_registro` | normal | Crea desde dict de BD |
| `test_palabra_oculta_sin_letras` | normal | Solo guiones sin letras |
| `test_palabra_oculta_con_una_letra` | normal | Una letra revelada |
| `test_palabra_oculta_letras_repetidas` | edge | `l` revela las dos `l` de castillo |
| `test_palabra_oculta_completa` | normal | Palabra completa revelada |
| `test_palabra_oculta_es_string` | tipo | Devuelve `str` |
| `test_registrar_letra_correcta_va_a_correctas` | normal | Letra correcta al set correcto |
| `test_registrar_letra_correcta_no_suma_fallo` | normal | No suma fallo |
| `test_registrar_letra_fallida_va_a_fallidas` | normal | Letra fallida al set correcto |
| `test_registrar_letra_fallida_suma_un_fallo` | normal | Suma 1 fallo |
| `test_registrar_misma_letra_correcta_dos_veces` | edge | Set no duplica |
| `test_registrar_misma_letra_fallida_dos_veces` | edge | Fallo se suma dos veces |
| `test_registrar_letra_devuelve_estado` | tipo | Devuelve `EstadoPartida` |
| `test_registrar_letra_normaliza_mayuscula` | edge | `C` se guarda como `c` |
| `test_letra_ya_usada_en_correctas` | normal | Letra acertada devuelve `True` |
| `test_letra_ya_usada_en_fallidas` | normal | Letra fallida devuelve `True` |
| `test_letra_no_usada_devuelve_false` | normal | Letra nueva devuelve `False` |
| `test_letra_ya_usada_mayuscula` | edge | Mayúscula detectada como usada |
| `test_letras_usadas_sin_letras` | normal | Lista vacía sin letras |
| `test_letras_usadas_combina_correctas_y_fallidas` | normal | Combina ambos sets |
| `test_letras_usadas_ordenadas_alfabeticamente` | normal | Lista ordenada |
| `test_letras_usadas_devuelve_lista` | tipo | Devuelve `list` |

---

### `tests/test_juego_logica.py` — 21 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_hay_victoria_todas_las_letras` | normal | Victoria con todas adivinadas |
| `test_hay_victoria_false_sin_letras` | normal | Sin letras no hay victoria |
| `test_hay_victoria_false_letras_parciales` | normal | Parciales no dan victoria |
| `test_hay_victoria_letras_repetidas` | edge | Letra repetida cuenta una vez |
| `test_hay_derrota_false_cero_fallos` | normal | Sin fallos no hay derrota |
| `test_hay_derrota_false_cinco_fallos` | límite | 5 fallos no es derrota |
| `test_hay_derrota_true_seis_fallos` | límite | 6 fallos exactos es derrota |
| `test_hay_derrota_true_supera_maximo` | edge | Más de 6 también es derrota |
| `test_letra_en_palabra_true` | normal | Letra presente devuelve `True` |
| `test_letra_en_palabra_false` | normal | Letra ausente devuelve `False` |
| `test_letra_en_palabra_mayuscula` | edge | Mayúscula se normaliza |
| `test_letra_en_palabra_tilde` | edge | Tilde no coincide sin tilde |
| `test_letra_en_palabra_repetida` | edge | Letra repetida devuelve `True` |
| `test_intentos_restantes_cero_fallos` | normal | 6 intentos al inicio |
| `test_intentos_restantes_tres_fallos` | normal | 3 intentos con 3 fallos |
| `test_intentos_restantes_derrota` | límite | 0 intentos en derrota |
| `test_intentos_restantes_devuelve_entero` | tipo | Devuelve `int` |
| `test_partida_no_terminada` | normal | Sin condición no termina |
| `test_partida_terminada_por_victoria` | normal | Victoria termina |
| `test_partida_terminada_por_derrota` | normal | Derrota termina |
| `test_partida_terminada_victoria_con_fallos` | edge | Victoria con fallos también termina |

---

### `tests/test_base_datos_conexion.py` — 3 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_obtener_conexion_devuelve_connection` | normal | Devuelve `sqlite3.Connection` |
| `test_conexion_tiene_row_factory` | normal | `row_factory` es `sqlite3.Row` |
| `test_conexion_es_funcional` | normal | Ejecuta `SELECT 1` correctamente |

---

### `tests/test_base_datos_inicializar.py` — 4 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_tabla_creada_tras_inicializar` | normal | Tabla `palabras` existe |
| `test_palabras_iniciales_insertadas` | normal | Al menos 20 palabras |
| `test_inicializar_es_idempotente` | edge | Doble inicialización no duplica |
| `test_palabras_tienen_todos_los_campos` | normal | Campos `palabra`, `categoria`, `dificultad` presentes |

---

### `tests/test_base_datos_consultas.py` — 16 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_obtener_palabra_aleatoria_devuelve_dict` | normal | Devuelve `dict` |
| `test_obtener_palabra_aleatoria_tiene_claves` | normal | Claves esperadas presentes |
| `test_obtener_palabra_por_categoria` | normal | Filtro de categoría funciona |
| `test_obtener_palabra_categoria_inexistente` | edge | Sin palabras devuelve `None` |
| `test_obtener_palabra_bd_vacia` | edge | BD vacía devuelve `None` |
| `test_obtener_palabra_por_dificultad` | normal | Filtro de dificultad funciona |
| `test_obtener_palabra_filtros_combinados` | normal | Categoría + dificultad combinados |
| `test_obtener_todas_devuelve_lista` | normal | Devuelve `list` |
| `test_obtener_todas_no_vacia` | normal | Lista con elementos |
| `test_obtener_todas_cada_elemento_es_dict` | tipo | Cada elemento es `dict` |
| `test_obtener_todas_ordenadas_por_categoria` | normal | Orden por categoría |
| `test_obtener_todas_bd_vacia` | edge | BD vacía devuelve `[]` |
| `test_obtener_categorias_devuelve_lista` | normal | Devuelve `list` |
| `test_obtener_categorias_tiene_claves` | normal | Claves `categoria` y `total` |
| `test_obtener_categorias_total_es_entero` | tipo | `total` es `int` |
| `test_obtener_categorias_bd_vacia` | edge | BD vacía devuelve `[]` |

---

### `tests/test_base_datos_insercion.py` — 12 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_insertar_palabra_nueva_devuelve_true` | normal | Inserción devuelve `True` |
| `test_insertar_palabra_nueva_existe_en_bd` | normal | Palabra guardada en BD |
| `test_insertar_palabra_duplicada_devuelve_false` | normal | Duplicado devuelve `False` |
| `test_insertar_normaliza_mayusculas` | edge | `DRAGON` se guarda como `dragon` |
| `test_insertar_mayuscula_duplica_minuscula` | edge | `DRAGON` duplica `dragon` |
| `test_insertar_con_espacios_extremos` | edge | `  pegaso  ` se guarda como `pegaso` |
| `test_no_duplica_con_distinta_capitalizacion` | edge | Capitalización diferente es duplicado |
| `test_palabra_ya_existe_true` | normal | Palabra existente devuelve `True` |
| `test_palabra_ya_existe_false` | normal | Palabra inexistente devuelve `False` |
| `test_palabra_ya_existe_mayuscula` | edge | Mayúscula detecta existente |
| `test_palabra_ya_existe_con_espacios` | edge | Espacios se ignoran en búsqueda |
| `test_palabra_ya_existe_devuelve_bool` | tipo | Devuelve `bool` |

---

### `tests/test_interfaz_pantalla.py` — 16 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_cabecera_contiene_titulo` | normal | Contiene "AHORCADO MEDIEVAL" |
| `test_cabecera_contiene_palabra_oculta` | normal | Muestra la palabra |
| `test_cabecera_sin_letras_muestra_ninguna` | normal | Sin letras muestra "ninguna" |
| `test_cabecera_con_letras_las_muestra` | normal | Letras en mayúsculas visibles |
| `test_cabecera_devuelve_string` | tipo | Devuelve `str` |
| `test_cabecera_tiene_bordes` | normal | Contiene `╔` y `╚` |
| `test_formatear_letras_vacia` | normal | Lista vacía devuelve "ninguna" |
| `test_formatear_letras_en_mayusculas` | normal | Letras en mayúsculas |
| `test_formatear_letras_separadas_por_coma` | normal | Separadas por coma |
| `test_formatear_letras_devuelve_string` | tipo | Devuelve `str` |
| `test_etiqueta_cero_fallos` | normal | Muestra "Sin fallos" |
| `test_etiqueta_fallos_maximos` | límite | Muestra "intentos" |
| `test_etiqueta_fallos_intermedios` | normal | Muestra número de fallos |
| `test_etiqueta_devuelve_string` | tipo | Devuelve `str` |
| `test_mostrar_mensaje_no_lanza_excepcion` | normal | Texto visible en salida |
| `test_mostrar_error_incluye_simbolo` | normal | Contiene `⚠` |

---

### `tests/test_cobertura_completa.py` — 18 tests

| Test | Tipo | Descripción |
|---|---|---|
| `test_normalizar_dificultad_valida` | normal | Valores válidos devuelven la dificultad |
| `test_normalizar_dificultad_invalida` | inválido | Valor desconocido devuelve `None` |
| `test_normalizar_dificultad_mayusculas` | edge | Mayúsculas se normalizan |
| `test_normalizar_dificultad_con_espacios` | edge | Espacios se eliminan |
| `test_insertar_palabra_error_bd` | error | `sqlite3.Error` devuelve `False` |
| `test_palabra_ya_existe_error_bd` | error | `sqlite3.Error` devuelve `False` |
| `test_obtener_palabra_aleatoria_error_bd` | error | `sqlite3.Error` devuelve `None` |
| `test_obtener_todas_error_bd` | error | `sqlite3.Error` devuelve `[]` |
| `test_obtener_categorias_error_bd` | error | `sqlite3.Error` devuelve `[]` |
| `test_inicializar_error_bd` | error | `sqlite3.Error` no lanza excepción |
| `test_mostrar_escena_valor_invalido` | edge | `numero_fallos=7` lanza `ValueError` |
| `test_mostrar_escena_negativo` | edge | `numero_fallos=-1` lanza `ValueError` |
| `test_mostrar_escena_estado_cero` | normal | Estado 0 renderiza correctamente |
| `test_mostrar_escena_estado_seis` | normal | Estado 6 renderiza correctamente |
| `test_normalizar_caracter_sin_tilde` | normal | Sin tilde devuelve igual |
| `test_normalizar_caracter_con_tilde` | normal | `á` devuelve `a` |
| `test_normalizar_caracter_e_tilde` | normal | `é` devuelve `e` |
| `test_normalizar_caracter_mayuscula_tilde` | edge | `Á` devuelve `a` |

---

## Resumen de decisiones — Fase 6

| Elemento | Propuesto | Decisión |
|---|---|---|
| BD para tests | BD real `palabras.db` | ✅ BD de prueba separada con `tmp_path` |
| Fixtures | Inline en cada test | ✅ `conftest.py` compartido |
| Orden | Tests después de refactorizar | ✅ Tests antes de refactorizar |
| `menu.py` y `bucle.py` | Incluir en esta fase | ⏳ Fase posterior con mocks |
| `dibujo.py` y `ahorcado.py` | Incluir en esta fase | ❌ Sin lógica testeable |
| Cobertura inicial | — | 96% en primera ejecución |
| Cobertura final | 96% | ✅ 100% tras `test_cobertura_completa.py` |
| `pytest.ini` | No existía | ✅ Añadido con `pythonpath = .` |
| Imports no usados (Ruff F401) | Presentes | ✅ Eliminados |
| Imports fuera de lugar (Ruff E402) | Presentes | ✅ Movidos al inicio |

---

## Resultado final

```
166 passed — 100% cobertura — 0 warnings de Ruff — 1.29s
```