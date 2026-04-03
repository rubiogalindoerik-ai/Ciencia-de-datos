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


