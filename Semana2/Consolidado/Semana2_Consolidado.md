# Actividad 2 - Ciencia de datos

---

## Todo ventas en Línea, S.A. de C.V

---

Imagina que eres el responsable de un proyecto de reciente creación, cuyo objetivo es examinar un conjunto de datos que contiene información sobre ventas de productos de una tienda en línea llamada "Todo ventas en Línea, S.A. de C.V." durante un período de tiempo. Se te pide realizar un análisis exploratorio de los datos para comprender de manera más profunda el rendimiento de las ventas y extraer información valiosa que contribuya a la toma de decisiones comerciales para el presente año. De la información que obtengas dependerán todas las estrategias comerciales de la organización para determinar qué producto vender más, a qué nicho de mercado dirigirse y en qué época del año reforzar las promociones.

---

## Instrucciones

Lee detenidamente las siguientes indicaciones para poder realizar la actividad:

1. **Lee los temas 5, 6, 7 y 8.**
2. **Accede a tu entorno de desarrollo de código.**
3. **Definición del problema y recopilación de datos**
   - Redacta el objetivo del proyecto y las preguntas clave que se buscan responder.
4. **Utiliza Python para generar, de manera aleatoria, los conjuntos de datos necesarios** para el ejercicio propuesto. Los conjuntos de datos deben cumplir con los siguientes requisitos:
   - Incluir al menos 10 columnas: cuatro de tipo numérico (entero o decimal), dos de tipo categórico (texto breve que representa una categoría), dos de tipo estructurado (datos con una organización predefinida) y dos de tipo no estructurado (texto libre, etc.).
   - Contener al menos 5,000 registros.

```python
from faker import Faker
import random

fake = Faker('es_MX')

def generate_Data(n=5000):
    data = [ ]
    for _ in  range(n):
        register = {
            "edad": random.randint(18,65),
            "salario": round(random.uniform(8000, 50000), 2),
            "experencia": random.randint(0, 40),
            "calificacion": round(random.uniform(1,5),1),
            "departamento": random.choice(["IT", "RH", "VH", "Finanzas"]),
            "educacion": random.choice(["Licenciatura", "Maestria", "Doctorado"]),
            "direccion": {
                "calle": fake.street_name(),
                "ciudad": fake.city(),
                "pais": fake.country()
            },
            "habilidades": random.sample(
                ["Python", "SQL", "Excel", "Java", "Comunicacion", "Liderazgo"],
                k=3
            ),
            "comentarios": fake.text(max_nb_chars=100),
            "descripcion": fake.sentence()
        }
        data.append(register)
    return data
```

1. **Preparación de los datos:**
   - Carga los datos a MongoDB.
   - Realiza una exploración inicial de los datos para comprender su estructura y calidad. Esta fase es crucial para identificar posibles problemas de calidad de datos, como valores faltantes o atípicos, y para entender la distribución y relaciones entre las variables.

```python
from pymongo import MongoClient
from faker import Faker
import random

fake = Faker('es_MX')

def generate_Data(n=5000):
    data = [ ]
    for _ in  range(n):
        register = {
            "edad": random.randint(18,65),
            "salario": round(random.uniform(8000, 50000), 2),
            "experencia": random.randint(0, 40),
            "calificacion": round(random.uniform(1,5),1),
            "departamento": random.choice(["IT", "RH", "VH", "Finanzas"]),
            "educacion": random.choice(["Licenciatura", "Maestria", "Doctorado"]),
            "direccion": {
                "calle": fake.street_name(),
                "ciudad": fake.city(),
                "pais": fake.country()
            },
            "habilidades": random.sample(
                ["Python", "SQL", "Excel", "Java", "Comunicacion", "Liderazgo"],
                k=3
            ),
            "comentarios": fake.text(max_nb_chars=100),
            "descripcion": fake.sentence()
        }
        data.append(register)
    return data

datos = generate_Data(5000)

client = MongoClient("mongodb://localhost:27017/")
db = client["empresaDB"]
coleccion = db["empleados"]
coleccion.insert_many(datos)

total = coleccion.count_documents({})
print("Total de registros:", total)
print("Datos cargados en mongoDB")

print("Vista prueba de algunos documentos")
for doc in coleccion.find().limit(10):
    print(doc)
```

