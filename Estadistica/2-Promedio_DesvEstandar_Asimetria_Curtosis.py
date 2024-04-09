# ************************************************************
# INTRODUCCIÓN A LA ESTADÍSTICA USANDO PYTHON
# Autor: Andrés Rugeles
# LastUpdate: 8 abril 2024
# ************************************************************

# 1.0 Importanto las bibliotecas requeridas para el ejercicio
import pandas as pd


# 2.0 Obteniendo el dataset de ejemplo:
data_spotify = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')


# 3.0 Preparando la información

    # 3.1 Creando un nuevo DataSet con los generso de Pop, Rap y latin
data_pop_rap_latin = data_spotify[data_spotify['playlist_genre'].isin(['pop', 'rap', 'latin'])]
print(f'Visualizando el DataSet {data_pop_rap_latin}')
print('______________________________________________________________')

    # 3.2 Del DataSet nuevo, se seleccionaran dos columnas y se creará otro DataSet
data_pop_rap_latin_filtrado = data_pop_rap_latin[['playlist_genre', 'duration_ms']]
print(f'DataSet únicamente con columnas de género y duración \n {data_pop_rap_latin_filtrado}')
print('______________________________________________________________')

    # 3.3 Obteniendo el promedio, devio estándar
meanData = data_pop_rap_latin_filtrado.groupby('playlist_genre').mean()/1000
stdData = data_pop_rap_latin_filtrado.groupby('playlist_genre').std()/1000
print(f'Promedio (seg): {meanData} \n\n Desvio estándar (seg): {stdData}')
print('______________________________________________________________')

# Con estos resultados, se puede observar que:
# Los promedios son parecidos, sin embargo, cómo hay diferencias importantes en el "Desvio Estándar", significa que hay presencia de valores atípicos o también conocidos como -outliers-.


# 4.0 Asimetría y Curtósis

    # 4.1 Importanto la biblioteca requerida para evaluar estos dos estadísticos
from scipy.stats import kurtosis, skew
import matplotlib.pyplot as plt

    # 4.2 Skew es para saber que tan asimétrica es la distribución
skew_value = skew(data_spotify['energy'])
print(f'Valor asimétrico de Energy: {skew_value} → En el histograma se observará el impacto de este valor negativo')
print('______________________________________________________________')

    # 4.3 Graficando un histográma sobre la columna de "Energy"
data_spotify['energy'].hist()
plt.xlabel('Energy')
plt.ylabel('Frecuencia')
plt.title("Histograma de Energy con una asimetría de -0.6363007")
plt.show()

    # 4.4 Skew para la variable "Acousticness"
skew_acoustic = skew(data_spotify['acousticness'])
print(f'Valor asimétrico de Acousticness: {skew_acoustic} → En el histograma se observará el impacto de este valor negativo')
print('______________________________________________________________')

data_spotify['acousticness'].hist()
plt.xlabel('Acousticness')
plt.ylabel('Frecuencia')
plt.title("Histograma de Acousticness con una asimetría de -1.59471")
plt.show()

# 5.0 Evaluando la Curtosis entre dos variables numéricas
data_spotify[['valence', 'duration_ms']].hist()
plt.xlabel('Valence | Duration')
plt.ylabel('Frecuencia')
plt.title("Histograma de estas dos variables")
plt.show()

kurtosis_value = data_spotify[['valence', 'duration_ms']].kurtosis()
print(f'La curtosos es: \n{kurtosis_value}')