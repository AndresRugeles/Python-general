# ************************************************************
# VISUALIZACIÓN DE DATOS PARTE I
# Autor: Andrés Rugeles
# LastUpdate: 8 de mayo 2024
# ************************************************************

# Importando Bibliotecas
import matplotlib.pyplot as plt    # pip install matplotlib
import numpy as np

# Ejemplo 1
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x,y)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title('Gráfico ejemplo 1')
plt.show()

# Ejemplo 2
xpoints = np.array([0, 10])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)

# Customización avanzada
font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.title('Gráfico ejemplo 2', fontdict = font1)
plt.xlabel("Eje x", fontdict=font2)
plt.ylabel("Eje y", fontdict=font2)
plt.show()

# Ejemplo 3
# Graficando un punto específico
xpoints = np.array([1,8])
ypoints = np.array([3, 15])
plt.plot(xpoints, ypoints, 'o')
plt.title('Gráfico ejemplo 3')
plt.show()

# Ejemplo 4
# Múltiples líneas
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.title('Gráfico ejemplo 4')
plt.show()

# Ejemplo 5
'''
Los valores del eje x se generan automáticamente como (0,1,2,3),
ya que hay cuatro puntos en 'ypoints'
'''
ypoints = np.array([3, 6, 1, 12])
plt.plot(ypoints, marker= 'o', ms=30, mec='hotpink', mfc='#4caf50' )
    # ms: tamaño del marker
    # mec: borde
    # mfc: relleno
plt.title('Gráfico ejemplo 5')
plt.show()

# Ejemplo 4, unificando gráficos
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = np.array([1, 2, 6, 8])
y2 = np.array([3, 8, 1, 10])

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos del ejemplo 1
ax.plot(x1, y1, label='Ejemplo 1')

# Graficar los datos del ejemplo 2
ax.plot(x2, y2, label='Ejemplo 2')

# Etiquetas de los ejes y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráficas de Ejemplos 1 y 2')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()



'''
Ejemplos de Marker
    'o'
    '*'
'''