1. **Análisis exploratorio de datos:**
   - Utiliza Pandas y NumPy para realizar análisis numérico y manipulación de datos.
   - Explora la distribución de datos numéricos y categóricos mediante el uso de estadísticas descriptivas como media, mediana, moda, solamente.
   - Crea un resumen estadístico utilizando un DataFrame de Python y sus librerías requeridas, como lo son NumPy y Pandas.
   - Realiza la interpretación del análisis exploratorio.

```python
from pymongo import MongoClient
from faker import Faker
import random
import pandas as pd
import numpy as np

fake = Faker('es_MX')

def generate_Data(n=5000):
    data = [ ]
    for _ in  range(n):
        register = {
            "edad": random.randint(18,65),
            "salario": round(random.uniform(8000, 50000), 2),
            "experiencia": random.randint(0, 40),
            "calificacion": round(random.uniform(1,5),1),
            "departamento": random.choice(["IT", "RH", "VH", "Finanzas"]),
            "educacion": random.choice(["Licenciatura", "Maestria", "Doctorado"]),
            "direccion": {
                "calle": fake.street_name(),
                "ciudad": fake.city(),
                "pais": fake.country()
            },
            "habilidades": random.sample(
                ["Python", "SQL", "Excel", "Java", "Comunicacion", "Liderazgo"],
                k=3
            ),
            "comentarios": fake.text(max_nb_chars=100),
            "descripcion": fake.sentence()
        }
        data.append(register)
    return data

client = MongoClient("mongodb://localhost:27017/")
db = client["empresaDB"]
coleccion = db["empleados"]

coleccion.delete_many({})
datos = generate_Data(5000)
coleccion.insert_many(datos)

total = coleccion.count_documents({})
print("Total de registros:", total)
print("Datos cargados en mongoDB")

print("Vista prueba de algunos documentos")
for doc in coleccion.find().limit(10):
    print(doc)

df = pd.DataFrame(datos)
print("Datos cargados en DataFrame")
print(df.head())

print("Estadísticas numéricas:")

print("\nMedia:")
print(df[["edad", "salario", "experiencia", "calificacion"]].mean())

print("\nMediana:")
print(df[["edad", "salario", "experiencia", "calificacion"]].median())

print("\nModa:")
print(df[["edad", "salario", "experiencia", "calificacion"]].mode().iloc[0])

print("Resumen general:")
print(df.describe())
```

![Resultado del programa](img/ResAnalisis.png)

**Interpretación**: En las variables numericas: edad, salario, experencia y calificacion en sus medias y medianas se puede ver que son balanceados y tambien se puede ver variabilidad en los salarios lo que muestra diversidad economica y como hay datos faltantes se puede ver una buena calidad de los datos

1. **Creación de gráficas para visualización de datos:**
   - Genera una visualización a través de un diagrama de cajas utilizando Python y las bibliotecas adecuadas.  
   ![Grafica de cajas de las variables numericas](/img/GrafCajas.png)
   - Crea una gráfica de dispersión para representar la relación entre variables.  
   ![Grafica de dispersion de los salarios respecto a la edad](/img/GrafDisper.png)
   - Crea un histograma para mostrar la distribución de datos.  
   ![Histograma de los salarios](/img/GrafHisto.png)
   - Realiza la interpretación de las gráficas creadas.

