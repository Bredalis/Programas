
import openai

class ResumirTexto:

	def texto(self):
		self.prompt = input('Texto: ')

	def estructura(self):
		openai.api_key = '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'

		self.mensaje = [
			{'role': 'system', 'content': 'Simplify text to a level appropriate for a second-grade student'},
			{'role': 'user', 'content': self.prompt}
		]

	def modelo(self):

		self.respuesta = openai.chat.completions.create(
			model = 'gpt-3.5-turbo',
			messages = self.mensaje,
			temperature = 0.4,
			max_tokens = 100,
			top_p = 0.4
		)

	def mostra_respuesta(self):
		print('\nResumen:\n')
		print(self.respuesta.choices[0].message.content)

resumir_texto = ResumirTexto()
resumir_texto.texto()
resumir_texto.estructura()
resumir_texto.modelo()
resumir_texto.mostra_respuesta()