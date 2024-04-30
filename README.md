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