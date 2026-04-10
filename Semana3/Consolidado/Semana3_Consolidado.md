# Avance de proyecto - Ciencia de datos

---

## Mercado inmobilario

---

#### Descripcion

En esta fase inicial, comenzarás tu inmersión en el análisis predictivo del mercado inmobiliario. Se te proporcionará una base de datos, que contiene datos cruciales sobre el mercado inmobiliario, que incluye, pero no se limita a precios, ubicaciones y características físicas de las propiedades. Llevarás a cabo un análisis exploratorio de datos (EDA) profundo para familiarizarte con estos, prepararlos para el análisis y descubrir patrones iniciales, tendencias y posibles anomalías. Este paso es esencial para cualquier proyecto de ciencia de datos, ya que establece una base sólida para el modelado predictivo posterior.

---

#### Objetivo

Realizar un análisis exploratorio para comprender las características fundamentales, tendencias y patrones de los datos relacionados con el mercado inmobiliario.

---

### Instrucciones

Para llevar a cabo esta actividad, utilizarás la siguiente base de datos: <https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction>  

#### Parte 1: Base de datos  

Carga la base de datos a Python e importa las librerías que utilizarás a lo largo de todo el análisis.  

#### Parte 2: Análisis Exploratorio de Datos (EDA)  

- **Análisis descriptivo:** calcula estadísticas para cada variable (media, mediana, desviación estándar, etc.). Identifica las variables que podrían influir más en el precio de una vivienda.

- **Visualización de datos:** Genera visualizaciones que ayuden a entender la distribución de las variables más importantes, la relación entre el precio de la vivienda y otras variables para identificar patrones o tendencias. Utiliza Matplotlib, Seaborn o cualquier otra biblioteca de visualización en Python. Ejemplos de gráficos a considerar incluyen histogramas, box plots, scatter plots y mapas de calor para correlaciones.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train2.csv")

# Analisis
print("Información del dataset:")
df.info()
df.describe()
print("Mediana:\n", df.median(numeric_only=True))
print("\nDesviación estándar:\n", df.std(numeric_only=True))

# Histrograma
plt.figure()
plt.hist(df["price"], bins=50)
plt.title("Distribución de precios")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.savefig("hist_precio.png")
plt.show()

# Boxplot
plt.figure()
sns.boxplot(x=df["price"])
plt.title("Boxplot del precio")
plt.savefig("boxplot_precio.png")
plt.show()

# Grafico de barras
plt.figure()
df["room_type"].value_counts().plot(kind="bar")
plt.title("Tipo de habitación")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.savefig("barras_room_type.png")
plt.show()

# Scatter
plt.figure()
plt.scatter(df["availability_365"], df["price"])
plt.xlabel("Disponibilidad")
plt.ylabel("Precio")
plt.title("Precio vs Disponibilidad")
plt.savefig("scatter_precio_disponibilidad.png")
plt.show()

# Mapa de calor
plt.figure()
corr = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr, annot=True)
plt.title("Correlación entre variables")
plt.savefig("heatmap.png")
plt.show()
```

---

## Ejercicios complementarios

---

### Ejercicios de Python Básico

#### Ejercicio 1: Variables y Tipos de Datos

```python
# Ejercicios:
# 1. Crear variables de diferentes tipos: int, float, str, bool, list, dict
# 2. Convertir tipos: str a int, float a int, int a float
# 3. Usar f-strings para formatear: "El usuario tiene X años"

entero = 19
flotante = 1.0
texto = "Erick"
boleano = True
lista = ["Uno", "Dos", "Tres", "Cuatro"]
diccionario = {"Nombre": "Erick", "Edad": 19}

str_int = "1"
int(str_int)
flo_int = 1.0
int(flo_int)
int_flo = 2
int(int_flo)

print(f"El nombre del usuario es {texto} y tiene {entero}")
```

#### Ejercicio 2: Control de Flujo

```python
# # Ejercicios:
# 1. Crear un programa que determine si un número es positivo, negativo o cero
# 2. Crear un menú con if-elif-else
# 3. Usar un loop for para iterar sobre una lista
# 4. Usar while para calcular factorial

