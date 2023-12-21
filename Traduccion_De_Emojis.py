
def Traduccion_Emojis(solicitud):

	import openai
	openai.api_key = "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"

	# Prompts y estrutura de mensajes

	contenido = """
	Se te proporcionará texto y tu tarea es 
	traducirlo a emojis. No utilice ningún texto 
	normal. Haz tu mejor esfuerzo solo con emojis """ 

	mensaje = [
		{"role": "system", "content": contenido},
		{"role": "user", "content": solicitud},
	]

	# Modelo y respuesta
	respuesta = openai.chat.completions.create(
		model = "gpt-3.5-turbo",
		messages = mensaje,
		temperature = 0.8,
		max_tokens = 64
	)

	print(respuesta.choices[0].message.content)