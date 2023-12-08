
"""
Programa creado para visualizar 
cualquier imagen a partir de la url
"""

# Librerias

import tkinter as tk
from PIL import Image, ImageTk

def Visualizador(url):

	interfaz = tk.Tk()
	interfaz.resizable(0,0)
	interfaz.title("Imagenes")
	interfaz.iconbitmap("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Imagen.ico")
	
	foto = Image.open(url)
	img = ImageTk.PhotoImage(foto)

	fondo = tk.Label(interfaz, image = img)
	fondo.pack()

	interfaz.mainloop()