```python
from pymongo import MongoClient
from faker import Faker
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fake = Faker('es_MX')

def generate_Data(n=5000):
    data = [ ]
    for _ in  range(n):
        register = {
            "edad": random.randint(18,65),
            "salario": round(random.uniform(8000, 50000), 2),
            "experiencia": random.randint(0, 40),
            "calificacion": round(random.uniform(1,5),1),
            "departamento": random.choice(["IT", "RH", "VH", "Finanzas"]),
            "educacion": random.choice(["Licenciatura", "Maestria", "Doctorado"]),
            "direccion": {
                "calle": fake.street_name(),
                "ciudad": fake.city(),
                "pais": fake.country()
            },
            "habilidades": random.sample(
                ["Python", "SQL", "Excel", "Java", "Comunicacion", "Liderazgo"],
                k=3
            ),
            "comentarios": fake.text(max_nb_chars=100),
            "descripcion": fake.sentence()
        }
        data.append(register)
    return data

client = MongoClient("mongodb://localhost:27017/")
db = client["empresaDB"]
coleccion = db["empleados"]

coleccion.delete_many({})
datos = generate_Data(5000)
coleccion.insert_many(datos)

total = coleccion.count_documents({})
print("Total de registros:", total)
print("Datos cargados en mongoDB")

print("Vista prueba de algunos documentos")
for doc in coleccion.find().limit(10):
    print(doc)

df = pd.DataFrame(datos)
print("Datos cargados en DataFrame")
print(df.head())

print("Estadísticas numéricas:")

print("\nMedia:")
print(df[["edad", "salario", "experiencia", "calificacion"]].mean())

print("\nMediana:")
print(df[["edad", "salario", "experiencia", "calificacion"]].median())

print("\nModa:")
print(df[["edad", "salario", "experiencia", "calificacion"]].mode().iloc[0])

print("Resumen general:")
print(df.describe())

plt.figure()
df["salario"].plot(kind='box')
plt.title("Diagrama de cajas - Salario")
plt.show()

plt.figure()
plt.scatter(df["edad"], df["salario"])
plt.xlabel("Edad")
plt.ylabel("Salario")
plt.title("Relación entre Edad y Salario")
plt.show()

plt.figure()
plt.hist(df["salario"], bins=30)
plt.xlabel("Salario")
plt.ylabel("Frecuencia")
plt.title("Distribución del salario")
plt.show()
```

**Interpretación**: En la grafica de dispersion se puede ver claramente que no hay ningunda relacion entre la edad y el salario pues no se concentran en una linea sino que los datos estan dispersos por toda la grafica, el histograma muestra como no hay ninguna barra alta y estan moderadamente equilibradas significa que hay distribucion uniforme y el diagrama de cajas del salario muestra que los valores están distribuidos en un rango aproximado de 8,000 a 50,000. La mediana se encuentra cerca de los 29,000, lo que indica que la distribución es equilibrada. El 50% de los datos se concentra entre 18,000 y 39,000, lo que refleja una variabilidad moderada en los salarios.

---

# Ejercicios complementarios

---

## Ejercicios de Bases de Datos SQL

---

### Ejercicio 1: Consultas Básicas

Dada la siguiente tabla `empleados`:

| id | nombre     | departamento | salario |
| -- | ---------- | ------------ | ------- |
| 1  | Juan       | IT           | 50000   |
| 2  | María      | HR           | 45000   |
| 3  | Carlos     | IT           | 55000   |
| 4  | Ana        | Finanzas     | 48000   |
| 5  | Pedro      | Marketing    | 42000   |

```sql
CREATE TABLE excercise1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    department VARCHAR(30) NOT NULL,
    salary INT
);

INSERT INTO excercise1 (name, department, salary)
VALUES 
    ('Juan', 'IT', 50000),
    ('Maria', 'HR', 45000),
    ('Carlos', 'IT', 55000),
    ('Ana', 'Finanzas', 48000),
    ('Pedro', 'Marketing', 42000);
```

Escribir consultas SQL para:

1 Seleccionar todos los empleados  

```sql
SELECT * FROM excercise1;
```

2 Seleccionar nombres y salarios de empleados de IT  

```sql
SELECT name, salary FROM excercise1 WHERE department='IT';
```

3 Encontrar el empleado con mayor salario  

```sql
SELECT MAX(salary) FROM excercise1;
```

4 Contar empleados por departamento  

