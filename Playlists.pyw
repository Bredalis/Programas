
"""
Programa que reproduce 
musica en mp3
"""

class Reproductor_De_Musica:

	def __init__(self, interfaz):

		# Propiedades de la interfaz
		
		self.interfaz = interfaz
		self.interfaz.title("PlayList")
		self.interfaz.geometry("210x100")
		self.interfaz.resizable(0,0)
		self.interfaz.config(bg = "#edd269")
		self.icono = "C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Playlists.ico"
		self.interfaz.iconbitmap(self.icono)

		self.playlist = [] # Lista de musica

		pygame.init()
		pygame.mixer.init()

		# Botones

		self.cargar = tk.Button(self.interfaz, text = "Cargar", bg = "#aee239", command = self.Cargar).pack()
		self.reproducir = tk.Button(self.interfaz, text = "Reproducir", bg = "#aee239", command = self.Reproducir).pack()
		self.pausar = tk.Button(self.interfaz, text = "Pausar", bg = "#aee239", command = self.Pausar).pack()
		self.reanudar = tk.Button(self.interfaz, text = "Reanudar", bg = "#aee239", command = self.Reanudar).pack()

	# Funcion que busca y guarda la musica
	def Cargar(self):
		cancion = filedialog.askopenfilename(title = "Musica", initialdir = "C:", 
			filetypes = (("Archivo de audio", "*.mp3"), ("todos los archivos", "*.*")))

		self.playlist.append(cancion) # Se guarda aqui

	# Funcion que reproduce la musica
	def Reproducir(self):
		if len(self.playlist) == 0:
			return

		pygame.mixer.music.load(self.playlist[0])
		pygame.mixer.music.play()

	# Pausa la musica
	def Pausar(self):
		pygame.mixer.music.pause()

	# Reanuda la musica
	def Reanudar(self):
		pygame.mixer.music.unpause()

if __name__ == "__main__":

	# Librerias

	import pygame
	import tkinter as tk
	from tkinter import filedialog

	# Interfaz

	interfaz = tk.Tk()
	app = Reproductor_De_Musica(interfaz)
	interfaz.mainloop()