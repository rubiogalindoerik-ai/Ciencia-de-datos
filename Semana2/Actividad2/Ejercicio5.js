db.productos.insertMany([
    {"nombre": "Laptop", "precio": 999, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 29, "categoria": "Electrónica"},
    {"nombre": "Escritorio", "precio": 299, "categoria": "Muebles"}
])

db.productos.find({"categoria": "Electrónica"});

db.productos.find({ "precio": { "$lt": 100 } });

db.productos.updateOne(
    { "nombre": "Laptop" }, 
    { "$mul": { "precio": 1.10 } }
);

db.productos.deleteMany({ "precio": { "$lt": 50 } });

db.productos.insertOne({
    "nombre": "Teclado Mecánico",
    "precio": 85,
    "categoria": "Electrónica"
});
