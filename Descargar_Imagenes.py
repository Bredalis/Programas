
import requests

print('Este es un programa para descargar imagenes de tipo .png, .jpg y .gift')

url = input('Ingrese la url: ')
nombre = input('Ingrese el nombre de la imagen: ')
tipo = input('Ingrese el tipo de imagen que quiere: ')

def descargar_imagen(url, nombre, tipo):

	ruta = 'C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Icon/Imagenes/'

	concatenacion = ruta + nombre + tipo
	imagen = requests.get(url).content

	with open(concatenacion, 'wb') as archivo:
		archivo.write(imagen)

descargar_imagen(url, nombre, tipo)