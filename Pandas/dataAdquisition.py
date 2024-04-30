# ************************************************************
# EJERCICIOS DE APLICACIÓN DE PANDAS
# Autor: Andrés Rugeles
# LastUpdate: 29 abril 2024
# ************************************************************

import pandas as pd

# Importando el archivo csv
data = pd.read_csv("C:/Users/ingan/OneDrive/Documentos/WORKSPACE/GitHub_AndresRugelesV/Python-general/Pandas/data.csv", sep="|")
print(data)
print("###############################")

# Importando un archivo de Excel
data_excel = pd.read_excel("C:/Users/ingan/OneDrive/Documentos/WORKSPACE/GitHub_AndresRugelesV/Python-general/Pandas/data.xlsx")
print(data_excel)
print("###############################")

# Importando un archivo de texto
with open("C:/Users/ingan/OneDrive/Documentos/WORKSPACE/GitHub_AndresRugelesV/Python-general/Pandas/data.txt", "r") as archivo:
    for linea in archivo:
        print(linea)