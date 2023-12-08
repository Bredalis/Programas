
print("Clasificador de notas con valor de 100 puntos")

while(True):

	try:
		Nota = int(input("Nota: "))

		if Nota >= 90 and Nota <= 100:
			print("¡Excelente, eres inteligente!")

		elif Nota <= 70:
			print("Tienes que mejorar")

		elif Nota < 90 and Nota > 70 and Nota < 100:
			print("¡Muy Bien, eres aplicado!")

		break

	except ValueError:
		print("Solo Numeros")	