# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 10 — Mejoras finales y cierre del proyecto
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Fase final del proyecto. Se implementan tres mejoras sobre el juego
completamente funcional: alcanzar el 100% de cobertura de tests,
añadir categoría `otros` y dificultad `legendario`, y una animación
de victoria al ganar la partida.

---

## INTERACCIÓN 1 — 100% de cobertura de tests

### 🔵 S — Situación

Con 191 tests pasando el proyecto tenía 99% de cobertura. Las 2 líneas
sin cubrir pertenecían al teardown del fixture `bd_prueba` en `conftest.py`,
código de infraestructura de tests que `coverage` no registra por diseño.

### 🔴 P — Problema

El 1% faltante no era código de producción sino el `conexion.close()` del
`yield` en el fixture. Intentar cubrirlo con un test directo no tiene sentido
semántico.

### 🟠 E — Exploración

**Prompt enviado:**

> *"ahora como completamos ese 100% de test"*

La IA propuso excluir `conftest.py` del reporte de cobertura mediante un
archivo `.coveragerc` en la raíz del proyecto.

### 🟢 C — Cambios

- `.coveragerc` creado en la raíz con `omit = tests/conftest.py`
- `pytest.ini` actualizado con `addopts = --cov-config=.coveragerc`

### 🔵 A — Acuerdo

✅ `conftest.py` excluido del reporte — es infraestructura, no lógica.  
✅ El código de producción sigue al 100%.

### 🟢 R — Resultado

**191 passed — 100% cobertura — 0 Miss.**

---

## INTERACCIÓN 2 — Categoría "otros" y dificultad "legendario"

### 🔵 S — Situación

El menú de añadir palabras solo aceptaba 4 categorías y 3 dificultades.
Se quería añadir `otros` para palabras sin categoría definida y `legendario`
para palabras de dificultad excepcional.

### 🔴 P — Problema

Las constantes estaban hardcodeadas en `constantes.py` y las etiquetas
del menú mostraban los valores directamente en el texto, lo que significaba
que añadir un valor nuevo requería tocar `accion_añadir_palabra.py` manualmente.

### 🟠 E — Exploración

**Prompt enviado:**

> *"quiero agregarle en añadir palabra la opcion de Otros. cuando no se aun
> personaje o un arma etc. en modo, poner legendario."*

### 🟢 C — Cambios

**`src/validaciones/palabra/constantes.py`:**
- Añadido `"otros"` a `CATEGORIAS_VALIDAS`
- Añadido `"legendario"` a `DIFICULTADES_VALIDAS`

**`src/base_datos/inicializar/palabras_iniciales.py`:**
- Añadidas 3 palabras de ejemplo en categoría `otros` con dificultad `legendario`:
  `excalibur`, `merlín`, `grial`

**`src/interfaz/menu/accion_añadir_palabra.py`:**
- Las etiquetas ahora se construyen dinámicamente desde las constantes:
  ```python
  categorias_texto  = " / ".join(sorted(CATEGORIAS_VALIDAS))
  dificultades_texto = " / ".join(sorted(DIFICULTADES_VALIDAS))
  ```
- Si se añaden nuevas categorías o dificultades en el futuro el menú
  las muestra automáticamente sin tocar este archivo.

**Tests añadidos:**
- `test_categoria_otros_valida()` en `test_validar_categoria.py`
- `test_dificultad_legendario_valida()` en `test_validar_dificultad.py`

### 🔵 A — Acuerdo

✅ Constantes actualizadas.  
✅ Palabras de ejemplo en BD inicial.  
✅ Etiquetas dinámicas en el menú.  
✅ Tests añadidos para los nuevos valores.

### 🟢 R — Resultado

**193 tests pasando — 100% cobertura.**  
El menú muestra correctamente:
```
Categoría (animales / armas / lugares / otros / personajes) >
Dificultad (dificil / facil / legendario / medio) >
```

---

## INTERACCIÓN 3 — Animación de victoria

### 🔵 S — Situación

Al ganar la partida el juego simplemente mostraba un mensaje de texto.
No había ningún elemento visual que celebrara la victoria del jugador.

### 🔴 P — Problema