```sql
SELECT  department, COUNT(*) AS count_of_values FROM excercise1 GROUP BY department;
```

5 Actualizar el salario de María a 50000  

```sql
UPDATE excercise1 SET salary = 50000 WHERE name=Maria;
```

---

### Ejercicio 2: Joins

Dadas las tablas:

**empleados**  

| id | nombre   | id_departamento |
| -- | -------- | ----------------|
| 1  | Juan     | 1               |
| 2  | María    | 2               |
| 3  | Carlos   | 1               |

**departamentos**  

| id | nombre      |
| -- | ----------- |
| 1  | IT          |
| 2  | HR          |
| 3  | Finanzas    |

```sql
CREATE TABLE department (
    idDepartment INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

INSERT INTO department (name)
VALUES 
    ('IT'),
    ('HR'),
    ('Finanzas');

CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    idDepartment int NOT NULL,
    CONSTRAINT fk_department
     FOREIGN KEY (idDepartment)
     REFERENCES department(idDepartment)
);

INSERT INTO employe (name, idDepartment)
VALUES 
    ('Juan', 1),
    ('Maria', 2),
    ('Carlos', 1);
```

Escribir consultas para:

1 INNER JOIN entre empleados y departamentos

```sql
SELECT employe.name AS Employes, department.name AS Departments FROM employe INNER JOIN department ON employe.idDepartment = department.idDepartment;
```

2 LEFT JOIN mostrando todos los empleados

```sql
SELECT e.name AS Employes, d.name AS Departments FROM employe e LEFT JOIN department d ON e.idDepartment = d.idDepartment;
```

3 Contar empleados por departamento

```sql
SELECT d.name AS Department, COUNT(e.id) AS Total_Employes FROM department d LEFT JOIN employe e ON d.idDepartment = e.idDepartment GROUP BY d.idDepartment, d.name;
```

---

## Ejercicios de JSON y Estructuras de Datos

---

### Ejercicio 3: Manipulación de JSON

Dado el siguiente JSON:

```json
{
  "empleados": [
    {"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
    {"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
    {"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
  ]
}
```

1 Extraer los nombres de todos los empleados

```js
const nombres = data.empleados.map(emp => emp.nombre);
```

2 Agregar una nueva habilidad a Juan

```js
data.empleados[0].habilidades.push("JavaScript");
```

3 Crear un nuevo empleado con id: 4

```js
data.empleados.push({
    "id": 4, 
    "nombre": "Ana", 
    "habilidades": ["C#", "SQL"]
});
```

3 Eliminar las habilidades de María

```js
data.empleados[1].habilidades = [];
```

---

### Ejercicio 4: Estructuras de Datos en Python

Implementar las siguientes estructuras:

```python
empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "María", "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]
```

Ejercicios:

1 Agregar un nuevo empleado

```python
empleados.append({"id": 4, "nombre": "Daisy", "salario": 60000})
```

2 Buscar empleado por id

```python
for emp in empleados:
    if emp["id"] == 2:
        print("Elemento encontrado:", emp)
        break 
```

3 Calcular promedio de salarios

```python
total = 0
for emp in empleados:
    total = total + emp["salario"]
promedio = total/len(empleados)
print(f"Promedio de salarios: {promedio}")
```

4 Filtrar empleados con salario > 50000

```python
for emp in empleados:
    if emp["salario"] > 50000:
        print(emp)
```

5 Actualizar el nombre del empleado con id=2

```python
for emp in empleados:
    if emp["id"] == 2:
        emp["nombre"] = "Jocelyn"
        print(emp)
        break
```

---

## Ejercicios de MongoDB

---

### Ejercicio 5: Operaciones CRUD

Utilizando la colección `productos`:

```javascript
db.productos.insertMany([
    {"nombre": "Laptop", "precio": 999, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 29, "categoria": "Electrónica"},
    {"nombre": "Escritorio", "precio": 299, "categoria": "Muebles"}
])
```

Realizar las siguientes operaciones:

