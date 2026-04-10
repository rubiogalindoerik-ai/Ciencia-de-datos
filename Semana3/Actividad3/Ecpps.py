import pandas as pd
import numpy as np

# Crear un DataFrame con datos de estudiantes
data = {
    "nombre": ["Ana", "Luis", "María", "Carlos", "Sofia"],
    "edad": [20, 22, 19, 21, 23],
    "carrera": ["Ing", "Ing", "Lic", "Ing", "Lic"],
    "promedio": [8.5, 9.0, 7.8, 8.2, 9.5],
}

df = pd.DataFrame(data)

# Ejercicios:
# 1. Seleccionar columna 'nombre'
# 2. Filtrar estudiantes con promedio > 8.5
# 3. Ordenar por edad
# 4. Agregar columna 'aprobado' (promedio >= 7)
# 5. Group by carrera y promediar

df["nombre"]
df[df["promedio"] > 8.5]
ordenado = df.sort_values(by="edad")
df["aprobado"] = df["promedio"] >= 7
promecarrera = df.groupby("carrera").numeric_only().mean()

# Dado el DataFrame anterior:
# 1. Manejar valores faltantes (agregar NaN y llenarlos)
# 2. Eliminar duplicados
# 3. Aplicar funciones con apply()
# 4. Usar loc e iloc para slicing
# 5. Concatenar dos DataFrames

df.loc[0, "promedio"] = np.nan
df["promedio"] = df["promedio"].fillna(df["promedio"].mean())
df = df.drop_duplicates()
df["estatus"] = df["promedio"].apply(lambda x: "Excelente" if x >= 9.0 else "Regular")
vista_loc = df.loc[0:2, ["nombre", "promedio"]]
vista_iloc = df.iloc[0, 0:2]
nuevos_estudiantes = pd.DataFrame(
    {
        "nombre": ["Pedro", "Lucía"],
        "edad": [24, 21],
        "carrera": ["Ing", "Lic"],
        "promedio": [8.0, 9.2],
    }
)
df_total = pd.concat([df, nuevos_estudiantes], ignore_index=True)