lisnumero = [1, 2, 3, 5, 6, 4, 8, 3, 5, 7, 5]
print("----------------------Menu-----------------------")
print("1. Determinar si un numero es +,- o 0")
print("2. Usar un loop for para iterar sobre una lista")
print("3. Usar un ciclo while para calcular un factorial")
op = int(input("Ingresa el numero de opcion: "))
if op == 1:
    num = int(input("Ingresa el numero a determinar: "))
    if num > 0:
        print("El numero es positivo")
    elif num < 0:
        print("El numero es negativo")
    elif num == 0:
        print("El numero es 0")
elif op == 2:
    for x in lisnumero:
        print(x)
elif op == 3:
    numf = int(input("Ingrese el numero para sacar factorial: "))
    numf2 = numf
    while numf2 > 1:
        numf2 = numf2 - 1
        print(numf2)
        numf = numf * numf2
    print(f"El numero en factorial es: {numf}")
else:
    print("Opcion no valida")
```

#### Ejercicio 3: Funciones

```python
# # Crear funciones para:
# 1. Calcular el área de un círculo
# 2. Convertir Celsius a Fahrenheit
# 3. Calcular el promedio de una lista
# 4. Encontrar el valor máximo y mínimo
promlist = [10, 8, 9, 7, 10, 6]
total = 0
print("----------------------Menu-----------------------")
print("1. Calcular area de un circulo")
print("2. Conevrtir Celsius a Fahrenheit")
print("3. Calcular el promedio de una lista")
print("4. Encontrar el valor maximo y minimo")
op = int(input("Ingresa el numero de opcion: "))
if op == 1:
    radius = int(input("Ingresa el radio: "))
    pi = 3.1416
    area = pi * (radius ^ 2)
    print(f"El area del circulo es: {area}")
elif op == 2:
    tempc = int(input("Ingresa la temperatura en celsius"))
    tempf = (1.8 * tempc) + 32
    print(f"Temperatura en Fahrenheit: {tempf}")
elif op == 3:
    for x in promlist:
        total = total + x
    prom = total / len(promlist)
elif op == 4:
    for x in promlist:
        print(x)
    print(f"Valor maximo de la lista: {max(promlist)}")
    print(f"Valor minimo de la lista: {min(promlist)}")
```

---

### Ejercicios de NumPy

#### Ejercicio 4: Operaciones con Arrays

```python
import numpy as np

# Crear arrays y realizar operaciones:
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Ejercicios:
# 1. Sumar los arrays elemento a elemento
# 2. Multiplicar por un escalar
# 3. Calcular la media, mediana y desviación estándar
# 4. Encontrar valores únicos
# 5. Reshape de un array 1D a 2D

suma = arr1 + arr2
mul1 = arr1 * 2
mul2 = arr2 * 2
media1 = sum(arr1) / len(arr1)
media2 = sum(arr2) / len(arr2)
mediana1 = np.median(arr1)
mediana2 = np.median(arr2)
desviacion1 = np.std(arr1, ddof=1)
desviacion2 = np.std(arr2, ddof=1)
unic1 = np.unique(arr1)
unic2 = np.unique(arr2)
new_arr1 = arr1.reshape(2, 3)
new_arr2 = arr2.reshape(2, 3)
```

#### Ejercicio 5: Álgebra con NumPy

```python
# Dados los vectores v1 = [1, 2, 3] y v2 = [4, 5, 6]
# Calcular:
# 1. Producto punto
# 2. Producto cruz
# 3. Magnitud de cada vector
# 4. Normalización de vectores}

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

pputo = np.dot(v1, v2)
pcruz = np.cross(v1, v2)
magnitud1 = np.linalg.norm(v1)
magnitud2 = np.linalg.norm(v2)
normalizado1 = v1 / magnitud1
normalizado2 = v2 / magnitud2
```

---

### Ejercicios de Pandas

#### Ejercicio 6: DataFrames Básico

```python
import pandas as pd

# Crear un DataFrame con datos de estudiantes
data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofia'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

# Ejercicios:
# 1. Seleccionar columna 'nombre'
# 2. Filtrar estudiantes con promedio > 8.5
# 3. Ordenar por edad
# 4. Agregar columna 'aprobado' (promedio >= 7)
# 5. Group by carrera y promediar

