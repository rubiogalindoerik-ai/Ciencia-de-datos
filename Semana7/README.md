# Documentacion del proyecto final

---

## Descripcion

En la segunda fase del proyecto, aplicarás técnicas avanzadas de ciencia de datos
para desarrollar modelos predictivos basados en los datos explorados anteriormente.
Asimismo, utilizarás técnicas de visualización de datos avanzadas para comunicar de
forma eficiente los insights obtenidos.

---

### ¿Que es?

Programa que se encarga de limpiar la base de datos y en base a esos datos entrenar
un algoritmo que muestre que variables afectan al precio de los alojamientos

---

## Estructura del proyecto

Semana7/
├── Consolidado/
│ └── Semana7_Consolidado.md # Documento consolidado semanal
├── Proyecto/
  ├── Final/
  │ ├── Modelo.py # Código del modelo
  │ ├── Limpieza.py # Código de limpieza
  │ ├── Datos/ # Datasets utilizados
  │ └── Visualizaciones/ # Gráficas generadas
  ├── Presentacion/ # Presentación (en Markdown)
  └── README.md # Documentacion del proyecto

---

## Librerias necesarias

**Dependencias**: pandas, seaborn, matplotlib, scikit-learn

**Comando de instalacion**:

```bash
pip install pandas seaborn matplotlib scikit-learn
```

---

## Guia de uso

Instala la base de datos "train2.csv" y lo archivos .py "modelo" y "limpieza"
dentro de la misma carpeta creas otra llamada Datos y ahi guardas la base de datos
luego desde la terminal o tu compilador de preferencia corres primero el acrhivo
"Limpieza.py" y despues "Modelo.py"

**Comandos para terminal**

```bash
python Limpieza.py
python Modelo.py
```
