#1
multiplos_de_cuatro = list(range(4, 101, 4))
print(multiplos_de_cuatro)
#2
mi_lista = ["Python", "es", "un", "lenguaje", "genial"]
penultimo_elemento = mi_lista[-2]
print(f"El penúltimo elemento es: {penultimo_elemento}")
#3
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("Python")
print(lista_vacia)
#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Reemplaza el segundo elemento (índice 1)
animales[-1] = "oso"  # Reemplaza el último elemento (índice -1)
print(animales)
#5
#Crea una lista de números.
#Encuentra el número más grande de esa lista.
#Elimina la primera vez que aparece ese número más grande en la lista.
#Muestra la lista resultante después de la eliminación.
#Por lo tanto, al ejecutar este programa, la salida que se mostrará será la lista numeros sin el número 22.

#6
numeros_saltos = list(range(10, 31, 5))
print(numeros_saltos[:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "corsa"
autos[2] = "megane"
print(autos)

#8
dobles = []
dobles.append(5 * 2)   # Agrega el doble de 5 (10)
dobles.append(10 * 2)  # Agrega el doble de 10 (20)
dobles.append(15 * 2)  # Agrega el doble de 15 (30)
print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

#10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

