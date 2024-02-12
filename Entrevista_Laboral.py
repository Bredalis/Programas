
# Programa que genera una serie 
# de preguntas tipo entrevista 
# para cualquier area laboral

import openai

class EntrevistaLaboral:
	def __init__(self, area_laboral):

		self.area_laboral = area_laboral

	def estructura(self):
		openai.api_key = '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'

		self.mensaje = [
			{'role': 'system', 'content': f'Crea una lista de 10 preguntas para una entrevista de trabajo sobre {self.area_laboral}'},
			{'role': 'user', 'content': self.area_laboral}
		]

	def modelo(self):
		self.respuesta = openai.chat.completions.create(
			model = 'gpt-3.5-turbo',
			messages = self.mensaje,
			temperature = 0.1,
			top_p = 0
		)

	def mostrar_respuesta(self):
		print(self.respuesta.choices[0].message.content)

entrevista = EntrevistaLaboral('Informatica')
entrevista.estructura()
entrevista.modelo()
entrevista.mostrar_respuesta()