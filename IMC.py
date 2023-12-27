
from math import floor

contenido = open('Manual.txt').read()
exec(contenido)

manual('Manual_IMC.txt')

def imc():

	peso = int(input('Ingrese su peso: '))
	altura = float(input('Ingrese su altura: '))

	resultado = floor(peso / (altura * altura))

	if resultado < 18.5:
		print(f'IMC: {resultado}, Peso Bajo')

	elif resultado >= 18.5 and resultado <= 24.9:
		print(f'IMC: {resultado}, Peso Normal')

	elif resultado >= 25 and resultado <= 29.9:
		print(f'IMC: {resultado}, Sobrepeso')

	elif resultado >= 30:
		print(f'IMC: {resultado}, Obesidad')

imc()