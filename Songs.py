
# Listas de canciones 
# favoritas para escuchar

class ListaDeCanciones():
	def __init__(self):

		self.lista = []

	def informacion(self, tipo):
		print(f'\nCanciones {tipo}: \n')

		for i in self.lista:
			print('\t-', i)

class Tristes(ListaDeCanciones):
	def __init__(self):

		self.lista = ['Before You Go',  'Fire On Fire', 
		'We Dont Talk Anymore',	'Bad Liar', 'Let Me Down Slowly',
		'Summertime', 'Faded', 'Another Love', 'Demons', 'Someone You Loved']

	def informacion(self):
		super().informacion('tristes')

class Pop(ListaDeCanciones):
	def __init__(self):

		self.lista = ['Hymn For The Weekend',  'Human', 'Middle Of The Night'
		'New Rules', 'Treat You Better', 'Unstoppable', 'Woman', 
		'Middle Of The Night', 'Satisfya', 'Ainsi Bas La Vida',
		'Derniére Danse']

	def informacion(self):
		super().informacion('pop')

class Kpop(ListaDeCanciones):
	def __init__(self):

		self.lista = ['I Am', 'Super Shy', 'Seven', 'OMG',
		'EAT',  'Fast Forward', 'The Feels', 'Money', 'Ditto',
		'ASAP']

	def informacion(self):
		super().informacion('kpop')

# Mostrar canciones

tristes = Tristes()
tristes.informacion()

pop = Pop()
pop.informacion()

kpop = Kpop()
kpop.informacion()