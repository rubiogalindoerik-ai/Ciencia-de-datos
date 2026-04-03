// Coleccion estudiantes
{"nombre": "Ana", "materias": ["Math", "Physics"], "edad": 20}
{"nombre": "Luis", "materias": ["Math", "Chemistry"], "edad": 22}
{"nombre": "Sofia", "materias": ["Biology"], "edad": 19}

db.estudiantes.find({"materias":"Math"});

db.estudiantes.find({"edad": {"$gt":20}});

db.estudiantes.aggregate([
    { "$group": { "_id": "$edad", "total": { "$sum": 1 } } }
])

db.estudiantes.find({}, { "nombre": 1, "_id": 0 });
