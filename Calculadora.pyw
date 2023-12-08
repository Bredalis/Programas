
import tkinter as tk
import math

Ventana = tk.Tk()
Ventana.geometry('245x245') 
Ventana.title("CALCULATOR")
Ventana.resizable(0,0)
Ventana.config(bg = "white")

Ventana.iconbitmap('C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Calculadora.ico')

Contenido = open('Manual.txt', 'r').read()
exec(Contenido)

def Clean():
	Mi_Entry.delete(0, tk.END)

def Reclick(Valor):
	
	Anterior = Mi_Entry.get()

	Mi_Entry.delete(0, tk.END)
	Mi_Entry.insert(0, str(Anterior + str(Valor)))

def Binario():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = int(Numero_1)

	Operacion = 'B'

def Suma():

    global Numero_1
    global Operacion

    Numero_1 = Mi_Entry.get()
    Numero_1 = float(Numero_1)

    Mi_Entry.delete(0, tk.END)

    Operacion = '+'

def Resta():

	global Numero_1 
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '-'

def Multiplicacion():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '*'

def Division():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '/'

def Potencia():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = float(Numero_1)

	Mi_Entry.delete(0, tk.END)

	Operacion = '^'

def Radicacion():

	global Numero_1
	global Operacion

	Numero_1 = Mi_Entry.get()
	Numero_1 = int(Numero_1)

	Operacion = '√'
	
def Resultado():

	global Numero_2
	
	Numero_2 = Mi_Entry.get()
	Numero_2 = float(Numero_2)

	Mi_Entry.delete(0, tk.END)

	if Operacion == '+' :

		Mi_Entry.insert(0, Numero_1 + Numero_2)

	if Operacion == '-' :

		Mi_Entry.insert(0, Numero_1 - Numero_2)

	if Operacion == '*' :

		Mi_Entry.insert(0, Numero_1 * Numero_2)

	if Operacion == '^' :
		
		Mi_Entry.insert(0, Numero_1 ** Numero_2)

	if Operacion == 'B':

		Mi_Entry.insert(0, bin(Numero_1)[2:])

	if Operacion == '/':

		try:

			Mi_Entry.insert(0, Numero_1 / Numero_2)

		except ZeroDivisionError:

			Mi_Entry.insert(0, "Error")

	if Operacion == '√':

		Mi_Entry.insert(0, math.sqrt(Numero_1))

Condicion = True
Texto = tk.IntVar().set("")
Numero_1 = ""
Numero_2 = ""
Operacion = ""

Mi_Entry = tk.Entry(Ventana, textvariable = Texto, width = 40, justify = 'right', bg = "white")
Mi_Entry.grid(column = 0, row = 0, columnspan = 5)

tk.Button(Ventana, text = '1', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(1)).grid(column = 1, row = 1, pady = 10)
tk.Button(Ventana, text = '2', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(2)).grid(column = 2, row = 1, pady = 10)
tk.Button(Ventana, text = '3', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(3)).grid(column = 3, row = 1, pady = 10)

tk.Button(Ventana, text = '4', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(4)).grid(column = 1, row = 2, pady = 10)
tk.Button(Ventana, text = '5', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(5)).grid(column = 2, row = 2, pady = 10)
tk.Button(Ventana, text = '6', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(6)).grid(column = 3, row = 2, pady = 10)

tk.Button(Ventana, text = '7', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(7)).grid(column = 1, row = 3, pady = 10)
tk.Button(Ventana, text = '8', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(8)).grid(column = 2, row = 3, pady = 10)
tk.Button(Ventana, text = '9', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(9)).grid(column = 3, row = 3, pady = 10)

tk.Button(Ventana, text = '0', bg = '#A569BD', cursor  = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(0)).grid (column = 1, row = 4, pady = 10)
tk.Button(Ventana, text = '+', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = Suma).grid(column = 4, row = 1, pady = 10)
tk.Button(Ventana, text = 'x', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink',command = Multiplicacion).grid(column = 4, row = 2, pady = 10)

tk.Button(Ventana, text = '÷', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = Division).grid(column = 3, row = 4, pady = 10)
tk.Button(Ventana, text = '-', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = Resta).grid(column = 4, row = 3, pady = 10)
tk.Button(Ventana, text = 'π', bg = '#A569BD', cursor  = 'hand2', width = 5, activebackground = 'pink', command = lambda: Reclick(math.pi)).grid(column = 2, row = 4, pady = 10)
tk.Button(Ventana, text = '=', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = Resultado).grid(column = 4, row = 4, pady = 10)

tk.Button(Ventana, text = 'B', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = Binario).grid(column = 1, row = 5, pady = 10)
tk.Button(Ventana, text = '√', bg = '#A569BD', cursor  = 'hand2', width = 5, activebackground = 'pink', command = Radicacion).grid(column = 2, row = 5, pady = 10)
tk.Button(Ventana, text = '⌦', bg = '#A569BD', cursor  = 'hand2', width = 5, activebackground = 'pink', command = Clean).grid(column = 3, row = 5, pady = 10)
tk.Button(Ventana, text = '^', bg = '#A569BD', cursor = 'hand2', width = 5, activebackground = 'pink', command = Potencia).grid(column = 4, row = 5, pady = 10)

class Cerrar():

    def __init__(self, Herencia):

        self.X = tk.Toplevel(Herencia)
        self.X.title("Salir")

        self.Herencia = Herencia
        
        tk.Label(self.X, text = "¿Quieres cambiar de color?").grid(row = 0, column = 0, columnspan = 2)

        self.Si = tk.Button(self.X, text = "Si", activebackground = 'pink', command = self.Color)
        self.Si.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.No = tk.Button(self.X, text = "No", activebackground = 'pink', command = self.Salir)        
        self.No.grid(row = 1, column = 1, padx = 5, pady = 5)

    def Color(self):
        

    	global Condicion

    	if Condicion:

    		Ventana.config(bg = "black")

    		Mi_Entry.config(bg = "black")
    		Mi_Entry.config(fg = "white")

    		Condicion = False

    	else:

    		Ventana.config(bg = "white")
    		Mi_Entry.config(bg = "white")
    		Mi_Entry.config(fg = "black")

    		Condicion = True    	

    def Salir(self):

        self.X.destroy()
        self.Herencia.destroy()

class Calculadora():

    def __init__(self, Herencia):

        self.Herencia = Herencia
        self.Herencia.protocol("WM_DELETE_WINDOW", self.Al_Cerrar)

    def Al_Cerrar(self):

        Clase = Cerrar(Ventana)

        self.Herencia.wait_window(Clase.X)

if __name__ == "__main__":

    Clase = Calculadora(Ventana)

Manual('Manual_Calculadora.txt')

Ventana.mainloop()