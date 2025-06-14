#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de añadir:", precios_frutas)
#2
# Partimos del diccionario resultante del Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 
                  'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# Actualizar los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario después de actualizar:", precios_frutas)
#3
# Partimos del diccionario resultante del Ejercicio 2
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 
                  'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# Crear una lista solo con las frutas (claves)
lista_frutas = list(precios_frutas.keys())

print("Lista de frutas:", lista_frutas)
#4
# Cargar 5 contactos
print("Por favor, carga 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

print("\nContactos cargados:", contactos)

# Consultar un número telefónico
nombre_buscar = input("\nIngresa el nombre del contacto que deseas consultar: ")

if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"'{nombre_buscar}' no se encontró en tus contactos.")

#5
frase = input("Ingresa una frase: ")

# Convertir la frase a minúsculas y dividirla en palabras
# Se usa .lower() para tratar "Hola" y "hola" como la misma palabra
# Se pueden añadir más limpiezas si la frase tiene puntuación, por ejemplo:
# palabras = re.findall(r'\b\w+\b', frase.lower())
palabras = frase.lower().split()

# 1. Palabras únicas (usando un set)
palabras_unicas = set(palabras)
print("\nPalabras únicas:", palabras_unicas)

# 2. Diccionario con la cantidad de veces que aparece cada palabra
recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
    # O usando collections.Counter:
    # from collections import Counter
    # recuento_palabras = Counter(palabras)

print("Recuento de palabras:", recuento_palabras)
#6
alumnos = {}

# Cargar nombres de 3 alumnos y sus 3 notas
print("Por favor, ingresa los nombres de 3 alumnos y sus 3 notas:")
for i in range(3):
    nombre_alumno = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        try:
            nota = float(input(f"Ingresa la nota {j+1} para {nombre_alumno}: "))
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número para la nota.")
            # Opcional: Podrías querer repetir la solicitud de la nota si es inválida
            j -= 1 # Para reintentar la misma nota si la entrada es inválida

    alumnos[nombre_alumno] = tuple(notas) # Guardar las notas como una tupla

print("\nNotas de los alumnos:", alumnos)

# Mostrar el promedio de cada alumno
print("\nPromedio de cada alumno:")
for alumno, notas_tupla in alumnos.items():
    promedio = sum(notas_tupla) / len(notas_tupla)
    print(f"El promedio de {alumno} es: {promedio:.2f}")
#7
# Sets de ejemplo (puedes pedirle al usuario que los ingrese si quieres)
parcial1_aprobados = {101, 102, 103, 104, 105}
parcial2_aprobados = {104, 105, 106, 107, 108}

print("Estudiantes que aprobaron Parcial 1:", parcial1_aprobados)
print("Estudiantes que aprobaron Parcial 2:", parcial2_aprobados)

# 1. Mostrar los que aprobaron ambos parciales (intersección)
aprobados_ambos = parcial1_aprobados.intersection(parcial2_aprobados)
print("\nEstudiantes que aprobaron ambos parciales:", aprobados_ambos)

# 2. Mostrar los que aprobaron solo uno de los dos (diferencia simétrica)
aprobados_solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)

# 3. Mostrar la lista total de estudiantes que aprobaron al menos un parcial (unión)
total_aprobados = parcial1_aprobados.union(parcial2_aprobados)
print("Lista total de estudiantes que aprobaron al menos un parcial:", total_aprobados)
#8
inventario = {}

while True:
    print("\n--- Gestión de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Mostrar todo el inventario")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        producto = input("Ingresa el nombre del producto a consultar: ")
        stock_actual = inventario.get(producto, "Producto no encontrado")
        print(f"Stock de '{producto}': {stock_actual}")
    elif opcion == '2':
        producto = input("Ingresa el nombre del producto: ")
        if producto in inventario:
            try:
                cantidad = int(input(f"¿Cuántas unidades deseas agregar a '{producto}'?: "))
                if cantidad > 0:
                    inventario[producto] += cantidad
                    print(f"Stock actualizado de '{producto}': {inventario[producto]}")
                else:
                    print("Por favor, ingresa una cantidad positiva.")
            except ValueError:
                print("Cantidad inválida. Ingresa un número entero.")
        else:
            print(f"'{producto}' no existe. Usa la opción 3 para agregarlo como nuevo.")
    elif opcion == '3':
        producto = input("Ingresa el nombre del nuevo producto: ")
        if producto not in inventario:
            try:
                stock_inicial = int(input(f"Ingresa el stock inicial de '{producto}': "))
                if stock_inicial >= 0:
                    inventario[producto] = stock_inicial
                    print(f"Producto '{producto}' agregado con stock {stock_inicial}.")
                else:
                    print("El stock inicial no puede ser negativo.")
            except ValueError:
                print("Stock inicial inválido. Ingresa un número entero.")
        else:
            print(f"'{producto}' ya existe. Usa la opción 2 para agregar unidades.")
    elif opcion == '4':
        if inventario:
            print("\nInventario actual:")
            for prod, stock in inventario.items():
                print(f"- {prod}: {stock} unidades")
        else:
            print("El inventario está vacío.")
    elif opcion == '5':
        print("Saliendo del programa de gestión de stock. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
#9
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Consulta médica",
    ("jueves", "18:00"): "Clase de Programación I"
}

print("Agenda actual:", agenda)

# Consultar actividad en cierto día y hora
print("\n--- Consultar Actividad en Agenda ---")
dia_consulta = input("Ingresa el día (ej. lunes): ").lower()
hora_consulta = input("Ingresa la hora (ej. 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)

evento = agenda.get(clave_consulta, "No hay actividad programada para esa hora y día.")

print(f"Actividad para {dia_consulta.capitalize()} a las {hora_consulta}: {evento}")
#10
diccionario_original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París"
}

# Construir el diccionario invertido
diccionario_invertido = {}
for pais, capital in diccionario_original.items():
    diccionario_invertido[capital] = pais

print("Diccionario original:", diccionario_original)
print("Diccionario invertido:", diccionario_invertido)