df["nombre"]
df[df["promedio"] > 8.5]
ordenado = df.sort_values(by="edad")
df["aprobado"] = df["promedio"] >= 7
promecarrera = df.groupby("carrera").numeric_only().mean()
```

#### Ejercicio 7: Manipulación de Datos

```python
# Dado el DataFrame anterior:
# 1. Manejar valores faltantes (agregar NaN y llenarlos)
# 2. Eliminar duplicados
# 3. Aplicar funciones con apply()
# 4. Usar loc e iloc para slicing
# 5. Concatenar dos DataFrames

df.loc[0, "promedio"] = np.nan
df["promedio"] = df["promedio"].fillna(df["promedio"].mean())
df = df.drop_duplicates()
df["estatus"] = df["promedio"].apply(lambda x: "Excelente" if x >= 9.0 else "Regular")
vista_loc = df.loc[0:2, ["nombre", "promedio"]]
vista_iloc = df.iloc[0, 0:2]
nuevos_estudiantes = pd.DataFrame(
    {
        "nombre": ["Pedro", "Lucía"],
        "edad": [24, 21],
        "carrera": ["Ing", "Lic"],
        "promedio": [8.0, 9.2],
    }
)
df_total = pd.concat([df, nuevos_estudiantes], ignore_index=True)
```

---

### Ejercicios de Visualización

#### Ejercicio 8: Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear visualizaciones:
# 1. Gráfico de línea básico
# 2. Gráfico de dispersión
# 3. Histograma
# 4. Gráfico de barras
# 5. Personalizar: títulos, etiquetas, leyenda, colores
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 2 - 1
data_hist = np.random.randn(1000)
categories = ["A", "B", "C", "D"]
values = [23, 45, 12, 30]

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Seno(x)", color="blue", linestyle="-", linewidth=2)
plt.title("Gráfico de Línea - Función Seno")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(
    x_scatter,
    y_scatter,
    label="Datos Aleatorios",
    color="purple",
    marker="o",
    s=50,
    alpha=0.6,
)
plt.title("Gráfico de Dispersión")
plt.xlabel("Valores X")
plt.ylabel("Valores Y")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(
    data_hist, bins=30, label="Frecuencia", color="green", edgecolor="black", alpha=0.7
)
plt.title("Histograma de Datos")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.bar(
    categories,
    values,
    label="Ventas por Categoría",
    color=["coral", "teal", "gold", "orchid"],
    edgecolor="navy",
)
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.legend()
plt.grid(axis="y")
plt.show()

```

#### Ejercicio 9: Análisis Exploratorio

```python
# Usando un dataset (puede ser 'iris' o cualquier otro)
import pandas as pd
import seaborn as sns

# Ejercicios:
# 1. Cargar dataset y mostrar info básica
# 2. Calcular estadísticas descriptivas
# 3. Crear histogramas de todas las columnas numéricas
# 4. Crear matriz de correlación
# 5. Crear boxplots por categoría
# 6. Identificar outliers

df = sns.load_dataset("iris")

print("--- Información Básica ---")
print(df.info())
print("\n--- Primeras 5 filas ---")
print(df.head())

print("\n--- Estadísticas Descriptivas ---")
print(df.describe())

df.select_dtypes(include=["number"]).hist(
    figsize=(10, 8), color="skyblue", edgecolor="black"
)
plt.suptitle("Distribución de Variables Numéricas", fontsize=16)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
corr_matrix = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="species", y="sepal_length", palette="Set2")
plt.title("Distribución de Sepal Length por Especie")
plt.show()


def identificar_outliers(columna):
    Q1 = columna.quantile(0.25)
    Q3 = columna.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return columna[(columna < limite_inferior) | (columna > limite_superior)]


print("\n--- Outliers Detectados ---")
for col in df.select_dtypes(include=["number"]).columns:
    outliers = identificar_outliers(df[col])
    if not outliers.empty:
        print(f"Columna '{col}' tiene {len(outliers)} outliers:\n{outliers.values}")
    else:
        print(f"Columna '{col}' no tiene outliers.")
```

---

### Ejercicios de Estadística

#### Ejercicio 10: Medidas de Tendencia Central

Calcular manualmente (sin funciones built-in):

| Datos       | Media | Mediana | Moda   |
| ----------- | ----- | ------- | ------ |
| [5, 3, 8, 3, 7] |  5.2   |    8    |    3   |
| [10, 20, 30, 40]|  25   |   25    | sin moda |
| [1, 2, 2, 3, 3, 3, 4]|  2.57  |   3    | 3 y 2  |

