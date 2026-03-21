# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
### Fase 4 — Lógica del juego
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Este documento recoge el proceso de asistencia con IA para implementar
los módulos `estado.py`, `logica.py` y `bucle.py` de la carpeta `src/juego/`.
Estos tres módulos conforman el corazón del juego: el estado de una partida,
las reglas que determinan victoria o derrota, y el bucle que coordina
el flujo completo de una partida.

---

## INTERACCIÓN 1 — Implementación de estado.py

### 🔵 S — Situación

Con `base_datos/` e `interfaz/` completos y funcionando, el siguiente paso
era implementar el módulo que representa y gestiona el estado de una partida
activa. Sin este módulo el bucle y la lógica no tienen datos con los que trabajar.

### 🔴 P — Problema

El juego necesita un objeto que almacene todo lo que ocurre durante una
partida: la palabra secreta, los fallos acumulados, las letras acertadas
y las fallidas. Usar variables sueltas o diccionarios sin estructura
definida haría el código frágil y difícil de mantener.

### 🟠 E — Exploración

**Prompt enviado:**

> *"si"*

La IA propuso usar una `dataclass` para representar el estado en vez de
un diccionario o variables sueltas, porque permite tipado explícito,
valores por defecto declarativos y es más legible.

### 🟢 C — Cambios

- `EstadoPartida` definida como `@dataclass` con `field(default_factory=set)`
  para los conjuntos de letras, evitando el problema del argumento mutable por defecto.
- `registrar_letra()` muta el estado directamente y lo devuelve para
  permitir encadenamiento si fuera necesario.
- `obtener_letras_usadas()` combina correctas y fallidas con el operador `|`
  y las ordena alfabéticamente para mostrar en pantalla.

### 🔵 A — Acuerdo

✅ `dataclass` para el estado de la partida.  
✅ `set` para letras correctas y fallidas (sin duplicados de forma automática).  
✅ Todas las funciones operan sobre `EstadoPartida`, no sobre variables sueltas.

### 🟢 R — Resultado

`src/juego/estado.py` generado con 1 clase y 5 funciones públicas.
Sintaxis verificada sin errores.

---

## INTERACCIÓN 2 — Implementación de logica.py

### 🔵 S — Situación

Con el estado definido se necesitaban las reglas del juego: cuándo se gana,
cuándo se pierde y cómo se evalúa cada letra jugada.

### 🔴 P — Problema

Mezclar las reglas dentro del bucle o del estado habría creado acoplamiento.
La lógica de victoria y derrota debe vivir separada para poder testearla
y modificarla de forma independiente.

### 🟠 E — Exploración

**Prompt enviado:**

> *"si"*

La IA propuso 5 funciones puras que reciben el estado y devuelven
un booleano o entero, sin efectos secundarios.

### 🟢 C — Cambios

- `hay_victoria()` usa `set.issubset()` para comparar las letras únicas
  de la palabra con las letras correctas acumuladas.
- `partida_terminada()` añadida como atajo para simplificar la condición
  del bucle principal sin repetir lógica.
- `intentos_restantes()` añadida para mostrar en pantalla cuántos intentos
  le quedan al jugador en cada turno.
- `MAXIMO_FALLOS` importado desde `src.interfaz.dibujo` para mantener
  una sola fuente de verdad en todo el proyecto.

### 🔵 A — Acuerdo

✅ Funciones puras sin efectos secundarios.  
✅ `MAXIMO_FALLOS` importado desde `dibujo.py`, no redefinido.  
✅ `partida_terminada()` como atajo que combina `hay_victoria()` y `hay_derrota()`.

### 🟢 R — Resultado

`src/juego/logica.py` generado con 5 funciones públicas.
Sintaxis verificada sin errores.

---

## INTERACCIÓN 3 — Implementación de bucle.py

### 🔵 S — Situación

Con el estado y la lógica listos se implementó el bucle principal que
coordina una partida completa de principio a fin.

### 🔴 P — Problema

El bucle necesita orquestar todos los módulos: obtener palabra de la BD,
gestionar turnos, validar entradas, mostrar la escena y preguntar si el
jugador quiere repetir. Toda esa coordinación debe estar en un solo lugar
sin convertirse en un archivo monolítico.

