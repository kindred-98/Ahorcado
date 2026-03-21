# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 7 — Refactorización modular
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Este documento recoge el proceso de refactorización del proyecto para
separar cada función y clase en su propio archivo independiente.
El objetivo es practicar importaciones explícitas y aplicar el principio
de responsabilidad única a nivel de archivo, no solo de módulo.

La refactorización se hace de adentro hacia afuera, empezando por los
módulos sin dependencias internas y terminando por los que dependen de
todo lo demás. Después de cada módulo se corren los tests para verificar
que nada se rompe.

---

## INTERACCIÓN 1 — Definición de la estrategia de refactorización

### 🔵 S — Situación

Con 166 tests pasando al 100% de cobertura, era el momento de refactorizar
el código para separar cada función en su propio archivo.

### 🔴 P — Problema

Los módulos actuales tenían varias funciones juntas en un solo archivo.
El objetivo era practicar importaciones explícitas y llevar el principio
de responsabilidad única al nivel más granular posible.

### 🟠 E — Exploración

**Prompt enviado:**

> *"si comencemos"*

La IA propuso el orden de refactorización de adentro hacia afuera:

```
1. validaciones/    ← sin dependencias internas
2. juego/estado/    ← solo dataclasses
3. juego/logica/    ← depende de estado e interfaz
4. base_datos/      ← de conexion hacia afuera
5. interfaz/        ← depende de dibujo
6. juego/bucle/     ← depende de casi todo
7. interfaz/menu/   ← depende de casi todo
```

### 🟢 C — Cambios

Se acordó aplicar la misma estructura a los tests en paralelo:
refactorizar un módulo de código, inmediatamente sus tests, correr
pytest, y si pasa todo seguir con el siguiente.

**Prompt enviado:**

> *"quiero aplicarlos a todo los modulos del proyecto.
> en la refactorizacion usar while True y simplificacion de funciones.
> yo creare una carpeta y dentro los archivos con los nombres."*

### 🔵 A — Acuerdo

✅ Un archivo por función/clase en código y en tests.  
✅ Refactorización en paralelo con sus tests.  
✅ `while True` en bucles de entrada de usuario.  
✅ Simplificación de funciones donde sea posible.  
✅ El alumno crea las carpetas y archivos vacíos.  
✅ Tests y código se actualizan en paralelo módulo por módulo.

### 🟢 R — Resultado

Estrategia definida. Flujo de trabajo establecido:
código → tests → `pytest tests/ -v` → siguiente módulo.

---

## INTERACCIÓN 2 — Refactorización de validaciones/letra/

### 🔵 S — Situación

Primer módulo a refactorizar por ser el más simple y sin dependencias
internas. `letra.py` tenía una constante, una función pública y una privada.

### 🔴 P — Problema

Todo en un solo archivo. Se necesitaba separar en archivos independientes
y actualizar todos los imports del proyecto que lo referenciaban.

### 🟠 E — Exploración

**Prompt enviado:**

> *"LISTO"* (carpetas y archivos vacíos creados)

### 🟢 C — Cambios

`src/validaciones/letra.py` → `src/validaciones/letra/`:

| Archivo nuevo | Contenido |
|---|---|
| `alfabeto.py` | Constante `ALFABETO_ESPAÑOL` |
| `validar_letra.py` | Función pública `validar_letra()` |
| `normalizar_caracter.py` | Función privada `_normalizar_caracter()` |

Tests refactorizados: `tests/test_validaciones_letra.py` →
`tests/validaciones/letra/`:

| Archivo nuevo | Contenido |
|---|---|
| `test_validar_letra.py` | 17 tests de `validar_letra()` |
| `test_normalizar_caracter.py` | 9 tests de `_normalizar_caracter()` |

**Imports actualizados:**
- `tests/test_validaciones_letra.py` — import corregido a ruta específica
- `tests/test_cobertura_completa.py` — `_normalizar_caracter` actualizado

### 🔵 A — Acuerdo

✅ Separación en 3 archivos.  
✅ Tests separados en 2 archivos.  
✅ `test_validaciones_letra.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `validaciones/letra/` refactorizado.

---

## INTERACCIÓN 3 — Refactorización de validaciones/palabra/

### 🔵 S — Situación

Segundo módulo. `palabra.py` tenía 3 funciones públicas, 1 privada
y 4 constantes.

### 🔴 P — Problema

Todo en un solo archivo. Las constantes eran compartidas por las 3
funciones públicas, lo que requería un archivo de constantes común.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/validaciones/palabra.py` → `src/validaciones/palabra/`:

| Archivo nuevo | Contenido |
|---|---|
| `constantes.py` | Las 4 constantes compartidas |
| `buscar_caracter_invalido.py` | Función privada `_buscar_caracter_invalido()` |
| `validar_palabra.py` | Función pública `validar_palabra()` |
| `validar_categoria.py` | Función pública `validar_categoria()` |
| `validar_dificultad.py` | Función pública `validar_dificultad()` |

Tests refactorizados en `tests/validaciones/palabra/`:

| Archivo nuevo | Contenido |
|---|---|
| `test_validar_palabra.py` | 16 tests |
| `test_validar_categoria.py` | 8 tests |
| `test_validar_dificultad.py` | 7 tests |

**Imports actualizados en `menu.py`:**

