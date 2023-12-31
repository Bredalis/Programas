
# Librerias

import time
import pygame
import tkinter as tk
from PIL import Image, ImageTk

interfaz = tk.Tk()
interfaz.title('Temporizador')
interfaz.geometry('245x230')
interfaz.resizable(0, 0)

# Icono

img = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Reloj.ico'
interfaz.iconbitmap(img)

# Funcion temporizadora

def temporizador(minutos):

	minutos = minutos
	segundos_totales = minutos * 60

	while segundos_totales > 0:

		minutos_restantes, segundos_restantes = divmod(segundos_totales, 60)
		print(minutos_restantes, ':', segundos_restantes)	
		time.sleep(1)

		segundos_totales -= 1

	print('¡Tiempo terminado!')
	sonido()

# Sonido que indica que la temporizacion a terminado

def sonido():

	pygame.init()

	url = pygame.mixer.Sound('C:/Users/Angelica Gerrero/Videos/Reloj.mp3')
	pygame.mixer.Sound.play(url, 5)

# Funcion para repetir la temporizacion

def repetir(cantidad):	
	temporizador(cantidad)

repetir(0)

# Imagen

url = Image.open(img)
img = ImageTk.PhotoImage(url)

tk.Label(interfaz, image = img).pack() 
tk.Button(interfaz, text = 'Repetir', 
	command = lambda: repetir(0)).place(x = 12, y = 10)

interfaz.mainloop()