
# Programa que se encarga 
# de buscar cierta palabra 
# en un documento y diga 
# cuantas veces se repite

import re

class ManipulacionDeDocumento:
	def __init__(self, url, palabra):
		self.documento_url = url
		self.palabra = palabra

	def abrir_documento(self):
		self.documento = open(self.documento_url, 
			encoding = 'utf-8').read()

	def mostrar_documento(self):
		print(f'Documento: \n\n{self.documento}')

	def buscar_palabra(self):
		if re.search(self.palabra, self.documento) is not None:
			print(f'\nHemos encontrado la palabra: {self.palabra}')

		else:
			print(f'\nNo hemos encontrado la palabra: {self.palabra}')

	def repeticion_palabra(self):
		print(f'Veces que se repite: {len(re.findall(self.palabra, self.documento))}')

# documento = ManipulacionDeDocumento('C:/Users/Bradalis/Downloads/Borrar.txt', 'las')
# documento.abrir_documento()
# documento.mostrar_documento()
# documento.buscar_palabra()
# documento.repeticion_palabra()