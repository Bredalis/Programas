
# Programa que evalua la relacion 
# entre el numero de vistas y la 
# duracion de los videos de BTS

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Leer datos

url = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Datasets/CSV/bts_videos.csv'
df = pd.read_csv(url)

print(df)
print(df.shape)

# Division de datos

# Entrenamiento

x_train = df.loc[248:, ['duracion']]
y_train = df.loc[248:, ['numero_de_vistas']]

# Prueba

x_test = df.loc[:247, ['duracion']]
y_test = df.loc[:247, ['numero_de_vistas']]

print(x_train)
print(len(x_train))

print(y_train)
print(len(y_train))

print(x_test)
print(len(x_test))

print(y_test)
print(len(y_test))

# Modelo

modelo = LinearRegression(fit_intercept = True)

# Entrenamiento

for i in range(0, 1000):
	modelo.fit(x_train, y_train)

# Prediccion

y_hat = modelo.predict(x_test)

MSE = mean_squared_error(y_test, y_hat)
R2 = r2_score(y_test, y_hat)

print(MSE)
print(R2)

# Grafica sin prediccion

df.plot.scatter(x = 'duracion', y = 'numero_de_vistas')
plt.show()

# Grafica con prediccion 

plt.scatter(x_train, y_train)
plt.plot(x_train, y_hat)

plt.show()