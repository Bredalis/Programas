
import matplotlib.pyplot as plt

anios = [10000, 9000, 8500, 7500] 

eventos = ['Domesti. de plantas', 'Domesti. de animales', 
	'Inicio de la agricultura e Jericó', 'Desarrollo de la céramica en Anatolia']

colores = ['green', 'red', 'blue', 'brown']

plt.bar(eventos, anios, color = colores)

plt.title('Revolución Neolítica')
plt.ylabel('A.C')
plt.xlabel('Eventos')

plt.show()