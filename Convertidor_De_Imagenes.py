
from PIL import Image

def Conversion(URL, Nombre, Tipo):

	Ruta = "C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/" + Nombre + "." + Tipo
	Imagen_Original = Image.open(URL)
	Imagen_Original.save(Ruta, format = Tipo)