# Actividad 1 - Ciencia de datos

## DeportivaMX

---

## Perfiles de ciencia de datos

Los siguientes perfiles son necesarios para poder controlar el crecimiento acelarado de la empresa:

### Cientifico de datos

Encargado de analizar y manejar los datos ademas de crear modelos de prediccion

**Justificacion**
Facilita identificar patrones de compra y mejorar la toma de decisiones

---

### Ingeniero de datos

Diseña la infraestructura, optimiza el rendimiento y gestiona la seguridad para proteger los datos

**Justificacion**
Asi la empresa al manejar grandes volumenes de datos con una mejor optimizacion de rendimiento en la infraestrutura y asegurar los datos del cliente

---

### Analista de datos

Analiza e interpreta los datos y genera informe

**Justificacion**
Transforma los datos en informacion mas comprensible y visual para el resto del equipo

---

## Las 5 V del Big data

### Volumen

Con el crecimiento de acelerado del negocio este genera grades cantidades de datos por las ventas, usuarios y productos

### Velocidad

Como los datos se generan en tiempo real se requiere que se procesen y analicen rapido para tomar buenas decisiones

### Variedad

Los datos provienen de diferentes fuentes de manera estructurada para las ventas, no estructurada para las reseñas y semiestructurada para los diferentes productos

### Veracidad

Se  garantiza la calidad de datos evitando qe se dupliquen o se ingrese informacion incorrecta o incompleta de los clientes

### Valor

Los datos deben generar beneficios para la empresa identificando los productos mas vendidos para enfocar los esfuersos en estos a nivel de marketing y inventario

---

## Arquitectura de almacenamiento

### Arquitectura seleccionada

Data Lake

**Justificacion**
El Data Lake permite almacenar grandes volúmenes de datos en su formato original, sin necesidad de estructurarlos previamente. Esto resulta ideal para DeportivaMX, ya que la empresa está en una etapa de crecimiento acelerado y maneja datos provenientes de múltiples fuentes, como ventas, clientes y productos ademas de que es escalable, flexible y de bajo costo.

---

### Base datos NoSQL

MongoDB

**Justificacion**

- Maneja datos no estruturados
- Usa formato JSON
- Permite consultas rapidas
- Permite la escalabilidad horizontal
- Facilita el manejo de grandes volumeness de informacion
- Es facil de usar

---

## Diseño de colecciones en JSON

### Coleccion: clientes

```json
{
  "_id": "ObjectId",
  "nombre": "Juan Pérez",
  "email": "juan@email.com",
  "telefono": "5512345678",
  "direccion": {
    "ciudad": "CDMX",
    "codigo_postal": "01234"
  },
  "fecha_registro": "2026-03-01"
}
```

### Coleccion: productos

```json
{
  "_id": "ObjectId",
  "nombre": "Tenis deportivos",
  "categoria": "Calzado",
  "precio": 1200,
  "stock": 50,
  "marca": "Nike"
}
```

### Coleccion: ventas

```json
{
  "_id": "ObjectId",
  "cliente_id": "ObjectId",
  "fecha": "2026-03-10",
  "productos": [
    {
      "producto_id": "ObjectId",
      "cantidad": 2,
      "precio_unitario": 1200
    }
  ],
  "total": 2400,
  "metodo_pago": "Tarjeta"
}
```

### Coleccion: reseñas

```json
{
  "_id": "ObjectId",
  "producto_id": "ObjectId",
  "cliente_id": "ObjectId",
  "calificacion": 5,
  "comentario": "Excelente producto",
  "fecha": "2026-03-12"
}
```

---

# Ejercicios complementarios

---

## Ejercicios de matematicas y algebra basica

### Ejercicio 1: Operaciones Algebraicas Básicas

Resolver las siguientes operaciones:

```
a) 3x + 5 = 17      → 3x = 17 - 5 → 3x = 12 → x = 12/3 → x = 4
b) 2y - 8 = 22      → 2y = 22 + 8 → 2y = 30 → y = 30/2 → y = 15
c) 4z + 3 = 3z + 10 → 4z - 3z = 10 - 3 → 1z = 7 → z = 7/1 → z = 7
d) 5(x + 2) = 35    → 5x + 10 = 35 → 5x = 35 - 10 → 5x = 25 → x = 25/5 → x = 5
```

