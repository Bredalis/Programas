
"""
Obtiene palabras clave 
de un bloque de texto
"""

def Palabras_Clave(texto):
	
	import openai
	openai.api_key = "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"

	# Prompts y estructura del modelo
	
	contenido = """
		Se le proporcionará un bloque de texto y su tarea 
		será extraer de él una lista de palabras clave """

	mensaje = [
		{"role": "system", "content": contenido},
		{"role": "user", "content": texto}
	]

	# Modelo
	
	respuesta = openai.chat.completions.create(
		model = "gpt-3.5-turbo",
		messages = mensaje,
		temperature = 0.5,
		max_tokens = 64
	)

	print(respuesta.choices[0].message.content)