### 🟠 E — Exploración

**Prompt enviado:**

> *"ok"*

La IA propuso una función pública `iniciar_partida()` con todas las
responsabilidades delegadas en funciones privadas, siguiendo el mismo
patrón aplicado en `menu.py`.

### 🟢 C — Cambios

- `_pedir_letra_valida()` incluye doble validación: formato correcto
  mediante `validar_letra()` y que no sea una letra ya jugada.
- `_mostrar_resultado_final()` revela la palabra completa en ambos casos
  (victoria y derrota) para que el jugador siempre vea la respuesta.
- `iniciar_partida()` acepta parámetro opcional `categoria` para filtrar
  palabras desde el menú cuando se implemente esa funcionalidad.
- `bucle.py` importa `validar_letra` de `src.validaciones.letra` que
  se implementará en la siguiente fase.

### 🔵 A — Acuerdo

✅ Una función pública, resto privadas.  
✅ Doble validación de letra: formato + no repetida.  
✅ Palabra revelada siempre al final de la partida.  
✅ Parámetro `categoria` opcional para filtrado futuro desde el menú.  
⏳ `validar_letra()` pendiente de implementar en `src/validaciones/letra.py`.

### 🟢 R — Resultado

`src/juego/bucle.py` generado con 1 función pública y 6 privadas.
Sintaxis verificada sin errores.

---

## Catálogo de funciones — Fase 4

### `src/juego/estado.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `EstadoPartida` | clase | Dataclass con `palabra_secreta`, `categoria`, `dificultad`, `letras_correctas`, `letras_fallidas` y `numero_fallos` |
| `crear_estado_inicial()` | pública | Crea un estado nuevo desde un registro de la BD |
| `construir_palabra_oculta()` | pública | Genera la cadena con guiones y letras reveladas |
| `registrar_letra()` | pública | Añade la letra a correctas o fallidas y actualiza el contador |
| `letra_ya_usada()` | pública | Evita que el jugador repita letras ya jugadas |
| `obtener_letras_usadas()` | pública | Devuelve todas las letras jugadas ordenadas para pantalla |

---

### `src/juego/logica.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `hay_victoria()` | pública | Comprueba si todas las letras únicas fueron adivinadas |
| `hay_derrota()` | pública | Comprueba si se alcanzó el límite de fallos |
| `letra_en_palabra()` | pública | Verifica si una letra pertenece a la palabra secreta |
| `intentos_restantes()` | pública | Calcula los intentos que le quedan al jugador |
| `partida_terminada()` | pública | Atajo que combina `hay_victoria()` y `hay_derrota()` |

---

### `src/juego/bucle.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `iniciar_partida()` | pública | Punto de entrada: gestiona el ciclo completo de partidas |
| `_obtener_palabra_o_salir()` | privada | Busca palabra en la BD, informa si no hay disponibles |
| `_ejecutar_bucle_de_turnos()` | privada | Turno a turno hasta que la partida termina |
| `_mostrar_turno()` | privada | Renderiza escena con categoría e intentos restantes |
| `_pedir_letra_valida()` | privada | Solicita letra en bucle hasta recibir una válida y nueva |
| `_mostrar_resultado_final()` | privada | Muestra victoria o derrota con la palabra revelada |
| `_preguntar_jugar_otra()` | privada | Pregunta si quiere otra partida antes de volver al menú |

---

## Resumen de decisiones — Fase 4

| Elemento | Propuesto | Decisión |
|---|---|---|
| Estructura del estado | Diccionario o variables sueltas | ✅ `dataclass` tipada |
| Letras usadas | Lista | ✅ `set` (sin duplicados automático) |
| Reglas del juego | Dentro del bucle | ✅ Módulo independiente `logica.py` |
| `MAXIMO_FALLOS` | Redefinir en logica.py | ✅ Importado desde `dibujo.py` |
| Validación de letra | Solo formato | ✅ Formato + no repetida |
| Resultado final | Solo en derrota | ✅ Palabra revelada en victoria y derrota |
| Parámetro categoría | Sin filtro | ✅ Opcional para uso futuro desde menú |