#### Ejercicio 11: Dispersion

Calcular:

| Datos                   | Rango | Varianza | Desviación Estándar |
| ----------------------- | ----- | -------- | ------------------- |
| [2, 4, 4, 4, 5, 5, 7, 9]  |   7   |    4     |          2          |
| [1, 3, 5, 7, 9]           |   8   |    8     |       2.83           |

---

### Ejercicios de Investigación

#### Ejercicio 12: El Proceso de Data Science

Investigar y explicar:

1. ¿Qué es el ciclo CRISP-DM?
El CRISP-DM (Cross Industry Standard Process for Data Mining) es una metodología estándar para desarrollar proyectos de ciencia de datos de forma estructurada.
2. ¿Cuáles son las fases del proceso de ciencia de datos?
Definición del problema, Recolección de datos, Limpieza y preparación, Análisis exploratorio (EDA), Modelado, Evaluación, Implementación y Monitoreo
3. ¿Qué es el MVP (Minimum Viable Product) en ciencia de datos?
El MVP (Minimum Viable Product) es una versión básica pero funcional de un modelo o solución.

#### Ejercicio 13: Caso de Estudio

Investigar un caso real de análisis exploratorio de datos:

- ¿Qué preguntas buscaban responder?
Usando como caso Netflix las preguntas son: Qué contenido le gusta a cada usuario?, Qué series/películas recomendar?, Qué tipo de contenido producir? y Cómo reducir la cancelación de usuarios (churn)?
- ¿Qué técnicas usaron?
Análisis exploratorio de datos (EDA), Sistemas de recomendación, Machine Learning, Clustering de usuarios y Análisis de comportamiento (clicks, tiempo de visualización)
- ¿Qué insights encontraron?
Los usuarios prefieren contenido personalizado, Las recomendaciones aumentan el tiempo de uso, Pueden predecir qué contenido será exitoso

---

## Actividades practicas

---

### Actividad 3.1: Refuerzo de Python

**Descripción:** Repasa y practica conceptos de Python para análisis de datos.

**Instrucciones:**

1. Crea un script que demuestre:

   - Listas, diccionarios y DataFrames
   - Funciones lambda
   - List comprehensions
   - Manejo de errores

2. Resuelve 5 ejercicios de programación básica
3. Documenta tu código con comentarios

```python
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
```

---

### Actividad 3.2: Carga y Exploración de Datos

**Descripción:** Practica cargar y explorar datasets.

**Instrucciones:**

1. Descarga un dataset de Kaggle (recomendado: Titanic o Iris)
2. Carga los datos usando Pandas
3. Realiza las siguientes exploraciones:

   - Muestra las primeras 10 filas
   - Muestra información del dataset (info, describe)
   - Identifica tipos de datos
   - Identifica valores nulos
   - Muestra estadísticas básicas

4. Guarda los resultados en un cuaderno Jupyter

**El archivo Jupyter se encuentra en la carpeta Actividad3 como Ap2**

---

### Actividad 3.3: Limpieza de Datos

**Descripción:** Practica técnicas de limpieza de datos.

**Instrucciones:**

1. Continúa con el dataset de la actividad anterior
2. Realiza las siguientes operaciones:

   - Maneja valores nulos (elimina o imputa)
   - Elimina duplicados
   - Convierte tipos de datos si es necesario
   - Estandariza nombres de columnas
   - Crea nuevas columnas si es necesario

3. Muestra el estado de los datos antes y después

**El archivo Jupyter se encuentra en la carpeta Actividad3 como Ap2**

---

### Actividad 3.4: Visualización Exploratoria

**Descripción:** Crea visualizaciones exploratorias básicas.

**Instrucciones:**

1. Usa el dataset limpiado
2. Crea las siguientes visualizaciones:

   - Histograma de una variable numérica
   - Gráfico de barras de una variable categórica
   - Diagrama de dispersión de dos variables
   - Mapa de calor de correlaciones

3. Interpreta cada gráfica
4. Guarda las visualizaciones

**El archivo Jupyter se encuentra en la carpeta Actividad3 como Ap2**

---

## Practicas de clase

---

### Fundamentos de python

#### 1.1 Variables y Tipos de Datos

Las **variables** son contenedores que almacenan valores. En Python temos diferentes **tipos de datos**:

