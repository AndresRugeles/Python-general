# ************************************************************
# VISUALIZACIÓN DE DATOS PARTE II
# Autor: Andrés Rugeles
# LastUpdate: 8 de mayo 2024
# ************************************************************

# Importando Bibliotecas
import matplotlib.pyplot as plt    # pip install matplotlib
import numpy as np

# Ejemplo 1
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle='solid')    #defaul
plt.title('Gráfico ejemplo 1')
plt.show()

# Ejemplo 2
plt.plot(ypoints, linestyle='dashed')
plt.title('Gráfico ejemplo 2')
plt.show()

# Ejemplo 3
plt.plot(ypoints, linestyle='dotted')
plt.title('Gráfico ejemplo 3')
plt.show()

'''
Otros estilos disponibles
    * 'dashdot'
    * 'none'
'''

# DEFINIENDO COLORES

# Ejemplo 4
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color='r')
plt.title('Gráfico ejemplo 4')
plt.show()

# Ejemplo 5
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, c='#4caf50', linewidth='20.5')
plt.title('Gráfico ejemplo 5')
plt.show()



