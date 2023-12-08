
# Librerias

from PIL import Image, ImageTk
import tkinter as tk
import random

# Lectura de datos

Contenido = open("Manual.txt", "r").read()
exec(Contenido)

Manual("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Python/Programas/Manual_Ahorcado.txt")

# Categorias de palabras

Contenido = open("Categorias_Ahorcado.txt", "r").read()
exec(Contenido)

Categorias = {
	"Comida": Comida, "Sentimientos": Sentimientos, "Paises": Paises, "Nombres": Nombres, "Cosas": Cosas, "Animales": Animales,
	"Artistas": Artistas
}

# Mecanica del juego

def Personaje_Ahorcado():

	Ventana = tk.Tk()
	Ventana.title("Ahorcado")
	Ventana.resizable(0,0)

	Ruta = Image.open("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Ahorcado.ico")
	
	Imagen = ImageTk.PhotoImage(Ruta)

	Etiqueta = tk.Label(Ventana, image = Imagen)
	Etiqueta.pack()

	Ventana.mainloop()

def Seleccionar_Palabra():

	Categoria = input("Ingrese el tipo de categoria entre (Comida, Sentimientos, Paises, Nombres, Cosas, Animales, Artistas):")

	print(f"La categoria es: {Categoria}")
	Palabra = random.choice(Categorias[Categoria])

	return Palabra

def Inicializar_Tablero(Palabra):	
	return ["_"] * len(Palabra)

def Mostrar_Tablero(Tablero):
	print(" ".join(Tablero))

def Pedir_Letra():

	Letra = input("Intoduce la letra: ")
	return Letra.lower()

def Actualizar_Tablero(Palabra, Tablero, Letra):

	for i in range(len(Palabra)):

		if Palabra[i] == Letra:
			Tablero[i] = Letra

def Jugar_Ahorcado():
	
	Palabra = Seleccionar_Palabra()
	Intentos_Maximos = 6
	Intentos = 0
	Tablero = Inicializar_Tablero(Palabra)

	while "_" in Tablero and Intentos < Intentos_Maximos:

		Mostrar_Tablero(Tablero)
		Letra = Pedir_Letra()

		if Letra in Palabra:

			Actualizar_Tablero(Palabra, Tablero, Letra)
			print("Correcto!")

		else:

			Intentos += 1

			for i in range(1, 6):

				if Intentos == i:
					print(f"Te quedan {6 - i} intentos")

			print("Incorrecto. Intentos {}/{}".format(Intentos, Intentos_Maximos))

	if "_" not in Tablero:
		print("Ganaste la palabra era:", Palabra)

	else:
		print("Perdiste :(")
		Personaje_Ahorcado()

Jugar_Ahorcado()