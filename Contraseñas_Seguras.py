
import pymongo

# Conectar a la bbdd

try:
	cliente = pymongo.MongoClient('mongodb://localhost:27017')
	db = cliente['Contraseñas_Seguras']
	coleccion = db['Google'] # Nombre de la coleccion

	# # Datos a insertar
	# datos = {'Contraseña': 'jswop34-2mdjpo%$fgs'}
	# coleccion.insert_one(datos)

	cliente.close()

except Exception:
	print('Ha ocurrido un error')	