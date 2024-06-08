# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Cargando los datos
dataset = pd.read_csv("C:/Users/ingan/OneDrive/Documentos/WORKSPACE/GitHub_AndresRugelesV/Python-general/scikitLearn/student_scores.csv", sep=",")

'''
Visualizando un ejemplo del dataset donde está, las horas de estudio y la califiación obtenida:
'''
print(f'{dataset.head()}')

# Dimensión del dataset
print(f'Cantidad de filas y columnas: {dataset.shape}')

# Realizando análisis exploratorio
dataset.plot(x='Hours', y='Scores', style="o")
plt.title("Horas vs Calificación")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación obtenida")
#plt.show()

# Segmentando los valores dependientes (y) e independientes (x)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Iniciando con el modelo de regresión:
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# Entrenando el modelo
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Obteniendo la INTERSECCIÓN y PENDIENTE
print(f'Intercepto = {regressor.intercept_}')
print(f'Pendiente = {regressor.coef_}')

# Calculando la predicción
y_pred = regressor.predict(X_test)
print(y_pred)

# Visualizando la predicción en un df de pandas
df = pd.DataFrame({'Actual':y_test, 'Prediccion':y_pred})
print(df)   # Vemos 5 filas que equivalen al 20% definido para pruebas

'''
EVALUACIÓN DEL MODELO
'''

# Prediccion en Train y test para posteriormente comparar
y_train_pred = regressor.predict(X_train)
y_test_pred = regressor.predict(X_test)

# Calculando el RMSE
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
print(f'RMSE de Train = {rmse_train}')
print(f'RMSE de Test = {rmse_test}')

# Evaluando el modelo automatizado
# Comparando múltiples modelos de forma simultánea
modelo = ['Regresion lineal']
for i, model in enumerate ([regressor]):
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    print(f'Modelo benchmark: {modelo[i]}')

    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    print(f'rmse para Train = {rmse_train}')
    print(f'rmse para Test = {rmse_test}')

# Calculando el R2
r2 = r2_score(y_test, y_pred)
print(f'R2 score para un modelo Worse es = {r2}')
