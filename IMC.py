
from math import floor

Contenido = open("Manual.txt").read()
exec(Contenido)

Manual("Manual_IMC.txt")

def IMC():

	Peso = int(input("Ingrese su peso: "))
	Altura = float(input("Ingrese su altura: "))

	Resultado = floor(Peso / (Altura * Altura))

	if Resultado < 18.5:
		print(f"IMC: {Resultado}, Peso Bajo")

	elif Resultado >= 18.5 and Resultado <= 24.9:
		print(f"IMC: {Resultado}, Peso Normal")

	elif Resultado >= 25 and Resultado <= 29.9:
		print(f"IMC: {Resultado}, Sobrepeso")

	elif Resultado >= 30:
		print(f"IMC: {Resultado}, Obesidad")

IMC()