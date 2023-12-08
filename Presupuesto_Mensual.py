
# Librerias

import pandas as pd
import sqlite3 as sqlite
import matplotlib.pyplot as plt

url_presupuesto = "C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/BBDD/Programas/SQLITE3/Presupuesto.db"

# Conectar a BBDD

bbdd_presupuesto = sqlite.connect(url_presupuesto)

# Obtener todas las columnas de las tablas

presupuesto = pd.read_sql("SELECT * FROM Monthly", bbdd_presupuesto)
print(f"Presupuesto: \n{presupuesto}")

# Mostrar gastos mensuales

def Gastos():

	plt.bar(presupuesto.MONTH, presupuesto.SPENDING, color = "pink")
	
	plt.title("Gastos")
	plt.show()

# Mostrar presupuesto mensual

Gastos()

plt.bar(presupuesto.MONTH, presupuesto.INCOME, color = "pink")

plt.title("Presupuesto Mensual (Ingresos)")
plt.show()