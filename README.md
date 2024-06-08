# Introducción a la estadística descriptiva

## Conceptos teóricos:
* Estadística descriptiva: describe las características mas importantes de un conjunto de datos -DataSet- tales como:
    * La media
    * La mediana
    * La moda
    * La desviación estándar
    * Rangos y percentiles
* Estadística inferencial: Se usa para generar conclusiones sobre una población de registros más grande de datos, basada en la muestra representativa de esa población. Es muy importante para la toma de decisiones. Aquí se aplican técnicas como:
    * Estimación de parámetros.
    * Pruebas de hipótesis.
* Asimetría: Es cuando la media, la moda y la mediana dan el mismo valor o muy similar.
* Curtosis: es para observar que tan puntiaguda es la curva de distribución de los datos. Para tener en cuenta:
    * Si la curtosis es negativa → hay menor concetración de datos en torno a la media y por lo tanto hay una mayor dispersión.
    * Si la curtosis es positiva → la variable analizada presenta menos dispersión.

## 📂 Estadística
En este Folder se exponenen ejemplos de uso a la Estadística usando Python. A continuación, hay algunos conceptos teoróricos importantes y la descripción de cada uno de los archivos que componen este Folder.
> Créditos:
>
> Ejercicios basados en el curso de introducción a la estadística con Python desarrollado por Layla Scheli en la escuela de "NamasData".

###  📄 1-introduccion.estadistica.py

#### Explicación de elementos fundamentales del código

* DataSet.info():
    * Visualiza una información básica de las columnas, como:
        * Nombre de la columna.
        * Cantidad de registros.
        * Cantidad de valores nulos.
        * Tipo de datos.

* DataSet.head():
    * De forma predeterminada, visualiza los 5 primeros registros del DataSet.
    * Sin embargo, se puede ingresar un valor numérico para mostrar, por ejemplo, los 10 primeros registros.

* DataSet.sample(n=16000, random_state=1)
    * n: es el número de registros que se desean para la muestra.
    * random_state: es un valor semilla para que el ejercicio sea replicable por otro usuario.


### 📄 2-Promedio_DesvEstandar_Asimetria_Curtosis.py
En el archivo anterior, puede consultar una descripción estadística general del DataSet usado en este ejercicio.

Explicación de los elementos fundamentales del código

* DataSet_New = DataSet[DataSet['column_x'].isin(['value_A', 'value_B', 'value_C'])]
    * Permite generar un  nuevo DataSet basada en otro y se filtran ciertos elementos de acuerdo con la columna especificada y los valores de esta.
* DataSet_New_filtrado = DataSet_New[['column_x', 'column_y']]
    * Permite seleccionar ciertas columnas de un DataSet y generar uno nuevo.

## BIBLITECA DE PANDAS (Panel Data)
Biblioteca usada ampliamente para el **Análisis de datos**. Proporciona estructuras flexibles y eficientes para trabajar con **datos estructurados**. Su nombre viene de referise a datos multidimensionales estructurados en forma de paneles. A continuación, algunas características:

1. **DataFrame**: tabla bidimensional con filas y columnas etiquetadas, que son similiares a hojas de cálculo o tablas de bases de datos. Permite hacer **operaciones** como: filtrado, selección, agrupación y manipulación de datos de forma fácil y eficiente.
1. **Series**: matriz unidimensional etiquetada. Usadas para representar una columna individual o una fila de un DataFrame.
1. **Funciones para limpieza y manipulación de datos**: incluye funciones para manejar valores nulos, eliminar duplicados, cambiar el tipo de datos.
1. **Operaciones de indexación y selección avanzadas**: incluye indexación booleana, por posición, por etiquetra y selección basada en condiciones.
1. **Integración con otras bibliotecas**: como Numpy, Matplotlib y Scikit-learn.

### Proceso para configurar "pandas"
* pip install pandas: Instalar pandas de ser necesario.
* import pandas as pd: Importar la biblioteca de pandas.
* print(pd.__version__): imprimir la versión de pandas que está instalada.

Consulta de Bibliografía: https://www.w3schools.com/python/pandas/default.asp


## EDA
Por sus siglas en inglés representa el "Exploratory Data Analysis" o "Análisis exploratorio de datos". Su función es la de examinar los datos previamente a la aplicación de técnicas estadísticas, obteniendo también una información de la relación existente entre las variables analizadas. En resumen, se puede:

* Organizar y preparar datos.
* Detrectar fallos en el diseño y recolección de datos.
* Detectar datos ausentes o atípicos.

### Utilidades de EDA
Facilita responder preguntas tales como:

* ¿Si existen sesgo en los datos recolectados?
* ¿Hay errores en la codificación de datos?
* ¿Cómo se sintetiza y presenta la información contenida en un conjunto de datos?
* ¿existen datos atípicos **(outliers)** y cómo tratarlos?
* ¿Hay datos ausentes **(missing)**, si tienen algún patrón y como tratarlos?

### Etapas del EDA

#### Etapa 1
1. Preparar los datos para poder aplicar técnicas estadísticas.
1. Graficar los datos por variable o multivariable y así analizar datos estadísticos para cuantificar datos.
1. Analizar correlación entre las variables y dependencias.

