
# Programa que predice
# las calificaciones de
# los estudiantes dependiendo
# del su consumo de alcohol

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from Metodos_Modelo import *

# Metodos

metodos = metodosParaModelos()

# Lectura de datos

url = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Datasets/CSV/student-mat.csv'
df = pd.read_csv(url)
print(df)

# Division de datos

x = df['G3']
y = df['G2']

x = pd.DataFrame(x)
y = pd.DataFrame(y)

# Entrenamiento

x_train = x.iloc[:100]
y_train = y.iloc[:100]

# Prueba

x_test = x.iloc[100:]
y_test = y.iloc[100:]

# Modelo

modelo = LinearRegression()

# Entrenamiento

metodos.entrenamiento(modelo, x_train, y_train)

# Prediccion

y_hat = modelo.predict(x_test)

# Metricas

metodos.metricas_regresion(y_test, y_hat)

# Grafica 1

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(ncols = 5, nrows = 1, figsize = (20, 5))

df.plot.scatter(x = 'famrel', y = 'G3', ax = ax1)
df.plot.scatter(x = 'freetime', y = 'G3', ax = ax2)
df.plot.scatter(x = 'goout', y = 'G3', ax = ax3)
df.plot.scatter(x = 'Dalc', y = 'G3', ax = ax4)
df.plot.scatter(x = 'Walc', y = 'G3', ax = ax5)

plt.show()

# Grafica 2

fig, (ax6, ax7, ax8, ax9) = plt.subplots(ncols = 4, nrows = 1, figsize = (20, 5))

df.plot.scatter(x = 'health', y = 'G3', ax = ax6)
df.plot.scatter(x = 'absences', y = 'G3', ax = ax7)
df.plot.scatter(x = 'G1', y = 'G3', ax = ax8)
df.plot.scatter(x = 'G2', y = 'G3', ax = ax9)

plt.show()

# Grafica con prediccion

plt.scatter(x_train, y_train)
plt.plot(x_test, y_hat)

plt.show()