### Ejercicio 2: Funciones Lineales

Dada la función f(x) = 2x + 3:

- Calcular f(0), f(1), f(5), f(10)
- Graficar la función e identificar la pendiente y ordenada al origen

```
f(0) = 2(0) + 3 → f(0) = 3
f(1) = 2(1) + 3 → f(1) = 2 + 3 → f(1) = 5
f(5) = 2(5) + 3 → f(5) = 10 + 3 → f(1) = 13
f(10) = 2(10) + 3 → f(10) = 20 + 3 → f(10) = 23
```

Segun la formula general de linea recta: y = mx + b

- La pendiente: 2
- la ordenada al origen: 3

**Grafica:**
![Grafica de la funcion](img/Graficaeje1.png)

### Ejercicio 3: Escalas y Volúmenes (Big Data)

Expresar en notación científica:

| Cantidad                    | Notación Científica |
| --------------------------- | ------------------- |
| 1,000,000 bytes             | 10⁶                 |
| 1,000,000,000 registros     | 10⁹                 |
| 1,000,000,000,000 bytes     | 10¹²                |

---

## Ejercicios de logica computacional

### Ejercicio 4: Diagramas de Flujo

Diseñar un algoritmo simple para:

1. Determinar si un número es par o impar
2. Calcular el promedio de 3 números
3. Encontrar el mayor de 4 números

```
Algoritmo Ejercicio4
  Definir num1, num2, num3, num4, promedio como real

  Escribir "Ingrese el primer numero"
  Leer num1
  Escribir "Ingrese el segundo numero"
  Leer num2 
  Escribir "Ingrese el tercer numero"
  Leer num3
  Escribir "Ingrese el cuarto numero"
  Leer num4

  Si num1 % 2 == 0 Entonces
    Escribir num1, " Es par"
  Sino
    Escribir num1, " Es impar"
  FinSi

  promedio = (num1+num2+num3)/3
  Escribir "El promedio de los numeros", num1, ",", num2, " y ", num3, " es: ", promedio

  Si num1 >= num2 Y num1 >= num3 Y num1 >= num4 Entonces
    Escribir num1, "Es el mayor de los 4 numeros"
  Sino Si num2 >= num1 Y num2 >= num3 Y num2 >= num4 Entonces
    Escribir num2, "Es el mayor de los 4 numeros"
  Sino si num3 >= num1 Y num3 >= num2 Y num3 >= num4 Entonces
    Escribir num3, "Es el mayor de los 4 numeros"
  Sino
    Escribir num4, "Es el mayor de los 4 numeros"
FinAlgoritmo
```

### Ejercicio 5: Pseudocódigo

Escribir pseudocódigo para:

1. Calcular el factorial de un número
2. Buscar un elemento en una lista
3. Ordenar una lista de números

```
Algoritmo Ejercicio5
  Definir n, i, lista1, lista2, elemento, factorial, j, tam como entero
  Definir encontrado como logico

  Escribir "Ingrese un numero"
  Leer n

  factorial = 1

  Para i = 1 Hasta n Hacer
    factorial = factorial * i
  FinPara

  Escribir "El factorial de ", n, " es: ", factorial

  Escribir "Ingrese el tamaño de la lista"
  Leer tam

  Dimension lista1[tam]

  Para i = 1 Hasta n Hacer
    Escribir "Ingrese el valor ", i
    Leer lista1[i]
  FinPara

  Escribir "Ingrese el elemento a buscar"
  Leer elemento

  encontrado = Falso

  Para i = 1 Hasta n Hacer
    Si lista1[i] == elemento Entonces
      encontrado = Verdadero
    FinSi
  FinPara

  Si encontrado Entonces
    Escribir "Elemento encontrado"
  Sino
    Escribir "Elemento no encontrado"
  FinSi

  Escribir "Ingrese el tamaño de la lista"
  Leer n

  Dimension lista2[n]

  Para i = 1 Hasta n Hacer
    Escribir "Ingrese el valor ", i
    Leer lista2[i]
  FinPara

  Para i = 1 Hasta n-1 Hacer
    Para j = 1 Hasta n-1 Hacer
      Si lista2[j] > lista2[j+1] Entonces
        temp = lista2[j]
        lista2[j] = lista2[j+1]
        lista2[j+1] = temp
      FinSi
    FinPara
  FinPara

  Escribir "Lista ordenada:"
  Para i = 1 Hasta n Hacer
    Escribir lista2[i]
  FinPara
```

