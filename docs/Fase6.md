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
└── test_interfaz_pantalla.py
```

---

## Catálogo de tests — Fase 6

### `tests/conftest.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `bd_prueba` | fixture | Crea una BD SQLite temporal con tabla y datos de prueba |
| `estado_inicial` | fixture | Crea un `EstadoPartida` limpio para tests de juego |
| `estado_con_letras` | fixture | Crea un `EstadoPartida` con letras ya jugadas |

---

### `tests/test_validaciones_letra.py`

| Test | Descripción |
|---|---|
| `test_letra_valida` | Una letra correcta devuelve `None` |
| `test_letra_vacia` | Cadena vacía devuelve error |
| `test_varias_letras` | Más de una letra devuelve error |
| `test_numero` | Un número devuelve error |
| `test_simbolo` | Un símbolo devuelve error |
| `test_letra_con_tilde` | Letra con tilde es válida |
| `test_enie` | La ñ es válida |
| `test_mayuscula` | Mayúscula se normaliza y es válida |

---

### `tests/test_validaciones_palabra.py`

| Test | Descripción |
|---|---|
| `test_palabra_valida` | Palabra correcta devuelve `None` |
| `test_palabra_vacia` | Cadena vacía devuelve error |
| `test_palabra_corta` | Menos de 3 letras devuelve error |
| `test_palabra_larga` | Más de 30 letras devuelve error |
| `test_palabra_con_numeros` | Números en la palabra devuelven error |
| `test_palabra_con_espacios` | Espacios en la palabra devuelven error |
| `test_categoria_valida` | Categoría correcta devuelve `None` |
| `test_categoria_invalida` | Categoría no permitida devuelve error |
| `test_dificultad_valida` | Dificultad correcta devuelve `None` |
| `test_dificultad_invalida` | Dificultad no permitida devuelve error |

---

### `tests/test_juego_estado.py`

| Test | Descripción |
|---|---|
| `test_crear_estado_inicial` | El estado se crea con sets vacíos y cero fallos |
| `test_construir_palabra_oculta_sin_letras` | Sin letras acertadas muestra solo guiones |
| `test_construir_palabra_oculta_con_letras` | Letras acertadas se revelan correctamente |
| `test_construir_palabra_oculta_completa` | Todas las letras acertadas muestra la palabra |
| `test_registrar_letra_correcta` | Letra correcta va a `letras_correctas` y no suma fallo |
| `test_registrar_letra_fallida` | Letra fallida va a `letras_fallidas` y suma un fallo |
| `test_letra_ya_usada_correcta` | Letra ya acertada devuelve `True` |
| `test_letra_ya_usada_fallida` | Letra ya fallada devuelve `True` |
| `test_letra_no_usada` | Letra nueva devuelve `False` |
| `test_obtener_letras_usadas_ordenadas` | Lista combinada y ordenada alfabéticamente |

---

### `tests/test_juego_logica.py`

| Test | Descripción |
|---|---|
| `test_hay_victoria_true` | Todas las letras adivinadas devuelve `True` |
| `test_hay_victoria_false` | Letras pendientes devuelve `False` |
| `test_hay_derrota_true` | Fallos iguales al máximo devuelve `True` |
| `test_hay_derrota_false` | Fallos menores al máximo devuelve `False` |
| `test_letra_en_palabra_true` | Letra presente devuelve `True` |
| `test_letra_en_palabra_false` | Letra ausente devuelve `False` |
| `test_intentos_restantes` | Calcula correctamente los intentos restantes |
| `test_partida_terminada_victoria` | Victoria termina la partida |
| `test_partida_terminada_derrota` | Derrota termina la partida |
| `test_partida_no_terminada` | Sin victoria ni derrota devuelve `False` |

---

### `tests/test_base_datos_conexion.py`

| Test | Descripción |
|---|---|
| `test_obtener_conexion_devuelve_conexion` | La función devuelve un objeto `Connection` |
| `test_conexion_tiene_row_factory` | `row_factory` está configurado como `sqlite3.Row` |

---

### `tests/test_base_datos_inicializar.py`

| Test | Descripción |
|---|---|
| `test_tabla_creada` | La tabla `palabras` existe tras inicializar |
| `test_palabras_iniciales_insertadas` | Hay al menos 20 palabras tras inicializar |
| `test_idempotente` | Inicializar dos veces no duplica registros |

---

### `tests/test_base_datos_consultas.py`

| Test | Descripción |
|---|---|
| `test_obtener_palabra_aleatoria` | Devuelve un diccionario con las claves esperadas |
| `test_obtener_palabra_por_categoria` | El filtro de categoría funciona correctamente |
| `test_obtener_palabra_categoria_inexistente` | Categoría sin palabras devuelve `None` |
| `test_obtener_todas_las_palabras` | Devuelve lista con todas las palabras |
| `test_obtener_todas_ordenadas` | La lista viene ordenada por categoría |
| `test_obtener_categorias` | Devuelve lista de categorías con su conteo |

---

### `tests/test_base_datos_insercion.py`

| Test | Descripción |
|---|---|
| `test_insertar_palabra_nueva` | Palabra nueva se inserta y devuelve `True` |
| `test_insertar_palabra_duplicada` | Palabra ya existente devuelve `False` |
| `test_insertar_normaliza_mayusculas` | La palabra se guarda en minúsculas |
| `test_palabra_ya_existe_true` | Palabra existente devuelve `True` |
| `test_palabra_ya_existe_false` | Palabra inexistente devuelve `False` |

---

### `tests/test_interfaz_pantalla.py`

| Test | Descripción |
|---|---|
| `test_construir_cabecera_contiene_palabra` | La cabecera incluye la palabra oculta |
| `test_construir_cabecera_sin_letras` | Sin letras usadas muestra "ninguna" |
| `test_construir_cabecera_con_letras` | Letras usadas aparecen en la cabecera |
| `test_formatear_letras_usadas_vacia` | Lista vacía devuelve "ninguna" |
| `test_formatear_letras_usadas_orden` | Las letras aparecen en mayúsculas |
| `test_construir_etiqueta_cero_fallos` | Estado 0 muestra "Sin fallos aún" |
| `test_construir_etiqueta_fallos_maximos` | Estado 6 muestra "Sin más intentos" |

---

## Resumen de decisiones — Fase 6

| Elemento | Propuesto | Decisión |
|---|---|---|
| BD para tests | BD real `palabras.db` | ✅ BD de prueba separada |
| Fixtures | Inline en cada test | ✅ `conftest.py` compartido |
| Orden | Tests después de refactorizar | ✅ Tests antes de refactorizar |
| `menu.py` y `bucle.py` | Incluir en esta fase | ⏳ Fase posterior con mocks |
| `dibujo.py` y `ahorcado.py` | Incluir en esta fase | ❌ Sin lógica testeable |