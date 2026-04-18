import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Normalizacion Min-Max

datosN = [10, 20, 30, 40, 50]

X_min = min(datosN)
X_max = max(datosN)

X_normalized = lambda X: (X - X_min) / (X_max - X_min)
resultado = [X_normalized(x) for x in datosN]

print(f"Datos para normalizacion {datosN}")
print(f"Resultado de la normalizacion: {resultado}")

# Estandarización (Z-Score)

datosE = [2, 4, 4, 4, 5, 5, 7, 9]

suma = 0
for i in datosE:
    suma = suma + i

μ = suma / len(datosE)
suma_cuadrados = sum([(x - μ) ** 2 for x in datosE])
calc_var = suma_cuadrados / (len(datosE) - 1)
σ = calc_var**0.5
Z = lambda X: (X - μ) / σ
resultado_estandarizacion = [Z(x) for x in datosE]

print(f"\nDatos para estandarizar: {datosE}")
print(f"Media: {μ}")
print(f"Desviacion estandar: {σ}")
print(f"Estandarización de cada dato: {resultado_estandarizacion}")

# Comparacion de tecnicas

datos = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)

# Aplicar:
# 1. MinMaxScaler de sklearn
# 2. StandardScaler de sklearn
# Comparar resultados

mmScaler = MinMaxScaler()
stScaler = StandardScaler()

scaled_minmax = mmScaler.fit_transform(datos)
scaled_standard = stScaler.fit_transform(datos)

print("\nDatos para comparacion de tecnicas: \n", datos)
print("Escala min-max: \n", scaled_minmax)
print("Escala estandar: \n", scaled_standard)
