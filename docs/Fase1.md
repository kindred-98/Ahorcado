# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 1 — Arte ASCII
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Este documento recoge el proceso de asistencia con IA para diseñar y refinar
el arte ASCII del **Ahorcado Medieval**. Se documenta cada interacción
siguiendo el método SPECAR: **Situación, Problema, Exploración, Cambios,
Acuerdo y Resultado.**

---

## INTERACCIÓN 1 — Propuesta inicial del arte ASCII

### 🔵 S — Situación

El ejercicio del Módulo 2 propone un Juego del Ahorcado con arte ASCII estándar
(7 estados, horca clásica). El profesor da libertad para personalizar la
implementación visual. Se dispone del PDF de referencia y una imagen de ejemplo
de una app comercial del juego.

### 🔴 P — Problema

El arte ASCII genérico no aporta valor diferencial al repositorio de GitHub.
Se necesita una propuesta visual más original que demuestre creatividad dentro
del marco técnico del ejercicio (CLI con Python).

### 🟠 E — Exploración

**Prompt enviado:**

> *"Quiero un juego en interfaz que salga un árbol y de él guinde una persona
> y que al 6 intento fallado el mecate de donde cuelga sea cortado con un
> disparo de otra persona para al fondo de la imagen."*

**La IA propuso dos caminos:**

- **CLI con arte ASCII** — encaja con el Commit 5 del enunciado.
- **Interfaz gráfica (tkinter / HTML)** — más detalle pero se aleja del ejercicio.

La IA recomendó quedarse en CLI con ASCII.

### 🟢 C — Cambios

Se pidió personalización sobre la propuesta base:

- Árbol con hojas en vez de horca clásica.
- Figura detallada, no palitos simples.
- Personaje secundario con espada a la derecha.
- Ambiente medieval.
- Escena nocturna con luna y estrellas.

### 🔵 A — Acuerdo

✅ CLI con ASCII  
✅ Árbol con hojas  
✅ Figura medieval detallada  
✅ Espadachín a la derecha  
✅ Noche con luna y estrellas  
✅ Estado 6 con efecto de corte  

### 🟢 R — Resultado

Se generó el primer `prueba_ahorcado.py` con los 7 estados y modo de navegación
interactivo (número 0-6, opción `todos` y `salir`). Funcional pero el layout
no correspondía al boceto que se tenía en mente.

---

## INTERACCIÓN 2 — Reposicionamiento de la escena

### 🔵 S — Situación

Se compartió un boceto dibujado a mano (imagen PNG) mostrando la distribución
deseada. El primer resultado tenía el árbol y la figura mal posicionados.

### 🔴 P — Problema

- El colgado no estaba en el centro exacto.
- El espadachín aparecía desde el estado 0 en vez del fallo 1.
- El suelo no diferenciaba hierba de tierra.

### 🟠 E — Exploración

**Prompt enviado:**

> *"El espadachín aparece en el primer fallo. Quiero una luna y quiero hierba
> donde está el ahorcado y tierra donde está el espadachín. Colgado en el
> centro exacto y no tan grande, mediano. Espadachín igual mediano."*

La IA resumió el nuevo layout antes de reescribir para confirmar comprensión.

### 🟢 C — Cambios

