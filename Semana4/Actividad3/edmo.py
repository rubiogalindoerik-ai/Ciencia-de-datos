import numpy as np

datos = [10, 12, 14, 15, 16, 18, 20, 22, 25, 100]

# Calcular:
# 1. Q1 (percentil 25)
# 2. Q3 (percentil 75)
# 3. IQR = Q3 - Q1
# 4. Límite inferior = Q1 - 1.5 * IQR
# 5. Límite superior = Q3 + 1.5 * IQR
# 6. Identificar outliers

q1 = np.percentile(datos, 25)
print("Q1: ", q1)

q3 = np.percentile(datos, 75)
print("Q3: ", q3)

iqr = q3 - q1
print(iqr)

linf = q1 - 1.5 * iqr
lins = q3 + 1.5 * iqr
print("Límite inferior: ", linf)
print("Limite superior: ", lins)

outliers = [x for x in datos if x < linf or x > lins]
print("Outliers: ", outliers)
