# Proyecto: Análisis Predictivo del Mercado Inmobiliario (Airbnb)

**Ciencia de Datos - Proyecto final**

---

## 1. Introducción y Objetivo

El objetivo de este proyecto es analizar los factores que determinan el precio de los alojamientos en Airbnb y construir un modelo capaz de predecir estos costos basándose en características físicas y reputación.

* **Fase 1:** Análisis Exploratorio de Datos (EDA).
* **Fase 2:** Modelado Predictivo (Regresión Lineal Múltiple).

---

## 2. El Dataset

Usando la base de datos de Kaggle: https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction:

* **Características:** Número de cuartos, camas, baños y capacidad.
* **Reputación:** Puntuaciones y cantidad de reseñas.
* **Objetivo:** Predecir el precio segun lo que tienen.

---

## 3. Análisis Exploratorio (EDA) - Estadísticos

| Variable | Media | Mediana | Desv. Estándar |
| :--- | :---: | :---: | :---: |
| log_price | 4.75 | 4.70 | 0.70 |
| accommodates | 3.15 | 2.00 | 2.15 |
| bedrooms | 1.18 | 1.00 | 0.63 |

---

## 4. Visualización: Distribución de Precios

El precio presenta una distribución que requiere transformación logarítmica para reducir el sesgo y mejorar el rendimiento del modelo.

![Historgrama de precios](/Ciencia%20de%20datos/Semana7/Proyecto/Final/Visualizaciones/hist_precio.png)

* La mayoría de las propiedades se concentran en un rango de precio medio, con pocos valores extremos tras la normalización.

---

## 5. Visualización: Correlaciones

¿Qué variables se mueven juntas? El mapa de calor y estas graficas de correlacion dan la respuesta:

![Mapa de calor](/Ciencia%20de%20datos/Semana7/Proyecto/Final/Visualizaciones/heatmap.png)

![Mapa de calor](/Ciencia%20de%20datos/Semana7/Proyecto/Final/Visualizaciones/pairplot_correlacion.png)

* **Correlación Fuerte:** Existe una relación clara entre el número de habitaciones/camas y el precio.
* **Correlación Débil:** La disponibilidad y los puntajes de reseñas tienen un impacto menor en el precio final de lo esperado.

---

## 6. Preparación de Datos y Limpieza

Para asegurar un modelo robusto, realizamos:

1. **Imputación:** Relleno de nulos con la mediana.
2. **Filtrado:** Eliminación de filas sin variable objetivo (`log_price`).
3. **Selección de variables:** Nos enfocamos en variables con mayor peso predictivo:
   * `accommodates`, `bedrooms`, `bathrooms`, `review_scores_rating`.

---

## 7. Modelado: Regresión Lineal Múltiple

El modelo esta formado por:

* **Dependiente ($y$):** `log_price`
* **Independientes ($X$):** Características de la vivienda.
* **División de datos:** 80% entrenamiento (45,911 filas) / 20% prueba (11,478 filas).

---

## 8. Resultados del Modelo

Los resultados muestran que el modelo es estadísticamente significativo, aunque hay margen de mejora.

| Métrica | Valor |
| :--- | :--- |
| **Coeficiente de Determinación ($R^2$)** | **0.3691** |
| **Error Cuadrático Medio (MSE)** | **0.2813** |
| **P-Value (todas las variables)** | **0.000** |

**Pesos del Modelo (Coeficientes):**
* `accommodates`: 0.1514
* `bedrooms`: 0.0894
* `bathrooms`: 0.0448
* `review_scores_rating`: 0.0083

---

## 9. Validación: Real vs. Predicción

Al comparar lo que el modelo predijo contra los valores reales en una grafica de dispersion:

![Comparación de Valores Reales vs Predicciones en grafica de dispersion](/Ciencia%20de%20datos/Semana7/Proyecto/Final/Visualizaciones/comparacion_final.png)

* **Aciertos:** Excelente precisión en precios de rango medio.
* **Desafíos:** Mayor dispersión en propiedades de lujo, donde factores subjetivos influyen más que el número de camas o baños.

---

## 10. Conclusiones

1. **El tamaño importa:** La cantidad de cuartos y la capacidad son los predictores más fuertes.
2. **Reputación secundaria:** Curiosamente, un buen puntaje no garantiza un precio más alto; es una condición necesaria pero no determinante del costo.
3. **Multicolinealidad:** Se observó relación entre camas y habitaciones, algo lógico en el mercado inmobiliario.

---