| Tipo | Descripción | Ejemplo |
|------|-------------|--------|
| `int` | Números enteros | `edad = 25` |
| `float` | Números decimales | `precio = 19.99` |
| `str` | Cadenas de texto | `nombre = "Ana"` |
| `bool` | Valores booleanos | `es_estudiante = True` |
| `list` | Listas ordenadas | `numeros = [1, 2, 3]` |
| `dict` | Diccionarios | `datos = {"nombre": "Ana"}` |

```python
# Ejemplo práctico: Creando variables de diferentes tipos

# Variables de diferentes tipos
edad = 25                    # int
altura = 1.75                # float
nombre = "María"             # str
es_estudiante = True        # bool
calificaciones = [8.5, 9.0, 7.8, 8.2]  # list
informacion = {"nombre": nombre, "edad": edad}  # dict

# Mostrando los valores
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} m")
print(f"Es estudiante: {es_estudiante}")
print(f"Calificaciones: {calificaciones}")
print(f"Información: {informacion}")
```

#### 1.2 Conversion de tipos

A veces necesitamos **convertir** un tipo de dato a otro. Esto se llama **casting**.

```python
# Ejemplo práctico: Conversión de tipos

# Convertir string a int
numero_str = "42"
numero_int = int(numero_str)
print(f"'{numero_str}' (str) → {numero_int} (int)")

# Convertir float a int (trunca la parte decimal)
pi = 3.14159
pi_entero = int(pi)
print(f"{pi} (float) → {pi_entero} (int)")

# Convertir int a float
numero = 5
numero_float = float(numero)
print(f"{numero} (int) → {numero_float} (float)")

# Convertir número a string
año = 2024
año_str = str(año)
print(f"{año} (int) → '{año_str}' (str)")
```

#### 1.3 Estructuras de Control: Condicionales

Los **condicionales** nos permiten ejecutar código basándonos en condiciones específicas.

```python
# Ejemplo práctico: Condicionales if-elif-else

def classify_number(n):
    """Clasifica un número como positivo, negativo o cero"""
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

# Probando la función
test_numbers = [-5, 0, 10, -3, 7]

for num in test_numbers:
    classification = classify_number(num)
    print(f"El número {num} es {classification}")
```

#### 1.4 Funciones

Las **funciones** son bloques de código reutilizables que realizan una tarea específica. Usar funciones nos ayuda a escribir código más limpio y modular.

```python
# Ejemplo práctico: Funciones útiles para ciencia de datos

import math

# Función 1: Área de un círculo
def area_circunferencia(radio):
    """Calcula el área de un círculo dado su radio"""
    return math.pi * radio ** 2

# Función 2: Convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# Función 3: Calcular el promedio de una lista
def calcular_promedio(lista):
    """Calcula el promedio de una lista de números"""
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Función 4: Encontrar valor máximo y mínimo
def max_min(lista):
    """Encuentra el valor máximo y mínimo de una lista"""
    return max(lista), min(lista)

# Probando las funciones
print(f"Área de un círculo con radio 5: {area_circunferencia(5):.2f}")
print(f"25°C en Fahrenheit: {celsius_a_fahrenheit(25):.2f}°F")
print(f"Promedio de [10, 20, 30, 40, 50]: {calcular_promedio([10, 20, 30, 40, 50])}")
print(f"Máximo y mínimo de [3, 1, 4, 1, 5]: {max_min([3, 1, 4, 1, 5])}")
```

---

### 2. NumPy: Computación Numérica

#### 2.1 Operaciones basicas con Arrays

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# 1. Sumar arrays elemento a elemento
suma = arr1 + arr2
print(f"arr1 + arr2 = {suma}")

# 2. Multiplicar por un escalar
multiplicado = arr1 * 3
print(f"arr1 * 3 = {multiplicado}")

# 3. Calcular media, mediana y desviación estándar
datos = np.array([10, 20, 30, 40, 50])
print(f"Media: {np.mean(datos)}")
print(f"Mediana: {np.median(datos)}")
print(f"Desviación estándar: {np.std(datos):.2f}")

# 4. Encontrar valores únicos
arr_con_duplicados = np.array([1, 2, 2, 3, 3, 3, 4])
unicos = np.unique(arr_con_duplicados)
print(f"Valores únicos en {arr_con_duplicados}: {unicos}")
```

#### 2.2 Álgebra con NumPy

```python
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# 1. Producto punto (dot product)
producto_punto = np.dot(v1, v2)
print(f"Producto punto de {v1} y {v2}: {producto_punto}")

