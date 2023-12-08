
import requests

print("Este es un programa para descargar imagenes de tipo .png, .jpg y .gift")

URL = input("Ingrese la url: ")
Nombre = input("Ingrese el nombre de la imagen: ")
Tipo = input("Ingrese el tipo de imagen que quiere: ")

def Descargar_Imagen(URL, Nombre, Tipo):

	Ruta = "C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/"

	Concatenacion = Ruta + Nombre + Tipo
	Imagen = requests.get(URL).content

	with open(Concatenacion, "wb") as Archivo:
		Archivo.write(Imagen)

Descargar_Imagen(URL, Nombre, Tipo)