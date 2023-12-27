
from PIL import Image

def conversion(url, nombre, tipo):

	ruta = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/' + nombre + '.' + tipo
	imagen_original = Image.open(url)
	imagen_original.save(ruta, format = tipo)