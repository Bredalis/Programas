
import tkinter as tk
import time 

Window = tk.Tk()
Window.title('CLOCK')
Window.resizable(0,0)
Window.geometry('450x250')
Window.iconbitmap('C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Reloj.ico')

Window.columnconfigure(0, weight = 15)
Window.rowconfigure(0, weight = 15)
Window.columnconfigure(0, weight = 1)
Window.rowconfigure(1, weight = 1)

def Clock(): 

	Hour = time.strftime('%r')
	Day = time.strftime('%A') 
	Month = time.strftime('%d-%m-%Y')

	Resizing = Hour_Interfaces.winfo_height()
	Full_change = int((Resizing-5)*0.32)
	
	Hour_Interfaces.config(text = Hour, font = ('', Full_change))
	Day_Interfaces.config(text = Day, font = ('', 15))
	Date_Interfaces.config(text = Month, font = ('', 15))

	Window.after(1000, Clock)

Hour_Interfaces = tk.Button(Window, fg = 'aqua', bg = "black", cursor = 'clock', relief = 'groove', bd = 3, activebackground = '#ff0266')
Hour_Interfaces.grid(row = 0, sticky = 'snew', ipadx = 20 , ipady = 5)

Day_Interfaces = tk.Button(Window, fg = 'green2', bg = "gray2", cursor = 'clock', relief = 'groove', bd = 3, activebackground = '#ff0266')
Day_Interfaces.grid(row = 1, sticky = 'snew')

Date_Interfaces = tk.Button(Window, fg = 'blue', bg = 'gray3', cursor = 'clock', relief = 'groove', bd = 2, activebackground = '#00B0FF')
Date_Interfaces.grid(row = 2, sticky = 'snew')

Clock()

Window.mainloop()