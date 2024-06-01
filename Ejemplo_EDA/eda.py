# ************************************************************
# APLICANDO EL PROCESO EDA
# Autor: Andrés Rugeles
# LastUpdate: 16 de mayo 2024
# ************************************************************

# Importanto bibliotecas requeridas
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import displot
import matplotlib.pyplot as plt
import matplotlib.style as style

# Cargando el DataSet
wine_quality = pd.read_csv("C:/Users/ingan/OneDrive/Documentos/WORKSPACE/GitHub_AndresRugelesV/Python-general/Ejemplo_EDA/winequality-red.csv", sep=",")
print("Primeras 5 filas")
print(wine_quality.head())
print("=====================")

print("Últimas 5 filas")
print(wine_quality.tail())
print("=====================")

print("Dimensiones del DataSet")
print(wine_quality.shape)
print("=====================")

print("Últimas 5 filas")
print(wine_quality.tail())
print("=====================")

print("Obteniendo el listado de columnas")
column_list = wine_quality.columns
print(column_list)
print("=====================")

print("Revisando el tipo de dato de cada columna")
print(wine_quality.dtypes)
print("=====================")

print("Obtener información resumen de los datos")
print(wine_quality.info())
print("=====================")

print("Obteniendo la totalida de datos por columna")
print(wine_quality.count())
print("=====================")

# Es recomendable verificar que la estrutura de dato sea un DataFrame
print("Obteniendo el tipo de dato del DataFrame")
print(type(wine_quality))
print("=====================")

print("Mejorando la visualiación de los resultados")
print(wine_quality.describe())
print("=====================")

print("Mejorando la visualiación de los resultados")
print(wine_quality.describe().round())
print("=====================")

'''
    INICIANDO EL ANÁLISIS GRÁFICO
'''

# Histograma
sns.displot(data=wine_quality, x="quality", kde=True)
plt.show()

sns.displot(data=wine_quality, x="volatile acidity", kde=True)
plt.show()

# kind: "kde": otro tipo de visualización.

# Agrupando varios gráficos
variables = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']

columns = 4
fig, axes = plt.subplots(len(variables) // columns, columns, figsize=(15,8))

for current_idx, variable in enumerate(variables):
    i = current_idx // columns
    j = current_idx % columns
    sns.histplot(wine_quality[variable], ax=axes[i][j])
    axes[i][j].set_title(variable)
    axes[i][j].set_xlabel("")

plt.tight_layout()
plt.show()

# Generando un Boxplot
variables = ['fixed acidity', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'sulphates', 'alcohol']

fig, axes = plt.subplots(1, len(variables), figsize=(15,6))
for ax, variable in zip(axes, variables):
    sns.boxplot(y=variable, data=wine_quality, ax=ax)

plt.tight_layout()
plt.show()


# Scatterplots
from seaborn import lmplot
lmplot(x='free sulfur dioxide', y='total sulfur dioxide', data=wine_quality, fit_reg=True)
plt.show()

# Obteniendo los valores de correlación
# El métod pearson es un estadístico muy usado para este tipo de cálculos
correlation = wine_quality.corr(method='pearson')
print(correlation.head())

# Generando un mapa de calor basado en los datos anteriores
plt.figure(figsize=(15,15)) # Definiendo tamaño del gráfico
sns.heatmap(correlation,
            cbar=True,
            square=True,
            annot=True,
            fmt='.2f',
            annot_kws={'size':15},
            cmap='coolwarm'
            )

# Rotando los ejes para que queden inclinados
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()