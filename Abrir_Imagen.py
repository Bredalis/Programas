
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

Foto = ""

Contenido = open('Manual.txt', 'r').read()

exec(Contenido)

def Abrir_Imagen():

    Ventana = tk.Tk()
    Ventana.title("Imagen")
    Ventana.resizable(0,0)
    Ventana.iconbitmap("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Camara_2.ico")

    global Foto

    try:

        Folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", 
            filetypes = (("Icon", "*.png"), ("Icon", "*.ico"), ("Icon", "*.jpg")))

        Img = Image.open(Folder)

        Foto = ImageTk.PhotoImage(Img)

        Etiqueta = tk.Label(Ventana, image = Foto)
        Etiqueta.pack()

        class Cerrar:

            def __init__(self, Herencia):

                self.X = tk.Toplevel(Herencia)
                self.X.title("Salir")

                self.Herencia = Herencia
                
                tk.Label(self.X, text = "¿Quieres abrir otra?").grid(row = 0, column = 0, columnspan = 2)

                self.Si = tk.Button(self.X, text = "Si", activebackground = "skyblue", command = self.Salir)
                self.Si.grid(row = 1, column = 0, padx = 5, pady = 5)

                self.No = tk.Button(self.X, text = "No", activebackground = "skyblue", command = self.Minimizar)        
                self.No.grid(row = 1, column = 1, padx = 5, pady = 5)

            def Salir(self):

                global Foto

                try:

                    Folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", 
                        filetypes = (("Icon", "*.png"), ("Icon", "*.ico"), ("Icon", "*.jpg")))

                    Img = Image.open(Folder)

                    Foto = ImageTk.PhotoImage(Img)

                    Etiqueta.config(image = Foto)

                except AttributeError:
                    print("Ha ocurrido un error")         

            def Minimizar(self):

                self.X.destroy()
                self.Herencia.destroy()

        class Registro:

            def __init__(self, Herencia):

                self.Herencia = Herencia
                self.Herencia.protocol("WM_DELETE_WINDOW", self.Al_Cerrar)

            def Al_Cerrar(self):
                Clase = Cerrar(Ventana)
                self.Herencia.wait_window(Clase.X)

        if __name__ == "__main__":

            Clase = Registro(Ventana)

    except Exception: 
        print("Ocurrio un error")

    Ventana.mainloop()

Manual('Manual_Abrir_Imagen.txt')
Abrir_Imagen()