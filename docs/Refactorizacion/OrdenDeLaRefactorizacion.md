El orden que seguire es de adentro hacia afuera, empezando por los módulos sin dependencias internas y terminando por los que dependen de todo lo demás.

El orden:

1. validaciones/    ← sin dependencias internas
2. juego/estado/    ← solo dataclasses, sin imports internos
3. juego/logica/    ← depende de estado e interfaz
4. base_datos/conexion/   ← base de todo base_datos
5. base_datos/inicializar/ ← depende de conexion
6. base_datos/consultas/  ← depende de conexion
7. base_datos/insercion/  ← depende de conexion
8. interfaz/dibujo/       ← solo constantes
9. interfaz/pantalla/     ← depende de dibujo
10. juego/bucle/          ← depende de casi todo
11. interfaz/menu/        ← depende de casi todo

El ahorcado.py no lo tocare toca, es el punto de entrada y ya es un archivo mínimo.

Después de cada módulo corremos:

```
pytest tests/ -v
```

Para verificar que nada se rompe antes de seguir con el siguiente.