- Árbol a la izquierda con rama larga hacia el centro.
- Figura colgada en el centro exacto, tamaño mediano.
- Espadachín aparece solo a partir del estado 1.
- Suelo con `/\/\` (hierba) bajo el colgado y `. . .` (tierra) bajo el espadachín.

### 🔵 A — Acuerdo

✅ Reescritura completa de los 7 estados con el nuevo layout.

### 🟢 R — Resultado

Segunda versión generada. Layout mejorado respecto al boceto. Verificado sin
errores de sintaxis ni warnings.

---

## INTERACCIÓN 3 — Eliminar el espadachín

### 🔵 S — Situación

Con la segunda versión lista se revisó la escena. Dos personajes resultaban
visualmente cargados y complicaban el ASCII.

### 🔴 P — Problema

El espadachín añadía complejidad innecesaria. La narrativa más impactante era
que la cuerda se rompiera sola en el 6to fallo.

### 🟠 E — Exploración

**Prompt enviado:**

> *"MEJOR QUITEMOS AL ESPADACHÍN, HAGÁMOSLO SOLO CON LA PERSONA Y QUE CAIGA
> EN EL 6 FALLO."*

La IA confirmó el nuevo plan antes de proceder.

### 🟢 C — Cambios

- Eliminación completa del espadachín de todos los estados.
- Estado 6 rediseñado: cuerda rota `~`, efecto `* SNAP! *` con estrellas `✦`.
- Figura en pose de caída libre.

### 🔵 A — Acuerdo

✅ Reescritura manteniendo árbol, hierba, estrellas y cabecera.  
❌ Espadachín eliminado definitivamente.

### 🟢 R — Resultado

Tercera versión más limpia y dramática. Sin warnings, sintaxis verificada.

---

## INTERACCIÓN 4 — Eliminar la luna

### 🔵 S — Situación

La luna ASCII ocupaba 4 líneas en el lado derecho de cada estado, compitiendo
visualmente con el árbol y la figura.

### 🔴 P — Problema

La luna con `( ' )` y `.' ~~~ '.` quedaba torpe visualmente. El cielo solo
con estrellas y puntos es más elegante.

### 🟠 E — Exploración

**Prompt enviado:**

> *"QUITEMOS LA LUNA."*

La IA identificó que el bloque se repetía en los 6 primeros estados y procedió
a reemplazarlos con `str_replace` individual.

### 🟢 C — Cambios

- Eliminación del bloque de luna de los 7 estados.
- Líneas reemplazadas por estrellas `✦` y puntos dispersos.
- Se corrigieron warnings de escape convirtiéndolos a raw strings `r"""`.

### 🔵 A — Acuerdo

✅ Reemplazo quirúrgico estado por estado.  
❌ Luna eliminada definitivamente.

### 🟢 R — Resultado

Versión final del archivo `prueba_ahorcado.py` aprobada: sin luna, sin
espadachín, sin warnings.

---

## INTERACCIÓN 5 — Árbol más grande y figura separada del tronco

### 🔵 S — Situación

Al integrar el arte en la arquitectura modular, se revisó visualmente la escena
y no convencía el tamaño del árbol ni la posición de la figura.

### 🔴 P — Problema

- El árbol era demasiado pequeño para la escena.
- La cabeza de la figura aparecía pegada al tronco del árbol.

### 🟠 E — Exploración

**Prompt enviado (con boceto anotado):**

> *"Quiero que el árbol sea más grande y que la cabeza no salga pegada al cepe."*

Se compartió una captura del estado 1 con anotaciones en amarillo marcando
dónde debía ir la figura.

### 🟢 C — Cambios

- Árbol mucho más alto, ocupa casi toda la altura izquierda.
- Rama rediseñada con doble línea para dar volumen.
- Cuerda más larga para separar la figura del tronco.
- Estado 6: mensaje cambiado a `⚔ Muerte por ahorcamiento . . . ⚔`.
- Figura cayendo con pose desparramada (brazos y piernas abiertos).

### 🔵 A — Acuerdo

✅ Árbol más alto y ancho.  
✅ Cuerda larga, figura centrada y separada.  
✅ Mensaje `Muerte por ahorcamiento`.  
✅ El alumno realizó cambios propios en el dibujo que no alteran la lógica.

### 🟢 R — Resultado

Archivo `dibujo.py` generado como módulo independiente en `src/interfaz/`.
Sintaxis verificada, 7 estados confirmados.

---

## Catálogo de funciones — Fase 1

### `src/interfaz/dibujo.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `ESTADOS` | `list[str]` | Lista con los 7 estados ASCII de la escena medieval |
| `MAXIMO_FALLOS` | `int` | Constante con el máximo de fallos permitidos (6) |

---

## Resumen de decisiones — Fase 1

| Elemento | Propuesto | Decisión |
|---|---|---|
| Plataforma | CLI o interfaz gráfica | ✅ CLI con ASCII |
| Árbol | Horca clásica | ✅ Árbol con hojas grande |
| Figura | Palitos simples | ✅ Figura medieval detallada |
| Espadachín | Con disparo al estado 6 | ❌ Eliminado |
| Estado 6 | Corte por espadachín | ✅ Cuerda rota sola + SNAP! |
| Mensaje estado 6 | HAS SIDO DERROTADO | ✅ Muerte por ahorcamiento |
| Luna | Luna grande ASCII | ❌ Eliminada |
| Suelo | Línea uniforme | ✅ Hierba + tierra diferenciada |