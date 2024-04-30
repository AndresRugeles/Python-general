# ************************************************************
# EXPLORACIÓN BÁSICA DE DATOS I
# Autor: Andrés Rugeles
# LastUpdate: 29 abril 2024
# ************************************************************

import pandas as pd

# Importanto el arvhivo de ejemplo
df = pd.read_csv("C:/Users/ingan/OneDrive/Documentos/WORKSPACE/GitHub_AndresRugelesV/Python-general/Pandas/AB_NYC_2019.csv", sep=",")

print(f'1. Visualizando los primeros 5 registros: \n {df.head()}')
print("-----------------------------------------------------------")

print(f'2. Visualizando los últimos 5 registros: \n {df.tail()}')
print("-----------------------------------------------------------")

print(f'3. Obteniendo la dimensionalidad: \n {df.shape}')
print("-----------------------------------------------------------")

print(f'4. Realizando un conteo de registros por columna: \n {df.count()}')
print("-----------------------------------------------------------")

print(f'5. Identificando el tipo de dato por columna: \n {df.dtypes}')
print("-----------------------------------------------------------")

print(f'6. Extrayendo el nombre de las columnas: \n {df.columns}')
print("-----------------------------------------------------------")

# Eliminando columnas
columns_to_drop = ['id', 'host_name', 'last_review']
df.drop(columns_to_drop, axis="columns", inplace=True)      # inplace=True es para que sobreescriba el objeto
print(f'7. Visualizando el dataframe ajustado: \n {df.shape}')
print("-----------------------------------------------------------")

# Reemplazando valores NaN
df.fillna({'reviews_per_month': 0}, inplace=True)
print(f'8. Comprobando el reemplazo de Nan por 0: \n {df.count()}')
print("-----------------------------------------------------------")

# Filtrando a nivel de columnas
df_1 = df[df['price'] < 100 ]
print(f'9. Imprimiendo los Alojamientos con precio menor a $100: \n {df_1}')
print("-----------------------------------------------------------")

print(f'10. Obteniendo el TOP X con respecto a una columna: \n {df.nlargest(10, "number_of_reviews")}')
print("-----------------------------------------------------------")

print(f'11. Obteniendo los 10 mejores barrios (neighbourhood) de acuerdo a la agrupación de valores: \n')
print(f'{df["neighbourhood"].value_counts().head(10)}')
print("-----------------------------------------------------------")

# Visualizando algunos datos
df["neighbourhood"].value_counts().head(10).plot(kind='bar')

import matplotlib.pyplot as plt
plt.show()