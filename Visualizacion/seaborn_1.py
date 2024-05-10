# ************************************************************
# VISUALIZACIÓN DE DATOS CON SEABORN PARTE I
# Autor: Andrés Rugeles
# LastUpdate: 8 de mayo 2024
# ************************************************************

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   # pip install seaborn

'''
EJEMPLO 1
'''

sns.set_theme(style='white')

# Generando valores aleatorios
rs = np.random.RandomState(10)
d = rs.normal(size=100)     # Distribución normal

# Graficando un histograma
sns.histplot(d, kde=True, color='m')
plt.savefig('histograma.png')

# Borrando el contendor figure
plt.clf()


'''
EJEMPLO 2
'''
sns.set_theme(style='dark')
fmri = sns.load_dataset('fmri')
print(fmri.head())

# Graficando dataset
sns.lineplot(x='timepoint',
             y='signal',
             hue='region',
             style='event',
             data=fmri)
plt.savefig('lineplot.png')
plt.clf()


'''
EJEMPLO 3
'''
# Gráfico de dispersión haciendo uso de la regresión
sns.set_theme(style='ticks')
df = sns.load_dataset('anscombe')
print(df.head())

# Graficando
sns.lmplot(x='x', y='y', data=df)
plt.savefig('Dispersión.png')


'''
CUSTOMIZANDO LOS VISUALES
'''
# Paleta de colores ACTUAL
#from matplotlib import pyplot as plt
current_palette = sns.color_palette()
sns.palplot(current_palette)
plt.show()

# Paleta de colores GRISES
sns.palplot(sns.color_palette('Greys'))
plt.show()

# Paleta de colores DIVERGENTE
sns.palplot(sns.color_palette('terrain_r'))
plt.show()

# Paleta de colores BRILLANTES
sns.palplot(sns.color_palette('bright'))
plt.show()

# Paleta de colores OSCUROS
sns.palplot(sns.color_palette('dark', 5))   # 5 es el número de colores
plt.show()

# Personalizando la paleta
color = ["green", "white", "red", "yellow", "green", "grey"]
sns.set_palette(color)
sns.palplot(sns.color_palette())
plt.show()