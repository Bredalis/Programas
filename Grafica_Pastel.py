
class Pastel:

	def __init__(self):

		self.Lista_Nombres = []
		self.Lista_Cantidades = []
		self.Pregunta = ""

	def Ejecucion(self):

		while self.Pregunta != "No":

			try:
				self.Nombres = input("Nombre: ")	
				self.Cantidades = int(input("Porcentaje: "))
				
				self.Lista_Nombres.append(self.Nombres)
				self.Lista_Cantidades.append(self.Cantidades)

			finally:
				self.Pregunta = input("¿Quieres seguir ingresando integrantes?: ")

	def Grafica(self):

		plt.pie(self.Lista_Cantidades, labels = self.Lista_Nombres)

		plt.title("Grafica de Pastel")
		plt.show()

if __name__ == "__main__":

	import matplotlib.pyplot as plt

	Pastel = Pastel()

	Pastel.Ejecucion()
	Pastel.Grafica()