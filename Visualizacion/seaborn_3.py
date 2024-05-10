# ************************************************************
# VISUALIZACIÓN DE DATOS CON SEABORN PARTE III
# Autor: Andrés Rugeles
# LastUpdate: 9 de mayo 2024
# ************************************************************

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   # pip install seaborn

# Ejemplo 1
ax = sns.lineplot(
    x = [1,2,3,4,5],
    y = [1,4,2,5,4]
)

# Anotación en un punto específico
ax.text(3, 2, "Texto personalizado")
plt.show()

# Ejemplo 2
ax = sns.lineplot(
    x = [1,2,3,4,5],
    y = [1,4,2,5,4]
)

# Anotración en un punto específico con texto personalizado
ax.text(3,1.5, "Texto personalizado 2",
        fontsize=12,
        fontstyle="oblique",
        color="red",
        ha="center",
        va="center",
        rotation=-50)
    # ha, va: alineación horizontal y vertical
plt.show()

# Etiquetar puntos específicos de datos
x = [1,2,3,4,5]
y = [1,4,2,5,4]
textos = ['A', 'B', 'C', 'D', "E"]

ax = sns.scatterplot(x = x, y = y)
for i, txt in enumerate(textos):
    ax.text(x[i], y[i], txt)
plt.show()

# Ejemplo con scatterplot
sns.set_theme(style='whitegrid')
fmri = sns.load_dataset("fmri")

sns.scatterplot(
    x='timepoint',
    y='signal',
    hue='region',
    style='event',
    data=fmri)
plt.show()


# Una derivación de scatter es el jointplot
# Sirve para ver distribuciones y correlaciones
df = sns.load_dataset('penguins')
sns.jointplot(data=df,
              x = 'bill_length_mm',
              y = "bill_depth_mm",
              marker = 'x',
              color = 'lavender',
              kind='reg')   # kind=reg de regresión
plt.show()


# Barplot
df = sns.load_dataset('titanic')
sns.barplot(x='class',
            y='fare',
            data=df,
            hue='sex',
            order = ['Third', "Second", "First"],
            color="salmon",  # Color se puede reemplazar por palette='pastel'
            saturation=0.1
            )
plt.show()

# Count plot
data = ["A", "B", "C", "B", "B", "C"]
sns.countplot(x = data)     # y= data: sería horizontal
plt.show()

# Otro ejemplo de count plot
data = ["A", "B", "C", "B", "B", "C"]
group = ["G1", "G1", "G2", "G2", "G1", "G1"]
sns.countplot(x=data, hue=group, edgecolor="red")
plt.show()