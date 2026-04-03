const data = {
  "empleados": [
    {"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
    {"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
    {"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
  ]
};

const nombres = data.empleados.map(emp => emp.nombre);
data.empleados[0].habilidades.push("JavaScript");
data.empleados.push({"id": 4, "nombre": "Ana", "habilidades": ["C#", "SQL"]});
data.empleados[1].habilidades = [];
