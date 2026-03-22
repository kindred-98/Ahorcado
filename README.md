<div align="center">

# ⚔️ EL AHORCADO MEDIEVAL

**Juego del Ahorcado con temática medieval desarrollado en Python**  
*Arquitectura modular · CLI · SQLite · Testing automatizado · Documentación SPECAR*

---

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-191%20passed-2ea44f?style=for-the-badge&logo=pytest&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-99%25-brightgreen?style=for-the-badge&logo=codecov&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Base%20de%20datos-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-1%20file%20per%20function-blueviolet?style=for-the-badge)
![Methodology](https://img.shields.io/badge/Docs-SPECAR-orange?style=for-the-badge)

</div>

---

## 📌 Índice

- [Descripción](#-descripción)
- [Demo](#-demo)
- [Características](#-características)
- [Arquitectura](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#️-uso)
- [Testing](#-testing)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Tecnologías](#-tecnologías)
- [Documentación IA](#-ia-utilizadas-durante-el-desarrollo)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 📖 Descripción

**El Ahorcado Medieval** es un juego de consola desarrollado en Python donde el jugador debe adivinar palabras de temática medieval antes de que el personaje sea ahorcado. Cada fallo revela un nuevo estado del arte ASCII personalizado con mensajes únicos en la rama del árbol.

El proyecto fue construido con foco en:

- 🏗️ **Arquitectura modular** — un archivo por función/clase en toda la base de código
- 🗄️ **Persistencia SQLite** — palabras organizadas por categoría y dificultad
- 🧪 **Testing robusto** — 191 tests automatizados con 99% de cobertura
- 📐 **Principio de responsabilidad única** — aplicado al nivel más granular posible
- 📋 **Documentación SPECAR** — 9 fases documentadas con metodología estructurada

---

## 🎮 Demo

```
  ╔════════════════════════════════════════════════════════════════════╗
  ║                   ✦   EL AHORCADO MEDIEVAL   ✦                    ║
  ║                                                                    ║
  ║   Palabra :  _ _ _ _ _ _ _ _                                       ║
  ║   Letras usadas: ninguna                                           ║
  ╚════════════════════════════════════════════════════════════════════╝

    &&@@@@@@@&&
   &@@@@@@@@@@@&      ✦        .         ✦      .       ✦
  &@@@@@@@@@@@@@&&________________________________________
 &@@@@@@@@@@@@@@& /       No me dejas morir por favor    \
 &@@@@@@@@@@@@@& /________________________________________\
  &@@@@@@@@@@@@&                       |
                                       |
```

---

## 🚀 Características

| Funcionalidad | Descripción | Estado |
|---|---|---|
| Juego completo | Adivinar palabras con 6 intentos máximo | ✅ |
| Arte ASCII medieval | 7 estados progresivos con mensajes personalizados | ✅ |
| Base de datos SQLite | 20 palabras iniciales en 4 categorías | ✅ |
| Añadir palabras | El jugador puede insertar palabras nuevas | ✅ |
| Ver palabras | Listado agrupado por categoría y dificultad | ✅ |
| Filtro por categoría | Elegir entre animales, armas, lugares o personajes | ✅ |
| Validaciones completas | Letras, palabras, categorías y dificultades | ✅ |
| Tests automatizados | Suite con pytest + cobertura 99% | ✅ |
| Arquitectura modular | Un archivo por función/clase | ✅ |
| Documentación SPECAR | 9 fases documentadas con IA | ✅ |

---

## 🧠 Arquitectura del proyecto

```
┌─────────────────────────────────────────────────────────────────────┐
│                      El Ahorcado Medieval                           │
│                                                                     │
│  ┌─────────────────┐         ┌──────────────────────────────────┐   │
│  │    interfaz/    │         │           juego/                 │   │
│  │                 │◄───────►│                                  │   │
│  │  menu/          │         │  estado/  → dataclass + ops      │   │
│  │  pantalla/      │         │  logica/  → victoria / derrota   │   │
│  │  dibujo/        │         │  bucle/   → flujo de partida     │   │
│  └─────────────────┘         └──────────────────────────────────┘   │
│          │                                    │                     │
│          ▼                                    ▼                     │
│  ┌─────────────────┐         ┌──────────────────────────────────┐   │
│  │  validaciones/  │         │          base_datos/             │   │
│  │                 │         │                                  │   │
│  │  letra/         │         │  conexion/    → obtener_conexion │   │
│  │  palabra/       │         │  inicializar/ → crear tabla      │   │
│  │                 │         │  consultas/   → SELECT aleatorio │   │
│  └─────────────────┘         │  insercion/   → INSERT / EXISTS  │   │
│                              └──────────────────────────────────┘   │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                      ahorcado.py                             │   │
│  │            Punto de entrada — inicializa BD y menú           │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Instalación

### Requisitos previos

- Python 3.12 o superior
- pip

### Pasos

**1. Clonar el repositorio:**

```bash
git clone https://github.com/kindred-98/Ahorcado.git
cd Ahorcado
```

**2. Crear entorno virtual:**

```bash
python -m venv .venv
```

**3. Activar entorno:**

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**4. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

### Iniciar el juego

```bash
python ahorcado.py
```

### Opciones del menú principal

```
  ╔══════════════════════════════════════════════╗
  ║       ⚔   EL AHORCADO MEDIEVAL   ⚔          ║
  ╠══════════════════════════════════════════════╣
  ║                                              ║
  ║   1)  ⚔  Jugar                              ║
  ║   2)  📖  Añadir palabra                    ║
  ║   3)  📜  Ver palabras                      ║
  ║   4)  🚪  Salir                             ║
  ║                                              ║
  ╚══════════════════════════════════════════════╝
```

---

## 🧪 Testing

El proyecto incluye una suite completa de tests automatizados con **pytest**.

**Ejecutar todos los tests:**

```bash
pytest tests/ -v
```

**Con reporte de cobertura:**

```bash
pytest --cov
```

**Con reporte detallado de líneas sin cubrir:**

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

**Resultados actuales:**

```
========================= test session starts =========================
platform win32 -- Python 3.14.3, pytest-9.0.2

tests/base_datos/conexion/          ...      PASSED
tests/base_datos/consultas/         ...........   PASSED
tests/base_datos/inicializar/       ....     PASSED
tests/base_datos/insercion/         ............  PASSED
tests/interfaz/pantalla/            .................. PASSED
tests/juego/estado/                 .......... PASSED
tests/juego/logica/                 .................. PASSED
tests/validaciones/letra/           .......................... PASSED
tests/validaciones/palabra/         ...................... PASSED
tests/test_cobertura_completa.py    ..................  PASSED

============= 191 passed in 1.89s =============
---------- coverage: 99% ----------
```

---

## 📂 Estructura del proyecto

```
Ahorcado/
│
├── ahorcado.py                          # Punto de entrada
│
├── src/
│   ├── validaciones/
│   │   ├── letra/
│   │   │   ├── alfabeto.py              # ALFABETO_ESPAÑOL
│   │   │   ├── validar_letra.py         # validar_letra()
│   │   │   └── normalizar_caracter.py   # _normalizar_caracter()
│   │   └── palabra/
│   │       ├── constantes.py            # CATEGORIAS, DIFICULTADES, LONGITUDES
│   │       ├── validar_palabra.py       # validar_palabra()
│   │       ├── validar_categoria.py     # validar_categoria()
│   │       ├── validar_dificultad.py    # validar_dificultad()
│   │       └── buscar_caracter_invalido.py
│   │
│   ├── juego/
│   │   ├── estado/
│   │   │   ├── clase_estado_partida.py  # EstadoPartida (dataclass)
│   │   │   ├── crear_estado_inicial.py
│   │   │   ├── construir_palabra_oculta.py
│   │   │   ├── registrar_letra.py
│   │   │   ├── letra_ya_usada.py
│   │   │   └── obtener_letras_usadas.py
│   │   ├── logica/
│   │   │   ├── hay_victoria.py
│   │   │   ├── hay_derrota.py
│   │   │   ├── letra_en_palabra.py
│   │   │   ├── intentos_restantes.py
│   │   │   └── partida_terminada.py
│   │   └── bucle/
│   │       ├── iniciar_partida.py       # Punto de entrada del juego
│   │       ├── ejecutar_bucle_de_turnos.py
│   │       ├── mostrar_turno.py
│   │       ├── pedir_letra_valida.py
│   │       ├── mostrar_resultado_final.py
│   │       ├── preguntar_jugar_otra.py
│   │       └── obtener_palabra_o_salir.py
│   │
│   ├── base_datos/
│   │   ├── conexion/
│   │   │   ├── ruta_base_datos.py       # RUTA_BASE_DATOS
│   │   │   └── obtener_conexion.py      # obtener_conexion()
│   │   ├── inicializar/
│   │   │   ├── palabras_iniciales.py    # PALABRAS_INICIALES (20 palabras)
│   │   │   ├── crear_tabla_palabras.py
│   │   │   ├── poblar_palabras_iniciales.py
│   │   │   └── inicializar_base_datos.py
│   │   ├── consultas/
│   │   │   ├── construir_consulta_aleatoria.py
│   │   │   ├── obtener_palabra_aleatoria.py
│   │   │   ├── obtener_todas_las_palabras.py
│   │   │   └── obtener_categorias.py
│   │   └── insercion/
│   │       ├── normalizar_dificultad.py
│   │       ├── insertar_palabra.py
│   │       └── palabra_ya_existe.py
│   │
│   └── interfaz/
│       ├── dibujo/
│       │   ├── maximo_fallos.py         # MAXIMO_FALLOS = 6
│       │   └── estados.py               # 7 estados ASCII medievales
│       ├── pantalla/
│       │   ├── limpiar_pantalla.py
│       │   ├── construir_cabecera.py
│       │   ├── mostrar_escena.py
│       │   ├── mostrar_mensaje.py
│       │   ├── mostrar_error.py
│       │   ├── formatear_letras_usadas.py
│       │   └── construir_etiqueta_fallos.py
│       └── menu/
│           ├── constantes_menu.py
│           ├── ejecutar_menu_principal.py
│           ├── mostrar_menu_principal.py
│           ├── pedir_opcion_menu.py
│           ├── pedir_campo_validado.py
│           ├── pedir_categoria_opcional.py
│           ├── accion_jugar.py
│           ├── accion_añadir_palabra.py
│           ├── accion_ver_palabras.py
│           ├── accion_salir.py
│           └── construir_menu.py
│
├── tests/
│   ├── conftest.py                      # Fixtures compartidos (BD temporal)
│   ├── test_cobertura_completa.py       # Tests de ramas except y edge cases
│   ├── base_datos/
│   │   ├── conexion/
│   │   ├── consultas/
│   │   ├── inicializar/
│   │   └── insercion/
│   ├── interfaz/
│   │   └── pantalla/
│   ├── juego/
│   │   ├── estado/
│   │   └── logica/
│   └── validaciones/
│       ├── letra/
│       └── palabra/
│
├── data/
│   └── palabras.db                      # Base de datos SQLite
│
├── docs/
│   ├── Fase1.md                         # Arte ASCII
│   ├── Fase2.md                         # Arquitectura e interfaz
│   ├── Fase3.md                         # Base de datos modular
│   ├── Fase4.md                         # Lógica del juego
│   ├── Fase5.md                         # Validaciones
│   ├── Fase6.md                         # Tests con pytest y pytest-cov
│   ├── Fase7.md                         # Refactorización modular (inicio)
│   ├── Fase8.md                         # Refactorización modular (base_datos + dibujo)
│   └── Fase9.md                         # Refactorización modular (cierre)
│
├── pytest.ini                           # Configuración de pytest
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠 Tecnologías

| Tecnología | Uso |
|---|---|
| [Python 3.12+](https://python.org) | Lenguaje principal |
| [SQLite3](https://docs.python.org/3/library/sqlite3.html) | Base de datos embebida |
| [Pytest](https://pytest.org) | Framework de testing |
| [Pytest-cov](https://github.com/pytest-dev/pytest-cov) | Cobertura de tests |
| [Dataclasses](https://docs.python.org/3/library/dataclasses.html) | Estado de partida |
| [Unicodedata](https://docs.python.org/3/library/unicodedata.html) | Normalización de tildes |

---

## 🤖 IA utilizadas durante el desarrollo

Este proyecto fue desarrollado con asistencia de herramientas de IA bajo metodología SPECAR.

| IA | Uso principal |
|---|---|
| **Claude (Anthropic)** | Arquitectura, generación de código, tests, refactorización y documentación completa |
| **Copilot** | Autocompletado y sugerencias en tiempo real dentro de VS Code |

Toda la asistencia IA está documentada en la carpeta `docs/` con el método SPECAR (Situación, Problema, Exploración, Cambios, Acuerdo, Resultado), cubriendo 9 fases del desarrollo.

---

## 📋 Changelog

### v1.0.0 — 2026-03-22

- 🎉 Release inicial del proyecto
- ✅ Juego del Ahorcado completo con 7 estados ASCII medievales personalizados
- ✅ Base de datos SQLite con 20 palabras en 4 categorías
- ✅ Menú interactivo: jugar, añadir palabras, ver palabras, salir
- ✅ Validaciones completas de entrada del usuario
- ✅ Arquitectura modular — un archivo por función/clase (59 archivos)
- ✅ Suite de 191 tests automatizados con 99% de cobertura
- ✅ Documentación SPECAR en 9 fases

---
<div align="center">

## 👨‍💻 Autor

**SHIKAMARU**

*Proyecto educativo del Módulo 2 — Estrategias de Generación de Código con IA · Dicampus*  
*Enfocado en arquitectura limpia, testing automatizado y principio de responsabilidad única.*

[![GitHub](https://img.shields.io/badge/GitHub-kindred--98-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98/Ahorcado)

---

## 📜 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

Puedes usar, modificar y distribuir este software libremente siempre que se incluya la licencia original.

---

*Hecho con ⚔️ Python y arquitectura medieval*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub
</div>