1 Read: Encontrar todos los productos de Electrónica

```javascript
db.productos.find({"categoria": "Electrónica"});
```

2 Read: Encontrar productos con precio < 100

```javascript
db.productos.find({ "precio": { "$lt": 100 } });
```

3 Update: Aumentar precio de Laptop en 10%

```javascript
db.productos.updateOne(
    { "nombre": "Laptop" }, 
    { "$mul": { "precio": 1.10 } }
);
```

4 Delete: Eliminar productos con precio < 50

```javascript
db.productos.deleteMany({ "precio": { "$lt": 50 } });
```

5 Create: Agregar un nuevo producto

```javascript
db.productos.insertOne({
    "nombre": "Teclado Mecánico",
    "precio": 85,
    "categoria": "Electrónica"
});
```

---

### Ejercicio 6: Consultas Avanzadas en MongoDB

```javascript
// Colección: estudiantes
{"nombre": "Ana", "materias": ["Math", "Physics"], "edad": 20}
{"nombre": "Luis", "materias": ["Math", "Chemistry"], "edad": 22}
{"nombre": "Sofia", "materias": ["Biology"], "edad": 19}
```

Consultas:
1 Encontrar estudiantes que cursan Math

```javascript
db.estudiantes.find({"materias":"Math"});
```

2 Encontrar estudiantes mayores de 20

```javascript
db.estudiantes.find({"edad": {"$gt":20}});
```

3 Contar estudiantes por edad

```javascript
db.estudiantes.aggregate([
    { "$group": { "_id": "$edad", "total": { "$sum": 1 } } }
])
```

4 Proyectar solo nombres

```javascript
db.estudiantes.find({}, { "nombre": 1, "_id": 0 });
```

---

## Ejercicios de Investigación

---

### Ejercicio 7: Tipos de Bases de Datos NoSQL

Investigar y explicar:

1. **Documentales**: MongoDB, CouchDB

- **MongoDB**:MongoDB es una base de datos NoSQL de documentos, de código abierto y alto rendimiento, diseñada para almacenar grandes volúmenes de datos con una estructura flexible, similar a JSON
- **CouchDB**:Es una base de datos NoSQL de código abierto orientada a documentos, diseñada para la web, que almacena datos en formato JSON sin esquemas rígidos

1. **Key-Value**: Redis, DynamoDB

- **Redis**:Es una base de datos NoSQL de código abierto, extremadamente rápida, que almacena datos en la memoria RAM en lugar de en el disco, permitiendo una latencia de microsegundos
- **DynamoDB**:Es un servicio de base de datos NoSQL de clave-valor y documentos, totalmente gestionado por AWS, diseñado para ofrecer un rendimiento rápido (milisegundos) y escalable a cualquier escala.

1. **Columnar**: Cassandra, HBase

- **Cassandra**:Es una base de datos NoSQL distribuida, de código abierto y "columna ancha" (wide-column), diseñada para manejar grandes volúmenes de datos en múltiples servidores con alta disponibilidad, rendimiento escalable y sin puntos únicos de fallo.
- **HBase**:Es una base de datos NoSQL distribuida, de código abierto y orientada a columnas, diseñada para gestionar grandes volúmenes de datos (Big Data) en tiempo real.

1. **Graph**: Neo4j

- **Neo4j**:Es la base de datos orientada a grafos (BDOG) nativa más popular, diseñada para gestionar datos altamente interconectados utilizando nodos y relaciones en lugar de tablas tradicionales.

**Investigar:**

- ¿Cuándo usar cada tipo?
  **Documentales**: Cuando no se necesite un esquema fijo y se ocupe un poco de flexibiilidad para realizar consultas complejas
  **Key-Value**: Para almacenar cache, sesiones de usuarios o aplicaciones en tiempo real que requieran una baja latencia
  **Columnar**: Para almacenar grandes volumenes de datos y que requieran alto rendimiento de escritura y lectura
  **Graph**: Cuando se gestione datos con relaciones complejas e interconectadas

