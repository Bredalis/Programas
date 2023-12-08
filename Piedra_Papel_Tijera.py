
# Libreria

import random

# Obtener eleccion del usuario
def Obtener_Opcion_Usuario():
	
	usuario = input("Elije una (piedra, papel o tijera): ")

	while usuario.lower() not in ["piedra", "papel", "tijera"]:
		print("Eleccion incorrecta")

		usuario = input("Elije una (piedra, papel o tijera): ")

	return usuario

# Obtener eleccion de la maquina
def Obtener_Opcion_Maquina():
	
	opciones = ["piedra", "papel", "tijera"]
	maquina = random.choice(opciones)

	return maquina

# Mostrar el resultado del juego
def Determinar_Resultado(usuario, maquina):

	if usuario == maquina:
		return "Empate"

	elif (usuario == "piedra" and maquina == "tijera") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):
		return "Ganaste"

	else:
		return "Perdiste :("


# Inicio del juego
def Juega_Piedra_Papel_Tijera():

	print("Bienvenido al juego contra ordenador de piedra, papel o tijera")

	usuario = Obtener_Opcion_Usuario()
	maquina = Obtener_Opcion_Maquina()
	resultado = Determinar_Resultado(usuario, maquina)

	print("Elejiste", usuario)
	print("La maquina elijio", maquina)
	print(resultado)

Juega_Piedra_Papel_Tijera()