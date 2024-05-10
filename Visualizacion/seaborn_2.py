# ************************************************************
# VISUALIZACIÓN DE DATOS CON SEABORN PARTE II
# Autor: Andrés Rugeles
# LastUpdate: 8 de mayo 2024
# ************************************************************

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   # pip install seaborn

'''
FACEGRID
Uso especial para visualizar datos que involucran múltiples variables categóricas.
Divide un Dataset en subconjuntos mas pequeños con respecto a una o varias variables categóricas
y crear visualizaciones separadas para cada subconjunto.
'''

# Ejemplo 1
df = sns.load_dataset('tips')
print(df.head())

# Graficar la relación que existe entre las variables de -total_bill- y "tip" segmentada por la variable "sex" y el "día"
graph = sns.FacetGrid(df, col="sex", hue="day")
graph.map(plt.scatter, "total_bill", "tip", edgecolor="w").add_legend()
plt.title("Gráfico ejemplo 1")
plt.show()


# Ejemplo 2
graph = sns.FacetGrid(df, row='smoker', col="time")
graph.map(plt.hist, 'total_bill', bins=15, color='orange')
plt.title("Gráfico ejemplo 2")
plt.show()


# Ejemplo 3
graph = sns.FacetGrid(df, col='time', hue='smoker')
graph.map(sns.regplot, 'total_bill', 'tip').add_legend()
plt.title("Gráfico ejemplo 3")
plt.show()


'''
PAIR GRID
Visualza relaciones entre pares de variables en un Dataset
'''

# Ejemplo 4
iris = sns.load_dataset("iris")
print(iris.head())

graph_2 = sns.PairGrid(iris)
graph_2.map_diag(sns.histplot)  # histograma en la diagonal principal
graph_2.map_offdiag(sns.scatterplot)    # gráficos de dispersión fuera de la diagonal
plt.title("Gráfijo ejemplo 4")
plt.show()