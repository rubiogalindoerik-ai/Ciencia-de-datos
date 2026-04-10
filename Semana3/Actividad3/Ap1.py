import pandas as pd

# 1. LISTAS

# Lista de números
numeros = [1, 2, 3, 4, 5]

# List comprehension: obtener cuadrados
cuadrados = [x**2 for x in numeros]

print("Lista original:", numeros)
print("Cuadrados:", cuadrados)

# 2. DICCIONARIOS

# Diccionario con información de una persona
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Querétaro"}

print("\nDiccionario:", persona)
print("Nombre:", persona["nombre"])

# 3. DATAFRAME

# Crear DataFrame con pandas
data = {
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Edad": [23, 30, 28],
    "Calificacion": [90, 85, 88],
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# 4. FUNCIONES LAMBDA

# Función lambda para sumar dos números
suma = lambda a, b: a + b

print("\nLambda suma:", suma(5, 3))

# Usar lambda con map
dobles = list(map(lambda x: x * 2, numeros))
print("Dobles:", dobles)

# 5. MANEJO DE ERRORES

try:
    numero = int(input("\nIngresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ValueError:
    print("Error: Debes ingresar un número válido.")

except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")

finally:
    print("Ejecución finalizada.")

# 6. EJERCICIOS BÁSICOS


# 🔹 Ejercicio 1: Suma de una lista
def suma_lista(lista):
    return sum(lista)


print("\nEjercicio 1:", suma_lista([1, 2, 3, 4]))


# 🔹 Ejercicio 2: Número par o impar
def es_par(numero):
    return "Par" if numero % 2 == 0 else "Impar"


print("Ejercicio 2:", es_par(7))


# 🔹 Ejercicio 3: Contar vocales en una cadena
def contar_vocales(texto):
    vocales = "aeiou"
    return sum(1 for letra in texto.lower() if letra in vocales)


print("Ejercicio 3:", contar_vocales("Hola Mundo"))


# 🔹 Ejercicio 4: Encontrar el número mayor
def numero_mayor(lista):
    return max(lista)


print("Ejercicio 4:", numero_mayor([3, 9, 1, 6]))


# 🔹 Ejercicio 5: Filtrar números mayores a 5
def mayores_a_cinco(lista):
    return [x for x in lista if x > 5]


print("Ejercicio 5:", mayores_a_cinco([2, 6, 8, 1, 4]))
