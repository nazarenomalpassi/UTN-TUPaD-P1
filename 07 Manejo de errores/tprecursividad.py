#1
def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.
    El caso base es factorial(0) = 1.
    """
    if n == 0:  # Caso base: el factorial de 0 es 1
        return 1
    else:       # Caso recursivo: n * factorial(n-1)
        return n * factorial(n - 1)

# Parte del programa principal para interactuar con el usuario
try:
    numero_usuario = int(input("Ingresa un número entero positivo para calcular su factorial y los anteriores: "))
    
    if numero_usuario < 0:
        print("Por favor, ingresa un número no negativo.")
    else:
        print(f"Calculando factoriales hasta {numero_usuario}:")
        for i in range(1, numero_usuario + 1): # Desde 1 hasta el número ingresado
            print(f"El factorial de {i} es: {factorial(i)}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
#2
def fibonacci(pos):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada de forma recursiva.
    Casos base: fibonacci(0) = 0, fibonacci(1) = 1.
    """
    if pos == 0:  # Primer caso base
        return 0
    elif pos == 1: # Segundo caso base
        return 1
    else:         # Caso recursivo: F(n) = F(n-1) + F(n-2)
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Parte del programa principal para interactuar con el usuario
try:
    posicion_limite = int(input("Ingresa la posición máxima para la serie de Fibonacci: "))

    if posicion_limite < 0:
        print("La posición debe ser un número no negativo.")
    else:
        print(f"Serie de Fibonacci hasta la posición {posicion_limite}:")
        for i in range(posicion_limite + 1): # Desde la posición 0 hasta la posición_limite
            print(f"F({i}) = {fibonacci(i)}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

#3
def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.
    Fórmula: n^m = n * n^(m-1).
    Caso base: n^0 = 1.
    """
    if exponente == 0: # Caso base: cualquier número elevado a 0 es 1
        return 1
    elif exponente < 0:
        # Para exponentes negativos: n^(-m) = 1 / n^m
        # Se calcula la potencia del exponente positivo y se saca su inverso.
        return 1 / potencia_recursiva(base, -exponente)
    else:              # Caso recursivo: base * potencia(base, exponente - 1)
        return base * potencia_recursiva(base, exponente - 1)

# Prueba de la función en un algoritmo general
try:
    b = float(input("Ingresa la base (número): "))
    e = int(input("Ingresa el exponente (número entero): "))

    resultado_potencia = potencia_recursiva(b, e)
    print(f"El resultado de {b} elevado a la {e} es: {resultado_potencia}")
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números válidos.")
except RecursionError:
    print("Error: RecursionError. El exponente podría ser demasiado grande o negativo de forma inesperada.")
#4
def decimal_a_binario_recursivo(numero_decimal):
    """
    Convierte un número entero positivo decimal a su representación binaria (cadena de texto) de forma recursiva.
    """
    if numero_decimal == 0: # Caso base: Si el número es 0, su binario es "0"
        return "0"
    elif numero_decimal == 1: # Caso base: Si el número es 1, su binario es "1"
        return "1"
    else:
        # Caso recursivo: Dividir por 2, guardar el resto y continuar con el cociente.
        # Los restos se leen de abajo hacia arriba, por lo que la llamada recursiva va primero.
        return decimal_a_binario_recursivo(numero_decimal // 2) + str(numero_decimal % 2)

# Parte del programa principal para interactuar con el usuario
try:
    num_dec = int(input("Ingresa un número entero positivo en base decimal para convertir a binario: "))
    
    if num_dec < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        # Manejo especial para el 0, ya que el caso base "0" es correcto,
        # pero la recursión con 0 directamente puede ser diferente si no se maneja bien el primer 0.
        if num_dec == 0:
            binario = "0"
        else:
            binario = decimal_a_binario_recursivo(num_dec)
        print(f"El número decimal {num_dec} en binario es: {binario}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero positivo.")
#5
def es_palindromo(palabra):
    """
    Verifica si una cadena de texto (sin espacios ni tildes) es un palíndromo de forma recursiva.
    No se permite el uso de [::-1] ni reversed(). 
    """
    # Casos base:
    # 1. Si la palabra tiene 0 o 1 caracter, es un palíndromo.
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo:
    # 2. Si el primer y último caracter son iguales, se verifica el resto de la palabra.
    elif palabra[0] == palabra[-1]:
        # Se llama a la función recursivamente con la subcadena sin el primer y último caracter
        return es_palindromo(palabra[1:-1])
    
    # 3. Si el primer y último caracter no son iguales, no es un palíndromo.
    else:
        return False

# Parte del programa principal para interactuar con el usuario
palabra_usuario = input("Ingresa una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ").lower()
# Opcional: limpiar la entrada si esperas tildes/espacios pero el requisito dice "sin espacios ni tildes"
# import re
# palabra_limpia = re.sub(r'[^a-z0-9]', '', palabra_usuario).lower()

if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' es un palíndromo.")
else:
    print(f"'{palabra_usuario}' NO es un palíndromo.")

#6
def suma_digitos(n):
    """
    Calcula la suma de los dígitos de un número entero positivo de forma recursiva.
    Restricciones: No convertir a string, usar % y //.
    """
    if n < 10:  # Caso base: Si el número es de un solo dígito, la suma es el propio número
        return n
    else:       # Caso recursivo: sumamos el último dígito y recursión con el resto del número
        # n % 10 obtiene el último dígito
        # n // 10 elimina el último dígito (división entera)
        return (n % 10) + suma_digitos(n // 10)

# Parte del programa principal para interactuar con el usuario
try:
    numero_sumar = int(input("Ingresa un número entero positivo para sumar sus dígitos: "))
    
    if numero_sumar < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        resultado_suma_digitos = suma_digitos(numero_sumar)
        print(f"La suma de los dígitos de {numero_sumar} es: {resultado_suma_digitos}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
#7
def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide de n niveles
    (n bloques en la base, n-1 en el siguiente, ..., 1 en la cima) de forma recursiva.
    """
    if n == 0:  # Caso base: Si no hay niveles (o base 0), no hay bloques
        return 0
    elif n == 1: # Caso base: Si hay 1 bloque en la base, solo es 1 bloque total
        return 1
    else:       # Caso recursivo: n bloques en el nivel actual + bloques de los niveles superiores
        return n + contar_bloques(n - 1)

# Parte del programa principal para interactuar con el usuario
try:
    bloques_base = int(input("Ingresa el número de bloques en el nivel más bajo de la pirámide: "))
    
    if bloques_base < 0:
        print("El número de bloques en la base debe ser un entero no negativo.")
    else:
        total_bloques = contar_bloques(bloques_base)
        print(f"Para una pirámide con {bloques_base} bloques en la base, se necesitan un total de {total_bloques} bloques.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
#8
def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito específico en un número entero positivo de forma recursiva.
    """
    if numero == 0:
        # Caso base: Si el número es 0, y el dígito buscado es 0, retorna 1.
        # Si el número es 0 y el dígito buscado no es 0, retorna 0.
        # Esto maneja correctamente contar el '0' en el número '0'.
        return 1 if digito == 0 else 0
    
    # Si el número ya es 0 (y el dígito no era 0) después de llamadas recursivas,
    # significa que ya no hay más dígitos que procesar.
    if numero < 10 and numero != 0: # Caso base para números de un solo dígito (no 0)
        return 1 if numero == digito else 0
    
    # Caso recursivo:
    # Comprobar el último dígito
    contador = 0
    if (numero % 10) == digito:
        contador = 1
        
    # Llamar recursivamente con el resto del número (sin el último dígito)
    return contador + contar_digito(numero // 10, digito)

# Manejo del caso especial cuando el número inicial es 0 y el dígito buscado es 0
# La implementación de contar_digito(0, 0) necesita ser robusta.
# La función de arriba ya lo maneja bien.

# Parte del programa principal para interactuar con el usuario
try:
    num_usuario = int(input("Ingresa un número entero positivo: "))
    dig_buscar = int(input("Ingresa el dígito a buscar (entre 0 y 9): "))

    if num_usuario < 0 or not (0 <= dig_buscar <= 9):
        print("Por favor, ingresa un número positivo y un dígito entre 0 y 9.")
    else:
        # Si el número ingresado es 0 y el dígito a buscar es 0, la función debería retornar 1.
        # Mi implementación actual lo maneja. Si no, necesitaríamos un if num_usuario == 0 and dig_buscar == 0
        
        veces_encontrado = contar_digito(num_usuario, dig_buscar)
        print(f"El dígito {dig_buscar} aparece {veces_encontrado} veces en el número {num_usuario}.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números enteros válidos.")
