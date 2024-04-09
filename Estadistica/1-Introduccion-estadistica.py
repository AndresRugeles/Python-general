# ************************************************************
# INTRODUCCIÓN A LA ESTADÍSTICA USANDO PYTHON
# Autor: Andrés Rugeles
# LastUpdate: 8 abril 2024
# ************************************************************


# 1.0 Importanto las bibliotecas requeridas para el ejercicio
import pandas as pd


# 2.0 Obteniendo el dataset de ejemplo:
data_spotify = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')


    # 2.1 Visualizando algunos estadísticos básicos:
info_Data = data_spotify.info()
print(f'Descripción básica de las columnas del DataSet: {info_Data}')
print('______________________________________________________________')


    # 2.2 Registros mas populares (Top 5)
top5_Data = data_spotify.sort_values('track_popularity', ascending=False).head()
print(f'Top 5 de los temas mas populares: {top5_Data}')
print('______________________________________________________________')


    # 2.3 ¿cuanles son los géneros musicales mas populares?
mean_Genero = data_spotify.groupby('playlist_genre')['track_popularity'].mean().sort_values(ascending=False)
print(f'Promedio de géneros mas populares ordenados de mayor a menor {mean_Genero}')
print('______________________________________________________________')


# 3.0 Estadística Inferencial

    # 3.1 realizando un muestro de la población de registros
muestra_1 = data_spotify.sample(n=16000, random_state=1)
muestra_2 = data_spotify.sample(n=16000, random_state=2)
muestra_3 = data_spotify.sample(n=16000, random_state=3)

    # 3.2 Obteniendo el promedio de track_popularity en cada muestreo
mean_muestra_1 = muestra_1.track_popularity.mean()
mean_muestra_2 = muestra_2.track_popularity.mean()
mean_muestra_3 = muestra_3.track_popularity.mean()

print(f'Prom. muestra 1 = {mean_muestra_1} | Prom. muestra 2 = {mean_muestra_2} | Prom. muestra 3 = {mean_muestra_3}')