### Ejercicio 6: Operaciones Booleanas

Evaluar las siguientes expresiones:

```python
a = True
b = False
c = True

# Evaluar:
print(a and b)      # False
print(a or b)      # True
print(not b)       # True
print(a and c)     # True
print((a or b) and c)  # True
```

---

## Ejercicios de investigacion

### Ejercicio 7: Historia de la Ciencia de Datos

Investigar y responder:

1. ¿Quién es considerada la primera científica de datos?
Ada Lovelace es reconocida como la primera cientifca de datos por que escribio el primer algoritmo de la historia antes del uso de las computadoras para procesar datos
2. ¿Qué es el "Data Science Venn Diagram" de Drew Conway?
Es un modelo que describe las habilidades necesarias para la ciencia de datos y se compone de 3 areas principales: programacion, conocimiento en matematicas y estadistica, y conocimiento del dominio
3. Menciona 3 herramientas modernas de Big Data

- **Apache Hadop**: que permite alamacenar y procesar grandes cantidades de datos de manera distribuida
- **Apache Spark**: procesa rapido datos en una memoria y analiza en tiempo real
- **MongoDB**: Base de datos orientada a documentos JSON y se usa bastante para datos semiestructurados

### Ejercicio 8: Aplicaciones de Big Data

Investigar un caso de uso real de Big Data en:

- Salud: en salud Mayo Clinic usa Big Daata para historiales clinicos, imagenes medicas y datos geneticos ya que son millones de registros, detectar patrones de enfermedades y mejora los diagnosticos
- Finanzas: en finanzas PayPal usa Big Data para detectar fraudes en tiempo real ya que analiza transacciones en milisegundos, detecta y bloquea comportamientos sospechosos
- Redes sociales: en las Redes sociales, Facebook usa Big Data para personalizar el contenido que ves en base a la manera en que interactuamos con el contenido que vemos asi prediciendo que nos interesa y mejorando nuestra experencia como usuario
- Deportes: en los deportes el equipo del FC Barcelona utiliza Big Data para mejorar el rendimiento de sus jugadores analizando los datos de los partidos para medir su rendimiento fisico y prevenir lesiones

---

# Actividades Propuestas

---

## Actividad 1.1: Investigación de Conceptos Fundamentales

**Descripción:** Investiga y resume los conceptos básicos de la ciencia de datos.

**Instrucciones:**

1. Define qué es la ciencia de datos y menciona sus componentes principales
2. Explica la diferencia entre datos estructurados y no estructurados
3. Investiga qué son las 5 V del Big Data y da un ejemplo de cada una
4. Crea un mapa conceptual con los diferentes perfiles profesionales en ciencia de datos

## 1. ¿Qué es la ciencia de datos?

La ciencia de datos es un campo interdisciplinario que combina estadística, programación y conocimiento del dominio para analizar datos y extraer información útil que apoye la toma de decisiones.

### Componentes principales

- **Estadística y matemáticas**: para el análisis de datos  
- **Programación**: para procesar grandes volúmenes de datos  
- **Conocimiento del dominio**: para interpretar los resultados  

---

## 2. Diferencia entre datos estructurados y no estructurados

### Datos estructurados

- Tienen un formato definido (tablas)
- Ejemplo: bases de datos SQL

### Datos no estructurados

- No tienen un formato fijo
- Ejemplo: imágenes, videos, texto

---

## 3. Las 5 V del Big Data

### Volumen

Gran cantidad de datos  
**Ejemplo:** millones de transacciones en una tienda en línea  

### Velocidad

Rapidez con la que se generan los datos  
**Ejemplo:** datos en tiempo real de compras  

### Variedad

Diferentes tipos de datos  
**Ejemplo:** texto, imágenes, videos  

### Veracidad

Calidad y confiabilidad de los datos  
**Ejemplo:** evitar datos duplicados o incorrectos  

### Valor

Capacidad de generar beneficios  
**Ejemplo:** mejorar ventas mediante análisis de clientes  

