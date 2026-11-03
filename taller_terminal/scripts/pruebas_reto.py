"""Pruebas de mi variante 1. Ejecutar con el mismo Python que herramienta.py."""
from pathlib import Path
from herramienta import cargar_objetos, unidades_por_categoria, buscar_objeto, filtrar_objetos

objetos = cargar_objetos(Path(__file__).with_name("datos.csv"))
assert len(objetos) == 6
assert unidades_por_categoria(objetos) == {"equipo": 9, "apoyo": 6}
assert buscar_objeto(objetos, "CABLE USB")["cantidad"] == 5
assert buscar_objeto(objetos, "no_existe") is None
assert filtrar_objetos(objetos, 2) == ['rotulador', 'adaptador', 'libreta'], "Revisa la selección del CSV"
mini = [dict(nombre="debajo", cantidad=1), dict(nombre="igual", cantidad=2),
        dict(nombre="encima", cantidad=3)]
assert filtrar_objetos(mini, 2) == ['debajo', 'igual'], "Revisa la igualdad al límite"
assert filtrar_objetos([], 2) == [], "La lista vacía devuelve otra lista vacía"
print("Pruebas correctas: resumen, búsqueda y filtro de la variante 1")