- ¿Cuáles son sus ventajas y desventajas?

  | tipo        | ventajas                                        | desventajas                                               |
  |-------------|-------------------------------------------------|-----------------------------------------------------------|
  |Documentales |Flexible y intuitivo                             |Consistencia y duplicidad                                  |
  |Key-Value    |Velocidad extrema y escalabilidad                |Consultas limitadas y simplicidad                          |
  |Columnar     |Lectura masiva y compresion                      |Escriitura lenta y esquema rigido                          |
  |Graph        |Relaciones complejas y rendimiento en conexiones |Especializacion y no es apta para todo por su complejidad  |

---

### Ejercicio 8: Arquitecturas de Almacenamiento

Investigar:

1. ¿Qué es Data Lake?: Es un repositorio centralizado que permite almacenar todos tus datos, estructurados y no estructurados, a cualquier escala.
2. ¿Qué es Data Warehouse?: Es un sistema diseñado para el análisis y reporte de datos. A diferencia del Lake, aquí los datos ya están limpios, organizados y estructurados.
3. Diferencias entre OLAP y OLTP:

|Caracteristica |OLTP                                          |OLAP                                              |
|---------------|----------------------------------------------|--------------------------------------------------|
|Proposito      |Operaciones diarias                           |Análisis de tendencias y toma de decisiones.      |
|Ejemplo        |Un cajero automático o un registro de ventas. |El reporte anual de ventas de los últimos 5 años. |
|Velocidad      |Respuesta inmediata                           |Consultas lentas                                  |
|Datos          |Datos actuales y detallados.                  |Datos históricos y resumidos.                     |

1. ¿Qué es ETL?: Es el proceso de movimiento de datos entre sistemas. Es el "puente" que lleva los datos desde tus aplicaciones hacia tu Data Warehouse.

---

# Actividades practicas

---

### Actividad 2.1: Investigación de Arquitecturas de Datos

**Descripción:** Investiga las diferentes arquitecturas de almacenamiento de datos.

**Instrucciones:**

1.Investiga qué son los Data Warehouse y Data Lakes

- **Data Warehouse**:Es un sistema diseñado para el análisis y el reporte de datos estructurados. Los datos que entran aquí ya han sido procesados, limpiados y organizados en tablas  
- **Data Lakes**:Es un repositorio centralizado que permite almacenar todos los datos en su formato nativo (bruto), ya sean estructurados (tablas), semiestructurados (JSON, XML) o no estructurados (imágenes, audios, PDFs).

2.Compara las características de cada uno

|Caracteristica |Data Warehouse                     |Data Lake                            |
|---------------|-----------------------------------|-------------------------------------|
|Tipo de dato   |Solo estructurado                  |Estructurado, semi y no estructurado |
|Esquema        |Schema-on-write                    |Schema-on-read                       |
|Usuarios       |Analistas de negocio y directivos  |Científicos de datos e ingenieros    |
|Costo          |Alto                               |Bajo                                 |
|Agilidad       |Menor                              |Alta                                 |

3.Investiga qué es un Data Mart

- **Data Mart**:Es una versión enfocada y específica de un Data Warehouse. En lugar de contener los datos de toda la empresa, se especializa en un área o departamento particular

4.Crea un diagrama mostrando las diferencias
![Diagrama de diferencias](/img/DiagramaDiff.png)

---

### Actividad 2.2: Introducción a MongoDB

**Descripción:** Instala y configura MongoDB en tu entorno local.

**Instrucciones:**

1. Instala MongoDB Community Server
2. Instala MongoDB Compass (interfaz gráfica)
![Instalacion de MongoDB community y compass](/img/InstMongo.png)
3. Crea una base de datos de prueba
4. Crea una colección y agrega 5 documentos de ejemplo
![Creacion de la base de datos y 5 documentos de ejemplo](/img/CreacBD.png)

---

### Actividad 2.3: Operaciones CRUD en MongoDB

**Descripción:** Practica las operaciones básicas de MongoDB.

**Instrucciones:**