```python
# antes
from src.validaciones.palabra import validar_palabra, validar_categoria, validar_dificultad

# después
from src.validaciones.palabra.validar_palabra    import validar_palabra
from src.validaciones.palabra.validar_categoria  import validar_categoria
from src.validaciones.palabra.validar_dificultad import validar_dificultad
```

### 🔵 A — Acuerdo

✅ 5 archivos de código + 3 de tests.  
✅ `constantes.py` como archivo compartido por las 3 funciones.  
✅ `test_validaciones_palabra.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `validaciones/palabra/` refactorizado.

---

## INTERACCIÓN 4 — Refactorización de juego/estado/

### 🔵 S — Situación

Tercer módulo. `estado.py` tenía 1 dataclass y 5 funciones públicas.
Era el módulo más importante porque todos los demás de `juego/` dependen de él.

### 🔴 P — Problema

Al convertir `estado.py` en carpeta, todos los módulos que importaban
`EstadoPartida` dejaban de funcionar: `logica.py`, `bucle.py`,
`conftest.py` y `test_juego_logica.py`.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/juego/estado.py` → `src/juego/estado/`:

| Archivo nuevo | Contenido |
|---|---|
| `clase_estado_partida.py` | Dataclass `EstadoPartida` |
| `crear_estado_inicial.py` | Función `crear_estado_inicial()` |
| `construir_palabra_oculta.py` | Función `construir_palabra_oculta()` |
| `registrar_letra.py` | Función `registrar_letra()` |
| `letra_ya_usada.py` | Función `letra_ya_usada()` |
| `obtener_letras_usadas.py` | Función `obtener_letras_usadas()` |

Tests refactorizados en `tests/juego/estado/`:

| Archivo nuevo | Contenido |
|---|---|
| `test_clase_estado_partida.py` | 7 tests |
| `test_crear_estado_inicial.py` | 7 tests |
| `test_construir_palabra_oculta.py` | 5 tests |
| `test_registrar_letra.py` | 7 tests |
| `test_letra_ya_usada.py` | 5 tests |
| `test_obtener_letras_usadas.py` | 5 tests |

**Imports actualizados:**

| Archivo | Import anterior | Import corregido |
|---|---|---|
| `conftest.py` | `from src.juego.estado import EstadoPartida` | `from src.juego.estado.clase_estado_partida import EstadoPartida` |
| `test_juego_logica.py` | `from src.juego.estado import EstadoPartida` | `from src.juego.estado.clase_estado_partida import EstadoPartida` |
| `src/juego/logica.py` | `from src.juego.estado import EstadoPartida` | `from src.juego.estado.clase_estado_partida import EstadoPartida` |
| `src/juego/bucle.py` | imports múltiples de `src.juego.estado` | imports individuales por archivo |

### 🔵 A — Acuerdo

✅ 6 archivos de código + 6 de tests.  
✅ `test_juego_estado.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `juego/estado/` refactorizado.

---

## Catálogo de archivos refactorizados hasta ahora

### `src/validaciones/letra/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `alfabeto.py` | `ALFABETO_ESPAÑOL` | constante |
| `validar_letra.py` | `validar_letra()` | pública |
| `normalizar_caracter.py` | `_normalizar_caracter()` | privada |

---

### `src/validaciones/palabra/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `constantes.py` | `LONGITUD_MINIMA_PALABRA`, `LONGITUD_MAXIMA_PALABRA`, `CATEGORIAS_VALIDAS`, `DIFICULTADES_VALIDAS`, `CARACTERES_VALIDOS_PALABRA` | constantes |
| `buscar_caracter_invalido.py` | `_buscar_caracter_invalido()` | privada |
| `validar_palabra.py` | `validar_palabra()` | pública |
| `validar_categoria.py` | `validar_categoria()` | pública |
| `validar_dificultad.py` | `validar_dificultad()` | pública |

---

### `src/juego/estado/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `clase_estado_partida.py` | `EstadoPartida` | clase |
| `crear_estado_inicial.py` | `crear_estado_inicial()` | pública |
| `construir_palabra_oculta.py` | `construir_palabra_oculta()` | pública |
| `registrar_letra.py` | `registrar_letra()` | pública |
| `letra_ya_usada.py` | `letra_ya_usada()` | pública |
| `obtener_letras_usadas.py` | `obtener_letras_usadas()` | pública |

---

## Pendiente de refactorizar

| Módulo | Estado |
|---|---|
| `src/juego/logica/` | ⏳ Próximo |
| `src/base_datos/conexion/` | ⏳ Próximo |
| `src/base_datos/inicializar/` | ⏳ Próximo |
| `src/base_datos/consultas/` | ⏳ Próximo |
| `src/base_datos/insercion/` | ⏳ Próximo |
| `src/interfaz/dibujo/` | ⏳ Próximo |
| `src/interfaz/pantalla/` | ⏳ Próximo |
| `src/juego/bucle/` | ⏳ Próximo |
| `src/interfaz/menu/` | ⏳ Próximo |

---

## Resumen de decisiones — Fase 7

| Elemento | Propuesto | Decisión |
|---|---|---|
| Granularidad | Por módulo | ✅ Un archivo por función/clase |
| Orden | Sin definir | ✅ De adentro hacia afuera |
| Tests | Después del código | ✅ En paralelo módulo por módulo |
| `while True` | Sin especificar | ✅ En bucles de entrada de usuario |
| Creación de carpetas | Por la IA | ✅ Por el alumno |
| Imports rotos | Detectados manualmente | ✅ Detectados por pytest automáticamente |