#### Etapa 2
1. Evaluar algunos supuestos sobre la distribución de las variables asimétricas, formas, etc.
1. Identificar los datos **outliers** y que impacto pueden tener en el análisis estadístico.
1. De igual forma, determinar el impacto de los **missing**.

### Operaciones principales
* Combinar conjunto de datos de dos o mas archivos distintos.
* Generar subconjunto de datos.
* Dividir el archivo de datos en varias partes.
* Transformar variables.
* Filtrar y ordenar el DataSet
* Agregar nuevos datos y variables a partir de los existentes.
* Eliminar datos y variables.
* Guardar datos y resultados de los análisis.

### Correlaciones y dependencias
Determinar que tan relacionadas están las variables que se están usando.

La correlación **toma valores entre -1 y 1**, donde:

* Entre más cerca a 1, es más fuerte la relación lineal directa entre las variables.
* Entre más cerca a -1, más fuerte es la relación pero en este caso inversa.
* Si el valor se acerca a 0, no hay relación lineal entre variables.

👉 La correlación no es, ni implica, causalidad.

### Distribuciones de las variables
Hace referencia a las **medidas de forma**, que estudian las características de la distribución de probabilidades observadas. Se descantan principalmente:

#### Simetría
Una variable es simétrica si los valores equidistantes de la media son iguales, y donde la media, la moda y la mediana dan como resultado valores muy similares.

En caso de que no se simétrica, se estaría hablando de Asimétrica izquierda o negativa y asimétrica derecha o positiva

#### Curtosis
Mide el grado de apuntamiento o achatamiento de la distribución de frecuencia. Es decir, ayuda a entener "cuán empinada está la curva". Existen diferentes tipos de curtosis como:

* Distribución platicúrtica (valor máximo bajo)
* Distribución Lepticúrtica (valor máximo alto)
* Distribución Mesocúrtica (valor máximo medio)


### BIBLIOTECAS NUMPY & SCIPY

#### Biblioteca Numpy

**Numpy** se usa para operaciones numéricas en arreglos multidimensionales o matrices. Sus características principales son:

* Operaciones matemáticas y estadísticas: incluye funciones trigonométricas, exponenciales, álgebra lineal, funciones estadísticas descriptivas.
* Indexación y segmentación avanzada: facilita la selección y manipulación de datos en matrices de gran tamaño.
* Broadcasting: son operaciones entre arreglos de diferentes formas y tamaños, simplificando escritura de código y mejora el rendimiento en comparación con operaciones tradicionales de Bucles.
* Integración con otras bibliotecas: SciPy, Pandas, Matplotlib.

#### Biblioteca Scipy

Se construye sobre Numpy y tiene una amplia ganma de algorítmos y herramientas para la computación científica y técnica. Algunas características son:

* Módulos especialezados: incluye módulos para computación científica, optimización, ´álgebra lineal, interpolación, procesamiento de señales, procesamiento de imágenes, estadística, integración numérica.
* Eficiencia y rendimiento
* Integración con otras bibliotecas
* Licencia de código abierto


## Regresión Lineal
Consiten en predecir el valor de una variable objetivo o dependiente que generalmente se denomina (y), dados los valores de un vector de variables independientes o regresoras descritas como (x), todo esto a partir de una función lineal que represente la relación entre las variables.

### Métricas de un modelo de regresión
1. **Error absoluto Medio (MAE - Mean Absolute Error)**: es la diferencia absoluta entre las predicciones y los valores reales.
1. **Error cuadrático medio (MSE - Mean squared Error)**: es la media de cuadrados de las diferencias entre las predicciones y los valores reales.
1. **Raiz del error cuadrático medio (RMSE - Root mean Squared error)**: proporciona una medida del error en la misma unidad que los datos originales.
1. **Error porcentual absoluto medio (MAPE - Mean absolute Percentage Error)**: es el promedio de los porcentajes absolutos de las diferencias entre las predicciones y los valores reales en relación con los valores reales. Es útil para evaluar la precisión en términos porcentuales.
1. **Coeficiente de determinación R2 (R-squared)**: representa la proporción de la variabnza en la variable dependiente que es predecible a partir de las variables independientes. Cuanto mas cercano a 1 sea R2, mejor se ajusta el modelo a los datos.  

https://economipedia.com/definiciones/modelo-de-regresion.html#:~:text=Un%20modelo%20de%20regresi%c3%B3n%20es,explicativas%20o%20independientes%20(X)

## Machine Learning ML
Disciplina derivada de la inteligencia artificial y se encarga de generar modelos capaced de aprender, es decir, analizar muchos datos y extraer lo patrones o insight de esos datos. Se trata de reducir la intervención humana ya que el modelo puede predicr o clasificar automáticamente.

## Tipos de aprendizaje en ML
1. Aprendizaje supervisado.
    
    1. Problemas de clasificación: relacionado a predecir la variable **target** o **respuesta** que debe ser de tipo categórica.
    1. Problemas de regresión: En lugar de predecir variables categóricas, se predicen variables numéricas, de tipo cuantitativo.
2. Aprendizaje no supervisado.
3. Aprendizaje por refuerzo.

