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
