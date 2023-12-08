
def Conversion():

	print("Este es un programa capas de convertir de una temperatura a otra")

	Conversiones = ["C a K", "C a F", "K a C", "K a F", "F a C", "F a K"]

	print(f"Estas son las conversiones: {Conversiones}")

	Eleccion = int(input("Ingrese el tipo de conversion que desea (Por numeros del 0 al 5): "))
	Numero = int(input("Ingrese el numero que quiere convertir: "))

	if Eleccion == 0:
		print(f"Celsius a Kelvin = {Numero + 273.15} ")

	elif Eleccion == 1:
		print(f"Celsius a Fahrenheit = {(Numero * 9/5) + 32}")

	elif Eleccion == 2:
		print(f"Kelvin a Celsius = {Numero - 273.15}")

	elif Eleccion == 3:
		print(f"Kelvin a Fahrenheit = {(Numero - 273.15) * 9/5 + 32}")

	elif Eleccion == 4:
		print(f"Fahrenheit a Celsius = {(Numero - 32) * 5/9}")

	elif Eleccion == 5:
		print(f"Fahrenheit a Kelvin = {(Numero - 32) * 5/9 + 273.15}")

Conversion()