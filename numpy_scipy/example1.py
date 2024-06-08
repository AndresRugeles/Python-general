# Importando bibliotecas
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Numpy Array
# Siempre deben ser de un mismo tipo"
list1 = [10,20,30,40,50,60]
print(list1)
print(type(list1))

# Convertir lista en un array
arr1 = np.array(list1)
print(arr1)
print(type(arr1))
print(arr1.dtype)

# Conviritnedo de flotante a
print(arr1.astype(float))

# Trabajando con diversos tipos de datos
list2 = [10, 'Ejemplo de texto']
arr_example = np.array(list2)
print(arr_example)

# Generando otro array
print(np.arange(0,10))
print(np.arange(0,100,10))
print(np.arange(100,10,-10))

arr3 = np.arange(0,10)
print(arr3.size)
print(arr3.ndim)
print(len(arr3))

# Creando arreglos de ceros, unos, 
print(np.zeros(10))
print(np.ones(15))
print(np.repeat(10,5))

# Repite el ojbeto a tres veces
a = np.array([10,20,30])
print(np.repeat(a,3))

# Creando arreglos aleatorios
print(np.random.random(4))

# Array intergers -5 valores
print(np.random.randint(0,500,5))

# Array intergers -10 valores
print(np.random.randint(0,500,10))

# Uso de una semilla
np.random.seed(123)
print(np.random.randint(0,100,10))

# Cambiando la semilla
np.random.seed(101)
print(np.random.randint(0,100,10))

# Creando un array con una distribución uniforme
f1 = np.random.uniform(5,10, size=(10))
print(f1)

# Extrayendo su valor flotante
np.floor(f1)

# Convirtiendo el array en integer
print(f1.astype(int))

# Arrays con distribución normal (mean=0 & variance = 1)
b2 = np.random.randn(10)
print(b2)

# Viendo los índices y valores del array
for index, value in np.ndenumerate(arr1):
    print(index, value)