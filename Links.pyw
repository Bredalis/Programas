
# Librerias

import tkinter as tk
import webbrowser as wb
import subprocess as sp

Ventana =  tk.Tk()
Ventana.geometry("200x150")
Ventana.resizable(0,0)
Ventana.config(bg = "pink")
tk.Wm.wm_title(Ventana, "Links")
Ventana.iconbitmap('C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Python_2.ico')

def Youtube():
	wb.open("https://www.youtube.com/feed/library")

def Word():
	wb.open("https://educrd-my.sharepoint.com/personal/a21a34804_educacion_edu_do/_layouts/15/doc.aspx?sourcedoc={1f85debc-4353-4562-af67-1275aa6964ad}&action=edit")

def BDBrowser():
	sp.run("C:/Program Files (x86)/DB Browser for SQLite/DB Browser for SQLite.exe")

def Visual_Code():
	sp.run("C:/Users/Angelica Gerrero/AppData/Local/Programs/Microsoft VS Code/Code.exe")

def Git():
	sp.run("C:/AngelicaGuerrero/Git/git-bash.exe")

tk.Button(Ventana, text = "Youtube", activebackground = "red", bg = "skyblue", command = Youtube).pack()
tk.Button(Ventana, text = "Word", activebackground = "blue", bg = "skyblue", command = Word).pack()
tk.Button(Ventana, text = "BDBrowser", bg = "skyblue", command = BDBrowser).pack()
tk.Button(Ventana, text = "Visual Studio Code", activebackground = "skyblue", bg = "skyblue", command = Visual_Code).pack()
tk.Button(Ventana, text = "GIT", activebackground = "green", bg = "skyblue", command = Git).pack()

Ventana.mainloop()