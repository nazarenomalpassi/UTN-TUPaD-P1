#1
for numero in range(101):
    print(numero)
#2
try:
    numero_str = input("Ingresa un número entero: ")
    numero = int(numero_str)
    cantidad_digitos = len(numero_str)
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")
#3
try:
    valor1 = int(input("Ingresa el primer número entero: "))
    valor2 = int(input("Ingresa el segundo número entero: "))
    inicio = min(valor1, valor2) + 1
    fin = max(valor1, valor2)
    suma = 0
    for numero in range(inicio, fin):
        suma += numero  
    print(f"La suma de los números entre {valor1} y {valor2} (excluyéndolos) es: {suma}")
except ValueError:
    print("Error: Por favor, ingresa números enteros válidos.")
#4
while True:
    try:
        numero = int(input("Ingresa un número entero (ingresa 0 para detener): "))
        if numero == 0:
            break
        suma_total += numero

    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")
print(f"La suma total de los números ingresados es: {suma_total}")
#5
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    try:
        intento = int(input("Adivina el número (entre 0 y 9): "))
        intentos += 1 
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")
#6
for numero_par in range(100, -1, -2):
    print(numero_par)
#7
try:
    limite = int(input("Ingresa un número entero positivo: "))
    if limite < 0:
        print("Error: Por favor, ingresa un número entero positivo.")
    else:
        suma_total = 0
        for numero in range(limite + 1):
            suma_total += numero  
        print(f"La suma de los números desde 0 hasta {limite} es: {suma_total}")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")
#8
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad_numeros = 5  
for i in range(cantidad_numeros):
    try:
        numero = int(input(f"Ingresa el número {i + 1}: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")
print("\n--- Resultados ---")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
#9
numeros = []
suma_total = 0

cantidad_numeros = 5  
for i in range(cantidad_numeros):
    try:
        numero = int(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)  
        suma_total += numero    
    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")
if cantidad_numeros > 0:
    media = suma_total / cantidad_numeros
    print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")
else:
    print("No se ingresaron números para calcular la media.")
#10
try:
    numero = int(input("Ingresa un número entero: "))
    numero_str = str(numero)
    numero_invertido_str = numero_str[::-1]
    numero_invertido = int(numero_invertido_str)
    print(f"El número ingresado es: {numero}")
    print(f"El número con los dígitos invertidos es: {numero_invertido}")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")



