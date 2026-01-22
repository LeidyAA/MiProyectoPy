# ==============================
# EJERCICIO 1
# Determinar si un número es negativo
# ==============================

# Se pide al usuario que ingrese un número entero
# input() siempre devuelve texto, por eso usamos int()
num = int(input("Ingrese un número entero: "))

# Se evalúa si el número es menor que cero
if num < 0:
    # Si el número es menor que 0, es negativo
    print("El número es negativo")
else:
    # Si no es menor que 0, entonces no es negativo
    print("El número no es negativo")


# ==============================
# EJERCICIO 2
# Determinar cuántos dígitos tiene un número
# ==============================

# Se solicita otro número entero
num2 = int(input("\nIngrese otro número entero: "))

# abs() se usa para quitar el signo negativo si lo tiene
# str() convierte el número en texto
# len() cuenta cuántos caracteres tiene el texto
cantidad_digitos = len(str(abs(num2)))

# Se muestra la cantidad de dígitos
print("El número tiene", cantidad_digitos, "dígitos")


# ==============================
# EJERCICIO 3
# Determinar si un número es primo
# ==============================

# Se solicita un número al usuario
num3 = int(input("\nIngrese un número para verificar si es primo: "))

# Los números menores o iguales a 1 no son primos
if num3 <= 1:
    print("El número no es primo")
else:
    # Se asume que el número es primo
    es_primo = True

    # Se revisa si el número se puede dividir por otro número
    # que no sea 1 ni él mismo
    for i in range(2, num3):
        if num3 % i == 0:
            # Si se puede dividir, entonces no es primo
            es_primo = False
            break  # Se detiene el ciclo porque ya sabemos que no es primo

    # Se muestra el resultado
    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")


# ==============================
# EJERCICIO 4
# Leer 4 números y encontrar el mayor y su posición
# ==============================

# Se crea una lista vacía para guardar los números
lista = []

# Se usa un ciclo for para pedir 4 números
for i in range(4):
    # Se solicita cada número
    numero = int(input(f"\nIngrese el número {i + 1}: "))
    # Se agrega el número a la lista
    lista.append(numero)

# max() obtiene el número mayor de la lista
mayor = max(lista)

# index() obtiene la posición del mayor
# Se suma 1 porque las listas empiezan en 0
posicion = lista.index(mayor) + 1

# Se muestran los resultados
print("Lista ingresada:", lista)
print("El mayor número es", mayor, "y está en la posición", posicion)


# ==============================
# EJERCICIO 5
# Eliminar números duplicados de una lista
# ==============================

# Lista original con números repetidos
numeros = [1,1,2,3,3,2,5,6,2,7,8,4,3,1]

# Lista vacía donde se guardarán los números sin repetir
sin_duplicados = []

# Se recorren todos los números de la lista original
for n in numeros:
    # Si el número no está en la nueva lista, se agrega
    if n not in sin_duplicados:
        sin_duplicados.append(n)

# Se muestran ambas listas
print("\nLista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)
