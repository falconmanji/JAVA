# Lógica CRUD y Validaciones - Sistema de Registro de Películas (Tema #2)
# Desarrollado por: Integrante 2 (Registrar, Listar, Buscar) e Integrante 3 (Validaciones, Modificar, Eliminar)

from persistencia import guardar_datos


# ==============================================================================
# FUNCIONES DE VALIDACIÓN Y ENTRADA SEGURA (Integrante 3)
# ==============================================================================

def solicitar_texto_no_vacio(mensaje):
    """
    Solicita una cadena de texto al usuario y valida que no esté vacía.
    """
    while True:
        try:
            texto = input(mensaje).strip()
            if texto:
                return texto
            print("  [!] Error: Este campo no puede quedar vacío. Intente nuevamente.")
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Entrada cancelada.")
            return ""


def solicitar_anio(mensaje):
    """
    Solicita el año de estreno como un número entero válido (entre 1888 y 2100).
    Usa bloques try/except para evitar cierres por ValueError.
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            anio = int(entrada)
            if 1888 <= anio <= 2100:
                return anio
            print("  [!] Error: Ingrese un año válido (entre 1888 y 2100).")
        except ValueError:
            print("  [!] Error: Debe ingresar un número entero válido para el año (ej. 2014).")


def solicitar_calificacion(mensaje):
    """
    Solicita la calificación de la película (número decimal o entero de 1 a 10).
    Usa bloques try/except para evitar cierres por ValueError.
    """
    while True:
        try:
            entrada = input(mensaje).strip().replace(",", ".")
            calificacion = float(entrada)
            if 1.0 <= calificacion <= 10.0:
                return round(calificacion, 2)
            print("  [!] Error: La calificación debe estar en el rango de 1 a 10.")
        except ValueError:
            print("  [!] Error: Debe ingresar un valor numérico válido (ej. 8.5 o 9).")


# ==============================================================================
# OPERACIONES CRUD: REGISTRAR, LISTAR Y BUSCAR (Integrante 2)
# ==============================================================================

def registrar_pelicula(peliculas):
    """
    Captura los datos de una nueva película, la agrega a la lista y guarda en JSON.
    """
    print("\n" + "=" * 55)
    print("              REGISTRAR NUEVA PELÍCULA")
    print("=" * 55)

    titulo = solicitar_texto_no_vacio("Título de la película: ")
    if not titulo:
        return

    genero = solicitar_texto_no_vacio("Género (ej. Acción, Ciencia Ficción, Drama): ").title()
    if not genero:
        return

    anio = solicitar_anio("Año de estreno: ")
    calificacion = solicitar_calificacion("Calificación (1 a 10): ")

    nueva_pelicula = {
        "titulo": titulo,
        "genero": genero,
        "anio": anio,
        "calificacion": calificacion
    }

    peliculas.append(nueva_pelicula)
    guardar_datos(peliculas)
    print(f"\n[Éxito] La película '{titulo}' fue registrada y guardada correctamente.")


def listar_peliculas(peliculas):
    """
    Muestra todas las películas registradas en formato de tabla por consola.
    """
    print("\n" + "=" * 75)
    print("                         LISTADO DE PELÍCULAS")
    print("=" * 75)

    if not peliculas:
        print("No hay películas registradas en el sistema actualmente.")
        print("=" * 75)
        return

    print(f"{'N°':<4} | {'Título':<30} | {'Género':<18} | {'Año':<6} | {'Calif.'}")
    print("-" * 75)
    for indice, peli in enumerate(peliculas, start=1):
        titulo_corto = (peli["titulo"][:27] + "...") if len(peli["titulo"]) > 30 else peli["titulo"]
        genero_corto = (peli["genero"][:15] + "...") if len(peli["genero"]) > 18 else peli["genero"]
        print(f"{indice:<4} | {titulo_corto:<30} | {genero_corto:<18} | {peli['anio']:<6} | {peli['calificacion']:.1f}/10")
    print("=" * 75)
    print(f"Total de películas registradas: {len(peliculas)}")


def buscar_peliculas(peliculas):
    """
    Permite buscar películas por coincidencia parcial en el título o en el género.
    """
    print("\n" + "=" * 55)
    print("                  BUSCAR PELÍCULAS")
    print("=" * 55)

    if not peliculas:
        print("No hay películas registradas para realizar búsquedas.")
        return

    criterio = solicitar_texto_no_vacio("Ingrese el título o género a buscar: ").lower()
    if not criterio:
        return

    resultados = [
        (indice, peli)
        for indice, peli in enumerate(peliculas, start=1)
        if criterio in peli["titulo"].lower() or criterio in peli["genero"].lower()
    ]

    if not resultados:
        print(f"\nNo se encontraron películas que coincidan con '{criterio}'.")
        return

    print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
    print("-" * 75)
    print(f"{'N°':<4} | {'Título':<30} | {'Género':<18} | {'Año':<6} | {'Calif.'}")
    print("-" * 75)
    for indice, peli in resultados:
        titulo_corto = (peli["titulo"][:27] + "...") if len(peli["titulo"]) > 30 else peli["titulo"]
        genero_corto = (peli["genero"][:15] + "...") if len(peli["genero"]) > 18 else peli["genero"]
        print(f"{indice:<4} | {titulo_corto:<30} | {genero_corto:<18} | {peli['anio']:<6} | {peli['calificacion']:.1f}/10")
    print("-" * 75)


# ==============================================================================
# OPERACIONES CRUD: MODIFICAR Y ELIMINAR (Integrante 3)
# ==============================================================================

def modificar_pelicula(peliculas):
    """
    Permite seleccionar una película por su número en la lista y actualizar sus datos.
    """
    print("\n" + "=" * 55)
    print("                 MODIFICAR PELÍCULA")
    print("=" * 55)

    if not peliculas:
        print("No hay películas registradas para modificar.")
        return

    listar_peliculas(peliculas)

    try:
        seleccion = int(input("\nIngrese el número (N°) de la película que desea modificar (0 para cancelar): ").strip())
        if seleccion == 0:
            print("Operación cancelada.")
            return
        if seleccion < 1 or seleccion > len(peliculas):
            print("  [!] Error: El número ingresado no corresponde a ninguna película de la lista.")
            return
    except ValueError:
        print("  [!] Error: Debe ingresar un número entero válido.")
        return

    peli = peliculas[seleccion - 1]
    print(f"\nEditando: '{peli['titulo']}' (Presione Enter para conservar el valor actual)")

    nuevo_titulo = input(f"Nuevo título [{peli['titulo']}]: ").strip()
    if nuevo_titulo:
        peli["titulo"] = nuevo_titulo

    nuevo_genero = input(f"Nuevo género [{peli['genero']}]: ").strip()
    if nuevo_genero:
        peli["genero"] = nuevo_genero.title()

    while True:
        nuevo_anio_str = input(f"Nuevo año [{peli['anio']}]: ").strip()
        if not nuevo_anio_str:
            break
        try:
            nuevo_anio = int(nuevo_anio_str)
            if 1888 <= nuevo_anio <= 2100:
                peli["anio"] = nuevo_anio
                break
            print("  [!] Error: El año debe estar entre 1888 y 2100.")
        except ValueError:
            print("  [!] Error: Ingrese un número entero válido para el año.")

    while True:
        nueva_calif_str = input(f"Nueva calificación (1-10) [{peli['calificacion']}]: ").strip().replace(",", ".")
        if not nueva_calif_str:
            break
        try:
            nueva_calif = float(nueva_calif_str)
            if 1.0 <= nueva_calif <= 10.0:
                peli["calificacion"] = round(nueva_calif, 2)
                break
            print("  [!] Error: La calificación debe estar entre 1 y 10.")
        except ValueError:
            print("  [!] Error: Ingrese un número válido para la calificación.")

    guardar_datos(peliculas)
    print(f"\n[Éxito] La película '{peli['titulo']}' ha sido actualizada correctamente.")


def eliminar_pelicula(peliculas):
    """
    Permite eliminar una película seleccionada por su número previa confirmación.
    """
    print("\n" + "=" * 55)
    print("                  ELIMINAR PELÍCULA")
    print("=" * 55)

    if not peliculas:
        print("No hay películas registradas para eliminar.")
        return

    listar_peliculas(peliculas)

    try:
        seleccion = int(input("\nIngrese el número (N°) de la película que desea eliminar (0 para cancelar): ").strip())
        if seleccion == 0:
            print("Operación cancelada.")
            return
        if seleccion < 1 or seleccion > len(peliculas):
            print("  [!] Error: El número ingresado no corresponde a ninguna película de la lista.")
            return
    except ValueError:
        print("  [!] Error: Debe ingresar un número entero válido.")
        return

    peli_a_borrar = peliculas[seleccion - 1]
    confirmacion = input(f"¿Está seguro de que desea eliminar '{peli_a_borrar['titulo']}'? (s/n): ").strip().lower()

    if confirmacion == "s":
        eliminada = peliculas.pop(seleccion - 1)
        guardar_datos(peliculas)
        print(f"\n[Éxito] La película '{eliminada['titulo']}' fue eliminada del sistema.")
    else:
        print("\nEliminación cancelada.")