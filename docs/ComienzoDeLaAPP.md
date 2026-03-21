# ⚔ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR

---

## Introducción

Este documento recoge el proceso completo de asistencia con IA para desarrollar el arte ASCII del Juego del Ahorcado Medieval, Se documenta cada interacción siguiendo el método SPECAR: **Situación, Problema, Exploración, Cambios, Acuerdo y Resultado.**

---

## INTERACCIÓN 1 — Propuesta inicial del arte ASCII

### 🔵 S — Situación

El ejercicio propone un Juego del Ahorcado con arte ASCII estándar (7 estados, horca clásica). El profesor da libertad para personalizar la implementación visual. Se dispone del archivo de referencia del ejercicio (PDF) y una imagen de ejemplo de una app comercial del juego.

### 🔴 P — Problema

El arte ASCII genérico no aporta valor diferencial al repositorio de GitHub. Se necesita una propuesta visual más original y llamativa que demuestre creatividad dentro del marco técnico del ejercicio (CLI con Python).

### 🟠 E — Exploración

**Mi prompt inicial:**

> *"Quiero un juego en interfaz que salga un árbol y de él guinde una persona y que al 6 intento fallado el mecate de donde cuelga sea cortado con un disparo de otra persona para al fondo de la imagen."*

La IA exploró dos caminos posibles:

- **CLI con arte ASCII** — encaja con el Commit 5 del enunciado, la limitación es que el disparo sería sugerido.
- **Interfaz gráfica (tkinter o HTML/JS)** — más detalle visual pero se aleja del ejercicio base.

La IA recomendó quedarse en CLI con ASCII para respetar la estructura del proyecto.

### 🟢 C — Cambios

Decidí quedarme en CLI pero pedí personalización:

- Árbol con hojas (no horca clásica).
- Figura detallada, no palitos simples.
- Personaje secundario con espada a la derecha.
- Ambiente medieval.
- Escena nocturna con luna y estrellas.

### 🔵 A — Acuerdo

Se acordó implementar el arte ASCII con las siguientes características:

- 7 estados (0-6), árbol con copa frondosa a la izquierda.
- Figura medieval detallada colgando con túnica, brazos y botas.
- Personaje espadachín a la derecha que aparece en el fallo 1.
- Fondo nocturno con luna grande arriba derecha y estrellas dispersas.
- Estado 6: cuerda cortada con efecto `SWISH!`, figura cayendo.

### 🟢 R — Resultado

Se generó el primer archivo `prueba_ahorcado.py` con los 7 estados y modo de navegación interactivo (número del 0 al 6, opción `todos` y `salir`). El resultado fue funcional pero el layout no correspondía al boceto que tenía en mente.

---

## INTERACCIÓN 2 — Reposicionamiento de la escena

### 🔵 S — Situación

Se compartió un boceto dibujado a mano (imagen PNG) mostrando la distribución deseada de los elementos. El primer resultado tenía el árbol y la figura mal posicionados respecto a la visión original.

### 🔴 P — Problema

La composición no respetaba el boceto:

- El colgado no estaba en el centro exacto de la escena.
- El espadachín aparecía desde el estado 0 en vez del fallo 1.
- La luna no estaba bien posicionada.
- El suelo no diferenciaba hierba (zona colgado) de tierra (zona espadachín).

### 🟠 E — Exploración

**Mi prompt de corrección:**

> *"El espadachín aparece en el primer fallo. La luna ok. Sí quiero hierba donde está el ahorcado y tierra donde está el espadachín. Colgado en el centro exacto y no tan grande, mediano. Espadachín igual mediano. El colgado va en el centro de la escena, colgando de una rama del árbol."*

La IA resumió el nuevo layout antes de reescribir el código para confirmar comprensión.

### 🟢 C — Cambios

Cambios confirmados respecto a la versión anterior:

- Árbol con copa frondosa a la izquierda, rama derecha larga hasta el centro.
- Figura colgada en el centro exacto, tamaño mediano.
- Espadachín a la derecha, aparece solo a partir del estado 1.
- Suelo con `/\/\` (hierba) bajo el colgado y `. . .` (tierra) bajo el espadachín.
- Luna grande arriba derecha como círculo ASCII.

### 🔵 A — Acuerdo

Se acordó reescribir completamente los 7 estados con el nuevo layout respetando el boceto dibujado a mano como referencia visual principal.

### 🟢 R — Resultado

Se generó la segunda versión del archivo. El layout mejoró notablemente respecto al boceto. El archivo fue verificado sin errores de sintaxis ni warnings y pasó las pruebas de ejecución.

---

## INTERACCIÓN 3 — Eliminar el espadachín

### 🔵 S — Situación

Con la segunda versión funcional, se revisó la escena y se reconsideró el rol del personaje secundario. La escena con dos personajes resultaba visualmente cargada y complicaba el ASCII.

### 🔴 P — Problema

El espadachín añadía complejidad visual innecesaria. La narrativa más impactante y limpia era que la cuerda se rompiera sola en el 6to fallo, sin personaje secundario, enfocando toda la atención en la figura cayendo.

### 🟠 E — Exploración

**Mi prompt:**

> *"MEJOR QUITEMOS AL ESPADACHÍN, HAGÁMOSLO SOLO CON LA PERSONA Y QUE CAIGA EN EL 6 FALLO."*

La IA confirmó el nuevo plan antes de proceder: cuerda rota sola, efecto `SNAP!`, figura cayendo con pose de impacto.

### 🟢 C — Cambios

- Eliminación completa del espadachín de todos los estados.
- Estado 6 rediseñado: cuerda con trazo roto `~`, efecto `* SNAP! *` con estrellas `✦`.
- Figura en pose de caída libre hacia el suelo.
- Lado derecho de la escena queda libre, dando amplitud visual.

### 🔵 A — Acuerdo

Se acordó reescribir el archivo manteniendo todo lo demás igual (árbol, hierba, estrellas, cabecera con letras) y eliminando únicamente el espadachín.

### 🟢 R — Resultado

Tercera versión generada, más limpia y dramática. Sin warnings, sintaxis verificada. La escena del estado 6 con `SNAP!` y la figura cayendo resultó más impactante que la versión con espadachín.

---

## INTERACCIÓN 4 — Eliminar la luna

### 🔵 S — Situación

Con la tercera versión lista se revisó el cielo de la escena. La luna ASCII ocupaba 4 líneas en el lado derecho de cada estado, compitiendo visualmente con el árbol y la figura central.

### 🔴 P — Problema

La luna en ASCII con `( ' )` y `.' ~~~ '.` quedaba demasiado literal y algo torpe visualmente. El cielo nocturno con solo estrellas y puntos es más elegante y deja más espacio limpio.

### 🟠 E — Exploración

**Mi prompt:**

> *"QUITEMOS LA LUNA."*

La IA identificó que el bloque de la luna se repetía exactamente igual en los 6 primeros estados y era distinto en el estado 6. Procedió a reemplazar los 7 bloques con `str_replace` individual.

### 🟢 C — Cambios

- Eliminación del bloque de luna `( ' )` / `.' ~~~ '.` de los 7 estados.
- Líneas reemplazadas por estrellas `✦` y puntos dispersos para mantener el ambiente nocturno.
- El espacio derecho del cielo quedó despejado y más amplio.
- Se corrigieron warnings de secuencias de escape convirtiéndolas a raw strings (`r"""`).

### 🔵 A — Acuerdo

Reemplazo quirúrgico estado por estado usando `str_replace`, sin tocar ningún otro elemento de la escena.

### 🟢 R — Resultado

Versión final del archivo `prueba_ahorcado.py` sin luna, sin espadachín, sin warnings. Arte ASCII verificado y aprobado. Listo para integrarse en el Commit 5 del proyecto real.

---

## Resumen de decisiones tomadas

| Elemento | Propuesto | Decisión final |
|---|---|---|
| Plataforma | CLI o interfaz gráfica | ✅ CLI con ASCII |
| Árbol | Horca clásica | ✅ Árbol con hojas |
| Figura colgada | Palitos simples | ✅ Figura medieval detallada |
| Personaje secundario | Espadachín con disparo | ❌ Eliminado — más limpio |
| Estado 6 | Corte por espadachín | ✅ Cuerda rota sola (SNAP!) |
| Ambientación | Sin especificar | ✅ Medieval nocturna |
| Luna | Luna grande ASCII | ❌ Eliminada — solo estrellas |
| Suelo | Línea uniforme | ✅ Hierba + tierra diferenciada |

---

## Archivo generado

**Archivo final:** `prueba_ahorcado.py`

- 7 estados ASCII (0-6) con árbol, figura medieval y cielo nocturno.
- Cabecera con recuadro para mostrar la palabra oculta y letras usadas.
- Modo de prueba interactivo: número del 0 al 6, opción `todos` y `salir`.
- Sin warnings en Python 3.12+ (uso de raw strings `r"""`).
- Listo para integrarse en `src/dibujo.py` en el Commit 5 del proyecto.


# Adjunto codigo con el que comence la app.

- Estara comentado por lo tanto para lograr verlo tendran que bajarse el repositorio o verlo en formado code.

<!-- # ============================================================
#   PRUEBA DE ARTE ASCII - EL AHORCADO MEDIEVAL
#   Navega entre estados: ingresa un número del 0 al 6
#   0 = sin fallos | 6 = cuerda rota, figura cayendo
# ============================================================

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# ─────────────────────────────────────────────────────────────
#  PALABRA DE PRUEBA (para visualizar las letras arriba)
# ─────────────────────────────────────────────────────────────
PALABRA_OCULTA = "_ _ _ _ _ _ _ _"
LETRAS_USADAS  = "Letras usadas: A, E, T"

# ─────────────────────────────────────────────────────────────
#  CABECERA CON LETRAS (aparece en todos los estados)
# ─────────────────────────────────────────────────────────────
CABECERA = """\
  ╔══════════════════════════════════════════════════════════════════╗
  ║          ✦   EL AHORCADO MEDIEVAL   ✦                           ║
  ║                                                                  ║
  ║   Palabra :  {palabra:<30}                    ║
  ║   {letras:<64}  ║
  ╚══════════════════════════════════════════════════════════════════╝"""

# ─────────────────────────────────────────────────────────────
#  7 ESTADOS ASCII
# ─────────────────────────────────────────────────────────────
ESTADOS = [

# ══════════════════════════════════════════════════════════════
# ESTADO 0 — Árbol, rama, cuerda vacía. Nadie colgado aún.
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                              \      ✦       .
   &@@@@@&&&&& /________________________________\    .      ✦
    &&@@@@&&& /                  |
     &@@@@&& /       ✦           |        .          ✦       .
      &@@@& /                    |
      &@@& /         .           |   ✦                   .
      &@@&/                      |
      &@@|           ✦           |        ✦          .
      &@||                       |
  ____|_||_______________________|______________________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\
""",

# ══════════════════════════════════════════════════════════════
# ESTADO 1 — Aparece la cabeza con capucha medieval
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                              \      ✦       .
   &@@@@@&&&&& /________________________________\    .      ✦
    &&@@@@&&& /                  |
     &@@@@&& /       ✦           |        .          ✦       .
      &@@@& /                  __|__
      &@@& /         .        /     \   ✦                .
      &@@&/                  | x . x |
      &@@|           ✦        \ ___ /       ✦          .
      &@||                     \ | /
  ____|_||______________________\|/______________________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\
""",

# ══════════════════════════════════════════════════════════════
# ESTADO 2 — Aparece el torso con túnica
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                              \      ✦       .
   &@@@@@&&&&& /________________________________\    .      ✦
    &&@@@@&&& /                  |
     &@@@@&& /       ✦           |        .          ✦       .
      &@@@& /                  __|__
      &@@& /         .        /     \   ✦                .
      &@@&/                  | x . x |
      &@@|           ✦        \ ___ /       ✦          .
      &@||                      | |
      &@||                    .-| |-.
  ____|_||____________________|_| |_|____________________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\
""",

# ══════════════════════════════════════════════════════════════
# ESTADO 3 — Aparecen los brazos caídos
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                              \      ✦       .
   &@@@@@&&&&& /________________________________\    .      ✦
    &&@@@@&&& /                  |
     &@@@@&& /       ✦           |        .          ✦       .
      &@@@& /                  __|__
      &@@& /         .        /     \   ✦                .
      &@@&/                  | x . x |
      &@@|           ✦        \ ___ /       ✦          .
      &@||                      | |
      &@||               *------| |------*
  ____|_||_______________|      | |      |______________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\
""",

# ══════════════════════════════════════════════════════════════
# ESTADO 4 — Aparece la parte inferior de la túnica
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                              \      ✦       .
   &@@@@@&&&&& /________________________________\    .      ✦
    &&@@@@&&& /                  |
     &@@@@&& /       ✦           |        .          ✦       .
      &@@@& /                  __|__
      &@@& /         .        /     \   ✦                .
      &@@&/                  | x . x |
      &@@|           ✦        \ ___ /       ✦          .
      &@||                      | |
      &@||               *------| |------*
      &@||                    .-| |-.
  ____|_||____________________|_| |_|____________________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\
""",

# ══════════════════════════════════════════════════════════════
# ESTADO 5 — Aparecen las piernas y pies
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                              \      ✦       .
   &@@@@@&&&&& /________________________________\    .      ✦
    &&@@@@&&& /                  |
     &@@@@&& /       ✦           |        .          ✦       .
      &@@@& /                  __|__
      &@@& /         .        /     \   ✦                .
      &@@&/                  | x . x |
      &@@|           ✦        \ ___ /       ✦          .
      &@||                      | |
      &@||               *------| |------*
      &@||                    .-| |-.
      &@||                   /  | |  \
  ____|_||__________________/   | |   \___________________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ [===] | | [===] /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\
""",

# ══════════════════════════════════════════════════════════════
# ESTADO 6 — Cuerda rota, figura cayendo al suelo
# ══════════════════════════════════════════════════════════════
r"""\
  .      ✦       .        ✦      .       ✦       .       ✦      .
     ✦       .        ✦      .       ✦       .       ✦      .
  .      ✦       .        ✦      .       ✦       .       ✦      .

  &&&&@@@@&&&&       ✦      .        ✦      .        ✦       .
 &@@@@@@@@@@@@&&                         ✦       .        ✦
 &@@@@@@@@@@@@@&& ______________________________   ✦      .
  &@@@@@@@@@@@@& /                          ~-'       ✦       .
   &@@@@@&&&&& /________________________________      .      ✦
    &&@@@@&&& /
     &@@@@&& /       ✦       ~.,       .          ✦       .
      &@@@& /
      &@@& /         .     ✦      ✦         ✦             .
      &@@&/                    * ✦ *
      &@@|           ✦       * SNAP! *      ✦          .
      &@||                     * ✦ *
      &@||               *------\ /------*
      &@||                 .---( @ )---.
      &@||                /    \_-_/    \
  ____|_||_______________/ [===]   [===] \________________________
 /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\ /\\
/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\/__\\

  ╔══════════════════════════════════════════════════════╗
  ║   ⚔   HAS SIDO DERROTADO, CABALLERO . . .   ⚔       ║
  ╚══════════════════════════════════════════════════════╝
""",
]

# ─────────────────────────────────────────────────────────────
#  BUCLE DE PRUEBA
# ─────────────────────────────────────────────────────────────

def mostrar_estado(numero: int):
    limpiar_pantalla()
    print(CABECERA.format(
        palabra=PALABRA_OCULTA,
        letras=LETRAS_USADAS,
    ))
    label = "Sin fallos aún" if numero == 0 else f"{numero} fallo(s)"
    print(f"\n  ── Estado {numero}/6  —  {label} ──\n")
    print(ESTADOS[numero])

def main():
    limpiar_pantalla()
    print("\n  ══════════════════════════════════════════")
    print("   🌙  PRUEBA DE ARTE ASCII — MODO MEDIEVAL")
    print("  ══════════════════════════════════════════")
    print("\n  Ingresa un número del 0 al 6 para ver cada estado.")
    print("  Ingresa 'todos' para ver la secuencia completa.")
    print("  Ingresa 'salir' para terminar.\n")

    while True:
        entrada = input("  Estado > ").strip().lower()

        if entrada == "salir":
            limpiar_pantalla()
            print("\n  ¡Hasta la próxima, caballero!\n")
            break

        elif entrada == "todos":
            for i in range(7):
                mostrar_estado(i)
                print(f"\n  [Estado {i}/6]  — Presiona ENTER para continuar...")
                input()

        elif entrada.isdigit() and 0 <= int(entrada) <= 6:
            mostrar_estado(int(entrada))

        else:
            print("  ⚠  Ingresa un número del 0 al 6, 'todos' o 'salir'.\n")

if __name__ == "__main__":
    main()

 -->
