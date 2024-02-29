
import openai
from textwrap import wrap

class GeneradorDeHistorias:
	def __init__(self, api, prompt):
		self.api = api
		self.instruccion_usuario = prompt

	def obtener_api(self):
		openai.api_key = self.api

	def creacion_de_instrucciones(self):

		self.instruccion_modelo = f'''

		Eres un experto creando historias largas e intrigantes. Escribe
		una historia con los (datos) que te pida el usuario, por ejemplo: 
		algun genero, personajes, lugares, dialogos, todas las cosas que 
		te pida el usuario. La hitoria no debe ser de mas de 5 parrafos.
		(datos) = {self.instruccion_usuario}.
		'''

	def instrucciones_del_modelo(self):

		self.mensajes = [
			{'role': 'system', 'content': self.instruccion_modelo},
			{'role': 'user', 'content': self.instruccion_usuario}
		]		

	def crear_modelo(self):
		
		self.modelo = openai.chat.completions.create(
			model = 'gpt-3.5-turbo',
			messages = self.mensajes,
			temperature = 1,
			max_tokens = 1000
		)

	def mostrar_respuestas(self):
		print('\n'.join(wrap(self.modelo.choices[0].message.content)))

# Datos para la historia

datos = '''

Para mi historia, quiero que el personaje principal se llame Lucas,
sea de genero de suspenso y sea la playa
'''

historia_suspenso = GeneradorDeHistorias(
	'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', 
	datos
)

historia_suspenso.obtener_api()
historia_suspenso.creacion_de_instrucciones()
historia_suspenso.instrucciones_del_modelo()
historia_suspenso.crear_modelo()
historia_suspenso.mostrar_respuestas()