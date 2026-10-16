from pathlib import Path
import shutil

# Carpeta de recetas (se crea junto al script si no existe)
RUTA_RECETAS = Path('C:/Users/Maria Paula Toro/Documents/Recetas')
RUTA_RECETAS.mkdir(exist_ok=True)


def contar_recetas():
    return sum(1 for _ in RUTA_RECETAS.glob("**/*.txt"))


def listar_categorias():
    return sorted(c for c in RUTA_RECETAS.iterdir() if c.is_dir())


def listar_recetas(categoria):
    return sorted(categoria.glob("*.txt"))


def elegir_de_lista(items, titulo, mostrar=lambda x: x.stem):
    """Muestra una lista numerada y devuelve el elemento elegido (o None)."""
    if not items:
        print("\n(No hay elementos disponibles)")
        return None
    print(f"\n{titulo}")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {mostrar(item)}")
    while True:
        eleccion = input("Elige un número (0 para cancelar): ").strip()
        if eleccion == "0":
            return None
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(items):
            return items[int(eleccion) - 1]
        print("Opción no válida, intenta de nuevo.")


def nombre_seguro(nombre):
    """Evita rutas peligrosas como '../' en los nombres."""
    nombre = nombre.strip()
    if not nombre or any(c in nombre for c in '\\/:*?"<>|') or nombre in (".", ".."):
        return None
    return nombre


def elegir_categoria():
    return elegir_de_lista(listar_categorias(), "Categorías disponibles:", lambda c: c.name)


def elegir_receta(categoria):
    return elegir_de_lista(listar_recetas(categoria), f"Recetas en '{categoria.name}':")


def leer_receta():
    categoria = elegir_categoria()
    if not categoria:
        return
    receta = elegir_receta(categoria)
    if not receta:
        return
    print(f"\n===== {receta.stem} =====")
    print(receta.read_text(encoding="utf-8"))
    print("=" * (14 + len(receta.stem)))


def crear_receta():
    categoria = elegir_categoria()
    if not categoria:
        return
    nombre = nombre_seguro(input("\nNombre de la nueva receta: "))
    if not nombre:
        print("Nombre no válido.")
        return
    archivo = categoria / f"{nombre}.txt"
    if archivo.exists():
        print("Ya existe una receta con ese nombre.")
        return
    print("Escribe el contenido de la receta (línea vacía para terminar):")
    lineas = []
    while True:
        linea = input()
        if linea == "":
            break
        lineas.append(linea)
    archivo.write_text("\n".join(lineas), encoding="utf-8")
    print(f"Receta '{nombre}' creada en '{categoria.name}'.")


def crear_categoria():
    nombre = nombre_seguro(input("\nNombre de la nueva categoría: "))
    if not nombre:
        print("Nombre no válido.")
        return
    carpeta = RUTA_RECETAS / nombre
    if carpeta.exists():
        print("Esa categoría ya existe.")
        return
    carpeta.mkdir()
    print(f"Categoría '{nombre}' creada.")


def eliminar_receta():
    categoria = elegir_categoria()
    if not categoria:
        return
    receta = elegir_receta(categoria)
    if not receta:
        return
    if input(f"¿Seguro que quieres eliminar '{receta.stem}'? (s/n): ").lower() == "s":
        receta.unlink()
        print("Receta eliminada.")
    else:
        print("Operación cancelada.")


def eliminar_categoria():
    categoria = elegir_categoria()
    if not categoria:
        return
    n = len(listar_recetas(categoria))
    aviso = f" y sus {n} receta(s)" if n else ""
    if input(f"¿Seguro que quieres eliminar la categoría '{categoria.name}'{aviso}? (s/n): ").lower() == "s":
        shutil.rmtree(categoria)
        print("Categoría eliminada.")
    else:
        print("Operación cancelada.")


def main():
    print("=" * 40)
    print("  ¡Bienvenido al Gestor de Recetas!")
    print("=" * 40)
    print(f"Ruta de recetas: {RUTA_RECETAS}")

    acciones = {
        "1": leer_receta,
        "2": crear_receta,
        "3": crear_categoria,
        "4": eliminar_receta,
        "5": eliminar_categoria,
    }

    while True:
        print(f"\nTotal de recetas: {contar_recetas()}")
        print("""
¿Qué deseas hacer?
  1. Leer una receta
  2. Crear una receta
  3. Crear una categoría
  4. Eliminar una receta
  5. Eliminar una categoría
  6. Salir""")
        opcion = input("Opción: ").strip()
        if opcion == "6":
            print("¡Hasta luego!")
            break
        accion = acciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

    




