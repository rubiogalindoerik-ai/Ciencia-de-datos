import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from scipy import stats

df = pd.read_csv("Datos/phpMYEkMl.csv")

print("Información del dataset:")
print(df.head())

df = df.replace("?", np.nan)
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["fare"] = pd.to_numeric(df["fare"], errors="coerce")
columnas_descarte = ["name", "ticket", "cabin", "boat", "body", "home.dest"]
df = df.drop(columns=columnas_descarte)
df["age"] = df["age"].fillna(df["age"].median())
df["fare"] = df["fare"].fillna(df["fare"].median())
df = df.dropna()
df["sex"] = df["sex"].map({"male": 1, "female": 0})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlación entre variables y Supervivencia")
plt.show()

sobrevivientes = df[df["survived"] == 1]["fare"]
no_sobrevivientes = df[df["survived"] == 0]["fare"]
t_stat, p_valor = stats.ttest_ind(sobrevivientes, no_sobrevivientes)
print("Resultados de la Prueba t-test (Variable: Tarifa/Fare)")
print(f"Media de tarifa (Sobrevivientes): {sobrevivientes.mean():.2f}")
print(f"Media de tarifa (No Sobrevivientes): {no_sobrevivientes.mean():.2f}")
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p (p-value): {p_valor:.4e}")
alpha = 0.05
if p_valor < alpha:
    print("Existe una diferencia entre quienes sobrevivieron y quienes no.")
else:
    print("\nNo hay diferencia")

X = df.drop("survived", axis=1)
y = df["survived"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo_log = LogisticRegression(max_iter=1000)
modelo_log.fit(X_train, y_train)

y_pred = modelo_log.predict(X_test)
print(f"Precisión del modelo (Accuracy): {accuracy_score(y_test, y_pred):.4f}")
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
