empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "María", "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]

empleados.append({"id": 4, "nombre": "Daisy", "salario": 60000})

for emp in empleados:
    if emp["id"] == 2:
        print("Elemento encontrado:", emp)
        break 

total = 0
for emp in empleados:
    total = total + emp["salario"]
promedio = total/len(empleados)
print(f"Promedio de salarios: {promedio}")

for emp in empleados:
    if emp["salario"] > 50000:
        print(emp)

for emp in empleados:
    if emp["id"] == 2:
        emp["nombre"] = "Jocelyn"
        print(emp)
        break

