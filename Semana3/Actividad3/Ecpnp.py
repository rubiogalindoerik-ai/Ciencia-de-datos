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
