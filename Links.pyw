
# Librerias

import tkinter as tk
import webbrowser as wb
import subprocess as sp

ventana =  tk.Tk()
ventana.geometry('200x150')
ventana.resizable(0, 0)
ventana.config(bg = 'pink')
tk.Wm.wm_title(ventana, 'Links')

icono = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Python_2.ico'
ventana.iconbitmap(icono)

def youtube():
	wb.open('https://www.youtube.com/feed/library')

def bdbrowser():
	sp.run('C:/Program Files (x86)/DB Browser for SQLite/DB Browser for SQLite.exe')

def visual_code():
	sp.run('C:/Users/Angelica Gerrero/AppData/Local/Programs/Microsoft VS Code/Code.exe')

def git():
	sp.run('C:/AngelicaGuerrero/Git/git-bash.exe')

tk.Button(ventana, text = 'Youtube', activebackground = 'red', bg = 'skyblue', 
	command = youtube).pack()

tk.Button(ventana, text = 'BDBrowser', bg = 'skyblue', 
	command = bdbrowser).pack()

tk.Button(ventana, text = 'Visual Studio Code', activebackground = 'skyblue', 
	bg = 'skyblue', command = visual_code).pack()

tk.Button(ventana, text = 'Git', activebackground = 'green', bg = 'skyblue', 
	command = git).pack()

ventana.mainloop()