La experiencia de ganar era igual a la de perder en términos visuales,
solo cambiaba el mensaje. Faltaba un momento de celebración que aprovechara
el arte ASCII del proyecto.

### 🟠 E — Exploración

**Prompt enviado:**

> *"también quiero que cuando el jugador gane le salta una animacion.
> porque ahora gana y no hace nada."*

La IA propuso una animación de frames ASCII con `time.sleep` y `os.system`
para limpiar la pantalla entre frames, sin dependencias externas.

### 🟢 C — Cambios

**Archivo nuevo `src/interfaz/pantalla/mostrar_victoria.py`:**
- 4 frames ASCII medievales con espadas y mensajes de victoria
- `mostrar_victoria(palabra_secreta)` — función pública
- `_mostrar_pantalla_final(palabra_secreta)` — pantalla estática final
- Constantes `_DURACION_FRAME = 0.4s` y `_REPETICIONES = 3`
- El alumno personalizó los frames del arte ASCII

**`src/juego/bucle/mostrar_resultado_final.py` actualizado:**
- En victoria → llama a `mostrar_victoria()` en lugar de `mostrar_escena()`
- En derrota → sigue mostrando la escena final con la palabra revelada

**Test nuevo `tests/interfaz/pantalla/test_mostrar_victoria.py`:**
- 5 tests usando `patch("time.sleep")` y `patch("os.system")` para que
  los tests no esperen ni limpien la pantalla real

### 🔵 A — Acuerdo

✅ Animación de 4 frames ASCII.  
✅ Pantalla final estática con la palabra adivinada.  
✅ Tests con mocks de `time.sleep` y `os.system`.  
✅ Arte ASCII personalizado por el alumno.

### 🟢 R — Resultado

**198 tests pasando — 100% cobertura.**  
Al ganar, el jugador ve la animación completa antes de que aparezca
la pregunta de jugar otra partida.

---

## Catálogo de cambios — Fase 10

### Archivos nuevos

| Archivo | Contenido |
|---|---|
| `src/interfaz/pantalla/mostrar_victoria.py` | Animación ASCII de victoria |
| `tests/interfaz/pantalla/test_mostrar_victoria.py` | 5 tests de la animación |
| `.coveragerc` | Exclusión de `conftest.py` del reporte |

---

### Archivos modificados

| Archivo | Cambio |
|---|---|
| `src/validaciones/palabra/constantes.py` | `"otros"` y `"legendario"` añadidos |
| `src/base_datos/inicializar/palabras_iniciales.py` | 3 palabras en categoría `otros` / dificultad `legendario` |
| `src/interfaz/menu/accion_añadir_palabra.py` | Etiquetas dinámicas desde constantes |
| `src/juego/bucle/mostrar_resultado_final.py` | Victoria llama a `mostrar_victoria()` |
| `pytest.ini` | Añadido `--cov-config=.coveragerc` |
| `tests/validaciones/palabra/test_validar_categoria.py` | Test para `"otros"` |
| `tests/validaciones/palabra/test_validar_dificultad.py` | Test para `"legendario"` |

---

## Resultado final del proyecto

```
198 passed — 100% cobertura — 0 Miss — 0 errores
```

| Métrica | Valor |
|---|---|
| Tests totales | 198 |
| Cobertura | 100% |
| Archivos de código fuente | 61 |
| Fases documentadas | 10 |
| Categorías de palabras | 5 (animales, armas, lugares, personajes, otros) |
| Niveles de dificultad | 4 (facil, medio, dificil, legendario) |
| Palabras iniciales en BD | 23 |

---

## Resumen de decisiones — Fase 10

| Elemento | Decisión |
|---|---|
| 100% cobertura | ✅ Via `.coveragerc` excluyendo `conftest.py` |
| Categoría nueva | ✅ `otros` — para palabras sin categoría definida |
| Dificultad nueva | ✅ `legendario` — para palabras de dificultad excepcional |
| Etiquetas del menú | ✅ Dinámicas desde constantes, no hardcodeadas |
| Animación victoria | ✅ 4 frames ASCII con `time.sleep` y mocks en tests |
| Arte ASCII victoria | ✅ Personalizado por el alumno |