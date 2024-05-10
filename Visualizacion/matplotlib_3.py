# ************************************************************
# VISUALIZACIÓN DE DATOS PARTE III - GRID Y SUBPLOTS
# Autor: Andrés Rugeles
# LastUpdate: 8 de mayo 2024
# ************************************************************

import numpy as np
import matplotlib.pyplot as plt

# Ejemplo 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Gráfica ejemplo 1")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.plot(x, y)
plt.grid()
plt.show()


# Ejemplo 2
#Grilla solo para el eje x
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Gráfico Ejemplo 2")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.plot(x, y)
plt.grid(axis = 'x')    # axis = 'y'
plt.show()


# Ejemplo 3
# Personalizando la grilla
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Ejemplo 3")
plt.xlabel("eje X")
plt.ylabel("eje Y")
plt.plot(x, y)
plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)
plt.show()


# Ejemplo 4
# Usando Subplots

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)    # filas, columnas, índice
plt.plot(x,y)
plt.title("Ejemplo 3 - Subplot 1")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)

plt.title("Ejemplo 3 - Subplot 2")
plt.plot(x,y)
plt.show()