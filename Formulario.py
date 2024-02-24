
# Librerias

import tkinter as tk
import sqlite3 as sqlite

ventana = tk.Tk()
ventana.title('Formulario')
ventana.resizable(0, 0)
ventana.config(bg = 'pink')
ventana.geometry('340x310')

ventana.iconbitmap('C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Registro_2.ico')

# Guardar datos en la bbdd

def manipular_boton(contenedores):

	for i in contenedores:
		if i.get() == '':
			boton.config(text = 'Guardado')

def limpiar_datos(contenedores):

	for i in contenedores:
		i.set('')

def guardar_datos(contenedores):

	bbdd = sqlite.connect('C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/BBDD/Programas/SQLITE3/Formulario.db')
	cursor = bbdd.cursor()
	instruccion = f'INSERT INTO Formulario VALUES("{ID.get()}", "{nombre.get()}", "{edad.get()}", "{hobby.get()}")'
	cursor.execute(instruccion)

	limpiar_datos(contenedores)
	manipular_boton(contenedores)

	bbdd.commit()
	bbdd.close()

tk.Label(ventana, text = 'Formulario', bg = 'pink', 
	pady = 10, font = (25)).pack()

# Contenedores de informacion

ID = tk.StringVar()
nombre = tk.StringVar()
edad = tk.StringVar()
hobby = tk.StringVar()
contenedores = [ID, nombre, edad, hobby]

# Etiquetas y campos a llenar

tk.Label(ventana, text = 'ID:', bg = 'pink').pack()
barra_id = tk.Entry(ventana, textvariable = ID)
barra_id.pack(pady = 10)

tk.Label(ventana, text = 'Nombre:', bg = 'pink').pack()
barra_nombre = tk.Entry(ventana, textvariable = nombre)
barra_nombre.pack(pady = 10)

tk.Label(ventana, text = 'Edad:', bg = 'pink').pack()
barra_edad = tk.Entry(ventana, textvariable = edad)
barra_edad.pack(pady = 10)

tk.Label(ventana, text = 'Hobby:', bg = 'pink').pack()
barra_hobby = tk.Entry(ventana, textvariable = hobby)
barra_hobby.pack(pady = 10)

# Boton para guardar

boton = tk.Button(ventana, text = 'Guardar', 
	command = lambda: guardar_datos(contenedores))
boton.place(x = 200, y = 272)

ventana.mainloop()