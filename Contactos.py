
# Obtener y mostrar contactos
# para el programa de whatsapp

import sqlite3 as sqlite
import pandas as pd

class Contactos:
	def __init__(self, url):
		
		self.bbdd = sqlite.connect(url)
		self.cursor = self.bbdd.cursor()

	def instruccion(self):
		self.instruccion = f'SELECT * FROM Contactos'
		self.cursor.execute(self.instruccion)

	def obtener_datos(self):
		self.datos = self.cursor.fetchall()

	def crear_df(self):
		self.df = pd.DataFrame(self.datos, 
			columns = ['id', 'nombres', 'numeros_telefonicos'])

	def mostrar_contactos(self):
		print(self.df) 

# Mostra contactos

url = 'G:/Mi unidad/LenguajesDeProgramacion/BBDD/Programas/SQLITE3/Contactos.db'
bbdd = Contactos(url)
bbdd.instruccion()
bbdd.obtener_datos()
bbdd.crear_df()
bbdd.mostrar_contactos()