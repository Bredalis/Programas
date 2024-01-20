
# Programa que predice 
# las calificaciones de 
# los estudiantes dependiendo 
# del su consumo de alcohol

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Lectura de datos

url = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Datasets/CSV/student-mat.csv'
df = pd.read_csv(url)
print(df)

# Division de datos

x = df['G3']
y = df['Dalc']

x = pd.DataFrame(x)
y = pd.DataFrame(y)

print(x)
print(y)

print(type(x))
print(type(y))

# Entrenamiento

x_train = x.iloc[:100]
y_train = y.iloc[:100]

print(x_train)
print(y_train)

# Prueba

x_test = x.iloc[100:]
y_test = y.iloc[100:]

print(x_test)
print(y_test)

# Modelo

modelo = LinearRegression(fit_intercept = True)

# Entrenamiento

# for i in range(0, 1000):
# 	modelo.fit(x_train, y_train)

# # Prediccion

# y_hat = modelo.predict(x_test)

# # Metricas

# MSE = mean_squared_error(y_test, y_hat)
# R2 = r2_score(y_test, y_hat)

# print(MSE)
# print(R2)

# Grafica sin prediccion

print(df.columns)

plt.scatter(x, y)

plt.title('Rendimiento Escolar y Consumo de Alcohol')
plt.xlabel('Calificaciones')
plt.ylabel('Consumo de Alcohol')

plt.show()

# Grafica con prediccion

plt.scatter(x_train, y_train)
plt.plot(x_train, y_hat)

plt.show()