1. Conecta Python a MongoDB usando pymongo
2. Crea una colección llamada "empleados" con campos: nombre, departamento, salario
3. Inserta al menos 10 documentos
4. Realiza las siguientes operaciones:
   - READ: Consulta empleados de un departamento específico
   - UPDATE: Actualiza el salario de un empleado
   - DELETE: Elimina un empleado

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["empresaDB"]

coleccion = db["empleados"]

empleados = [
    {"nombre": "Juan Pérez", "departamento": "IT", "salario": 12000},
    {"nombre": "María López", "departamento": "RH", "salario": 10000},
    {"nombre": "Carlos Ruiz", "departamento": "IT", "salario": 13000},
    {"nombre": "Ana Torres", "departamento": "Ventas", "salario": 9000},
    {"nombre": "Luis Gómez", "departamento": "IT", "salario": 15000},
    {"nombre": "Sofía Hernández", "departamento": "RH", "salario": 11000},
    {"nombre": "Pedro Martínez", "departamento": "Ventas", "salario": 9500},
    {"nombre": "Laura Díaz", "departamento": "IT", "salario": 14000},
    {"nombre": "Jorge Castillo", "departamento": "RH", "salario": 10500},
    {"nombre": "Elena Vargas", "departamento": "Ventas", "salario": 9800}
]

coleccion.insert_many(empleados)
print("Documentos insertados")

print("\nLista Inicial de empleados:")
for emp in coleccion.find():
    print(emp)

print("\nEmpleados del departamento IT:")
for emp in coleccion.find({"departamento": "IT"}):
    print(emp)

coleccion.update_one(
    {"nombre": "Juan Pérez"},
    {"$set": {"salario": 16000}}
)
print("\nSalario actualizado para Juan Pérez")

coleccion.delete_one({"nombre": "Ana Torres"})
print("\nEmpleado eliminado: Ana Torres")

print("\nLista final de empleados:")
for emp in coleccion.find():
    print(emp)
```

1. Muestra los resultados de cada operación

![Resultado del programa](/img/ResultPr.png)

---

### Actividad 2.4: Modelado de Datos NoSQL

**Descripción:** Diseña un modelo de datos para un caso específico.

**Instrucciones:**

1. Elige un caso: "Sistema de biblioteca digital"
2. Diseña la estructura de documentos necesaria

El caso sera la biblioteca digital y su estructura seran los libros, usuarios, prestamos, autores y categorias para tener control de una hipotetica biblioteca

1. Crea al menos 5 colecciones con relaciones
2. Define los campos y tipos de datos

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["bibliotecaDB"]

usuarios = db["usuarios"]
libros = db["libros"]
autores = db["autores"]
categorias = db["categorias"]
prestamos = db["prestamos"]

autor_id = autores.insert_one({
    "nombre": "J. K. Rowling",
    "nacionalidad": "Britanica"
}).inserted_id

categoria_id = categorias.insert_one({
    "nombre": "Fantasia",
    "descripcion": "Elementos mágicos, sobrenaturales o inexplicables que rompen con las leyes de la realidad establecida"
}).inserted_id

libro_id = libros.insert_one({
    "titulo": "Harry Potter",
    "anio_publicacion": 1997,
    "autor_id": autor_id,
    "categoria_id": categoria_id,
    "disponible": True
}).inserted_id

usuario_id = usuarios.insert_one({
    "nombre": "Juan Pérez",
    "correo": "juan@email.com",
    "fecha_registro": "2026-01-01",
    "activo": True
}).inserted_id

prestamos.insert_one({
    "usuario_id": usuario_id,
    "libro_id": libro_id,
    "fecha_prestamo": "2026-03-31",
    "fecha_devolucion": None,
    "estado": "activo"
})
print("Datos insertados correctamente")
```

1. Justifica tu diseño

El diseño es asi porque un usuario puede tener multiples libros, el libro le pertence al autor y es parte de una categoria mientras que el prestamo se encarga de relacionar el libro y el usuario


[def]: Semana2/img