# 2. Producto cruz (cross product)
producto_cruz = np.cross(v1, v2)
print(f"Producto cruz de {v1} y {v2}: {producto_cruz}")

# 3. Magnitud de cada vector
magnitud_v1 = np.linalg.norm(v1)
magnitud_v2 = np.linalg.norm(v2)
print(f"|v1| = {magnitud_v1:.2f}")
print(f"|v2| = {magnitud_v2:.2f}")

# 4. Normalización de vectores
v1_normalizado = v1 / np.linalg.norm(v1)
v2_normalizado = v2 / np.linalg.norm(v2)
print(f"v1 normalizado: {v1_normalizado}")
print(f"v2 normalizado: {v2_normalizado}")
```

---

### 3. Pandas: Manipulación de Datos

**Pandas** es la librería principal para manipulación y análisis de datos. Proporciona estructuras de datos flexibles para manejar datos tabulares.

#### 3.1 Operaciones Básicas con DataFrames

```python
import pandas as pd

data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofía'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

# 1. Seleccionar columna 'nombre'
nombres = df['nombre']
print("Nombres:", nombres.tolist())

# 2. Filtrar estudiantes con promedio > 8.5
destacados = df[df['promedio'] > 8.5]
print("\nEstudiantes con promedio > 8.5:")
print(destacados)

# 3. Ordenar por edad
ordenado = df.sort_values('edad')
print("\nEstudiantes ordenados por edad:")
print(ordenado)

# 4. Agregar columna 'aprobado' (promedio >= 7)
df['aprobado'] = df['promedio'] >= 7
print("\nDataFrame con columna 'aprobado':")
print(df)
```

```python
import pandas as pd

data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofía'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

# 5. Group by carrera y promediar
promedio_por_carrera = df.groupby('carrera')['promedio'].mean()
print("Promedio por carrera:")
print(promedio_por_carrera)
```

#### 3.2 Manipulación Avanzada de Datos

```python
import pandas as pd
import numpy as np

data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofía'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

# 1. Manejar valores faltantes
# Agregar un valor nulo
df_con_nulos = df.copy()
df_con_nulos.loc[2, 'promedio'] = np.nan
print("DataFrame con valor nulo:")
print(df_con_nulos)

# Llenar valores nulos con el promedio
df_lleno = df_con_nulos.fillna(df_con_nulos['promedio'].mean())
print("\nDataFrame con valores nulos llenados:")
print(df_lleno)

# 2. Usar loc para selección por etiqueta
print("\nUsando loc (fila con etiqueta '2'):")
print(df.loc[2])

# 3. Usar iloc para selección por índice
print("\nUsando iloc (primeras 3 filas):")
print(df.iloc[:3])
```

---

### 4. Visualización con Matplotlib

**Matplotlib** es la librería principal para crear visualizaciones estáticas, animadas e interactivas en Python.

#### 4.1 Diferentes Tipos de Gráficas

```python
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))

# 1. Gráfico de dispersión
plt.subplot(2, 2, 1)
x_disp = np.random.randn(50)
y_disp = np.random.randn(50)
plt.scatter(x_disp, y_disp, alpha=0.6, color='purple')
plt.title('Gráfico de Dispersión')
plt.xlabel('X')
plt.ylabel('Y')

# 2. Histograma
plt.subplot(2, 2, 2)
datos_hist = np.random.randn(1000)
plt.hist(datos_hist, bins=30, color='steelblue', edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# 3. Gráfico de barras
plt.subplot(2, 2, 3)
categorias = ['Ing', 'Lic', 'Doc', 'Arq']
valores = [45, 30, 15, 10]
plt.bar(categorias, valores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.title('Gráfico de Barras')
plt.xlabel('Carrera')
plt.ylabel('Cantidad')

# 4. Boxplot
plt.subplot(2, 2, 4)
datos_box = [np.random.normal(0, 1, 100),
            np.random.normal(0, 1.5, 100),
            np.random.normal(0, 2, 100)]
plt.boxplot(datos_box, labels=['Grupo A', 'Grupo B', 'Grupo C'])
plt.title('Boxplot')
plt.ylabel('Valor')

plt.tight_layout()
plt.show()
```
