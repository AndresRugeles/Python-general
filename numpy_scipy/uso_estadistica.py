# Importando bibliotecas
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generar datos aletaorios con distribución normal
data = np.random.normal(loc=0, scale=1, size=100)
print(f'Preview Data = {data} \n _____________________')

# Ditribución binomial
binomial_distribution = stats.binom(n=10, p=0.5)

# Calculando algunos datos estadísticos
mean = np.mean(data)
print(f'Media = {mean} \n _____________________')
median = np.median(data)
print(f'Mediana = {median} \n _____________________')
std_dev = np.std(data)
print(f'Desviación estándar = {std_dev} \n _____________________')
variance = np.var(data)
print(f'Varianza = {variance} \n _____________________')
max_value = np.max(data)
print(f'Valor máximo = {max_value} \n _____________________')
min_value = np.min(data)
print(f'Valor mínimo = {min_value} \n _____________________')

# Realizando una prueba t de una muestra
t_statistic, p_value = stats.ttest_1samp(data, popmean=0)
# Realizar una prueba de Chi-cuadrado
chi2_statistic, chi2_p_value = stats.chisquare(data)

# Crear una distribución uniforme entre 0 y 1
uniform_distribution = stats.uniform(loc=0, scale=1)
# Generar valores aleatorios
random_values = uniform_distribution.rvs(size=1000)

# Generar distribución EXPONENCIAL con tasa lambda igual a 0.5
exponential_distribution = stats.expon(scale=2)
# Generar valores aletorios
random_values = exponential_distribution.rvs(size=1000)

# Generar distribución de POISSON con tasa lambda igual a 3
poisson_distribution = stats.poisson(mu=3)
# Generar valores aleatorios
random_values = poisson_distribution.rvs(size=1000)

'''
Correlación de Pearson
'''
x = np.random.normal(loc=0, scale=1, size=100)
y = 2*x + np.random.normal(loc=0, scale=0.5, size=100)

#Calculando la correlación
correlation_coefficient, p_value = stats.pearsonr(x,y)
print(f'Coeficiente de correlación de Pearson = {correlation_coefficient} \n______________')
    # entre mas cercano a 1, es correlación positiva
print(f'Valor p = {p_value} \n______________')

'''
Prueba de Shapiro-Wilk para comprobar
normalidad de los datos
'''
sample = np.random.normal(loc=0, scale=1, size=100)
w_statistic, p_value = stats.shapiro(sample)
print(f'Estadística de Shapiro = {w_statistic} \n______________')
print(f'Valor p = {p_value} \n______________')

# Calcular el intervalo de confianza del 95% para la media
sample = np.random.normal(loc=0, scale=1, size=100)
confidence_interval = stats.norm.interval(0.95, loc=np.mean(sample), scale=stats.sem(sample))
print(f'Intervalo de confianza para la media = {confidence_interval} \n______________')

'''
Regresión lineal simple
'''
x = np.array([1,2,3,4,5])
y = np.array([2,3,4,5,6])

# Realizar regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(f'Pendiente = {slope}')
print(f'Intercepto = {intercept}')
print(f'Coeficiente de correlación = {r_value}')
print(f'Valor p = {p_value}')
print(f'Error estándar = {std_err}')

'''
Integrando con visualización de datos
'''
plt.hist(data, bins=10, density=True, alpha=0.6, color='g')
plt.show()
