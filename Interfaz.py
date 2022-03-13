from tkinter import *

from Gestor import Gestor


class Interfaz:

    def __init__(self):
        raiz = Tk()
        raiz.title("Analizador, Proyecto1 LFP")
        raiz.resizable(0,0)
        raiz.iconbitmap("Icono.ico")
        #raiz.geometry("850x550")
        #raiz.config(bg="White")
        miFrame = Frame()
        miFrame.pack()
        #miFrame.config(bg="White")
        miFrame.config(width="850",height="550")

        #self.texto = StringVar()

        #miLabel = Label(miFrame, text="Prueba Label", fg="Blue", font=("Comic Sans MS", 18))
        #miLabel.place(x=150,y=250)
        #areaAnalizar = Label(miFrame, text="Ingresar el texto a analizar")
        #areaAnalizar.grid(row=1, column=0 ,padx=20, pady=20)
        #areaAnalizar.place(x=50,y=100)
        self.analizar = Text(miFrame)
        #analizar.grid(row=1, column=1, padx=20, pady=20)
        self.analizar.place(x=100,y=80)
        #scroll = Scrollbar(miFrame, command=analizar.yview)
        #scroll.place(x=800,y=100)
        #analizar.config(yscrollcommand=scroll.set)
        botonAnalizar = Button(miFrame, text="Analizar", font=("Comic Sans MS", 10),width=12, height=2, command=self.Analizar)
        botonAnalizar.place(x=100, y=480)
        botonCargar = Button(miFrame, text="Cargar Archivo", font=("Comic Sans MS", 10),width=15, height=2, command=self.CargarArchivo)
        botonCargar.place(x=615, y=480)



        raiz.mainloop()

    def Analizar(self):
        texto = self.analizar.get(1.0, "end-1c")  #->PARA PODER SACAR LA INFORMACION DEL CAMPO
        #texto = self.analizar.insert(1.0, "HOLAAAAAAAAAAA\n")  #->PARA PODER METER EL TEXTO EN EL CAMPO
        print(texto)

    def CargarArchivo(self):
        gestor = Gestor()
        self.analizar.insert(1.0,gestor.CargarData())