---

## 4. Mapa conceptual (perfiles de ciencia de datos)

Ciencia de Datos
│
├── Científico de Datos
│   ├── Modelos predictivos
│   └── Análisis avanzado
│
├── Ingeniero de Datos
│   ├── Infraestructura
│   └── Procesamiento de datos
│
├── Analista de Datos
│   ├── Reportes
│   └── Visualización
│
└── Ingeniero de Machine Learning
    ├── Implementación de modelos
    └── Automatización

---

## Actividad 1.2: Análisis de Casos de Uso

**Descripción:** Analiza casos reales de aplicación de ciencia de datos.

**Instrucciones:**

1. Investiga 3 empresas que utilizan ciencia de datos (ej: Netflix, Amazon, Spotify)
2. Para cada empresa, identifica:
   - Qué tipo de datos recopilan
   - Qué técnicas de análisis utilizan
   - Qué problemas resuelven con los datos
3. Crea una presentación breve resumiendo tus hallazgos

## 1.Netflix

### Datos que recopila

- Historial de visualización  
- Calificaciones  
- Tiempo de reproducción  

### Técnicas utilizadas

- Machine Learning  
- Sistemas de recomendación  

### Problema que resuelve

- Personalizar contenido para cada usuario  

---

## 2.Amazon

### Datos que recopila

- Compras realizadas  
- Búsquedas  
- Carrito de compras  

### Técnicas utilizadas

- Análisis predictivo  
- Recomendaciones  

### Problema que resuelve

- Aumentar ventas y mejorar experiencia del cliente  

---

## 3.Spotify

### Datos que recopila

- Canciones escuchadas  
- Listas de reproducción  
- Interacciones del usuario  

### Técnicas utilizadas

- Machine Learning  
- Análisis de comportamiento  

### Problema que resuelve

- Recomendar música personalizada  

---

## Actividad 1.3: Configuración del Entorno de Trabajo

**Descripción:** Prepara tu entorno de trabajo para el curso.

**Instrucciones:**

1. Instala Python (si no lo tienes)
2. Instala las librerías principales:
   - NumPy
   - Pandas
   - Matplotlib
   - Seaborn
   - Scikit-learn
3. Verifica la instalación ejecutando un script básico
4. Crea un cuaderno Jupyter con un ejemplo de carga de datos

```python
import pandas as pd

data = {
    "nombre": ["Erick", "Daisy", "Israel"],
    "edad": [19, 18, 18],
    "ciudad": ["CDMX", "Guadalajara", "Monterrey"]
}

df = pd.DataFrame(data)

print(df)
```

---

## Actividad 1.4: Exploración de Fuentes de Datos

**Descripción:** Explora diferentes fuentes de datos disponibles.

**Instrucciones:**

1. Investiga qué es Kaggle y cómo puedes usarlo
2. Explora al menos 3 datasets públicos en Kaggle
3. Identifica qué tipo de datos contiene cada uno
4. Elige un dataset que te interese y describe:
   - Qué información contiene
   - Qué preguntas podrías responder con esos datos

### 1. ¿Qué es Kaggle?

Es una plataforma en línea utilizada por científicos de datos para acceder a datasets, participar en competencias y desarrollar proyectos de análisis.

Se puede utilizar para:

- Descargar datasets reales
- Practicar análisis de datos
- Crear y compartir notebooks
- Participar en competencias de machine learning

### 2. Datasets explorados

#### Dataset 1: Titanic

- Tipo de datos: estructurados  
- Contenido:
  - Información de pasajeros (edad, sexo, clase)
  - Datos de supervivencia  

---

#### Dataset 2: Netflix Movies and TV Shows

- Tipo de datos: semiestructurados  
- Contenido:
  - Títulos, géneros, fechas de lanzamiento
  - Descripciones de contenido  

---

#### Dataset 3: COVID-19 Dataset

- Tipo de datos: estructurados  
- Contenido:
  - Número de casos por país
  - Muertes y recuperaciones  

---

### 3. Dataset seleccionado: Titanic

#### Información que contiene

El dataset del Titanic incluye información sobre los pasajeros del barco, como:

- Edad  
- Sexo  
- Clase social  
- Precio del boleto  
- Puerto de embarque  
- Estado de supervivencia  
