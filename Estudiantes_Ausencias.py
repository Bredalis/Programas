
# Programa que predice las calificaciones 
# de los estudiantes dependiendo de 
# sus ausencias en la escuela

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Lectura de datos

url = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Datasets/CSV/student-mat.csv'
df = pd.read_csv(url)

print(df)

# Division de datos

# Entrenamiento

x_train = df.loc[:99, ['G3']]
y_train = df.loc[:99, ['absences']]

# Prueba

x_test = df.loc[100:, ['G3']]
y_test = df.loc[100:, ['absences']]

# Modelo

modelo = LinearRegression(fit_intercept = True)

# Entrenamiento

modelo.fit(x_train, y_train)

y_hat = modelo.predict(x_test)

# Metricas

MAE = mean_absolute_error(y_test, y_hat)
R2 = r2_score(y_test, y_hat)

print(MAE)
print(R2)

# Grafica sin prediccion

plt.subplots(figsize = (10, 5))

plt.scatter(x = df.G3, y = df.absences)
plt.show()

# Grafica con prediccion

plt.scatter(x_train, y_train)
plt.plot(x_test, y_hat)
plt.show()