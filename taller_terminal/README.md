# Mi herramienta de terminal

Autor/a y usuario GitHub: GGM (TheRealGGIOVI)
Variante de reto asignada (1–5): 1 (Reposición)

## Qué hace
Lee scripts/datos.csv, resume unidades por categoría y busca por nombre.
Mi nueva función: `filtrar_objetos(objetos, limite)` devuelve los nombres de las referencias con cantidad menor o igual que el límite.

## Requisitos
Bash (Git Bash en Windows) y Python 3.8 o posterior. Sin bibliotecas externas.
Si el intérprete se llama python3 o py -3, adaptar las llamadas a Python de daemon.sh.

## Organización
daemon.sh y README.md van en taller_terminal/.
herramienta.py, datos.csv y pruebas_reto.py van en taller_terminal/scripts/.
El lanzador crea taller_terminal/resultados/.

## Ejecución (desde taller_terminal)
```bash
bash daemon.sh
cat resultados/resumen.txt
cat resultados/filtro.txt
```
El lanzador muestra la ayuda, guarda el resumen y busca "cable USB".
Línea añadida al lanzador para filtrar y guardar resultados/filtro.txt: `python "$scripts/herramienta.py" --accion filtrar --limite 2 > "$resultados/filtro.txt"`
Límite de mi variante: 2
Pruebas: python scripts/pruebas_reto.py

## Comprobación
Predicción antes de ejecutar: Con límite 2, esperamos 3 coincidencias en el CSV: rotulador (1), adaptador (0) y libreta (2).
Resultado obtenido, caso en el límite y lista vacía: Coincidencias: 3 (rotulador, adaptador, libreta). En el caso límite (cantidad == 2) se incluye correctamente (<= 2). Con lista vacía devuelve lista vacía `[]`.
Comando de pruebas: python scripts/pruebas_reto.py
Qué estructura uso y por qué: Lista de diccionarios para cargar filas manteniendo orden y campos con nombre; diccionario acumulador para agregar unidades por categoría en un solo recorrido O(n); y lista de cadenas para recopilar los nombres que cumplen la condición de filtrado sin coste innecesario.
Ayuda de IA o «sin IA» y cómo la comprobé: Asistencia de IA en el andamiaje del código y redacción del README, verificada mediante pruebas unitarias con aserciones formales (`pruebas_reto.py`) y comprobación de la salida generada por `daemon.sh`.

daemon.sh ejecuta Python una vez; no es un servicio permanente.

