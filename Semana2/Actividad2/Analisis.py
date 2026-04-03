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
