
# Rendimiento de los alumnos
# Evaluacion de las calificaciones
# con respecto a las horas de estudio

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Lectura de datos

url = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Datasets/CSV/Rendimiento_Escolar.csv'
df = pd.read_csv(url)

print(df)
print(df.shape)

# Division de datos

# Entrenamiento

x_train = df.loc[:99, ['horas_de_estudios']]
y_train = df.loc[:99, ['calificaciones']]

print(len(x_train))
print(len(y_train))

print(x_train)
print(y_train)

# Pruebas

x_test = df.loc[100:, ['horas_de_estudios']]
y_test = df.loc[100:, ['calificaciones']]

print(len(x_test))
print(len(y_test))

print(x_test)
print(y_test)

# Modelo

modelo = LinearRegression(fit_intercept = True)

for i in range(0, 1000):
  modelo.fit(x_train, y_train)

y_hat = modelo.predict(x_test)

# Metricas de evaluacion

MAE = mean_absolute_error(y_test, y_hat)
print(MAE)

r2 = r2_score(y_test, y_hat)
print(r2)

# Grafica sin prediccion

plt.rcParams['figure.figsize'] = (10, 5)

df.plot.scatter(x = 'horas_de_estudios', y = 'calificaciones')
plt.show()

# Grafica con prediccion

plt.scatter(x_train, y_train)
plt.plot(x_train, y_hat)
plt.show()