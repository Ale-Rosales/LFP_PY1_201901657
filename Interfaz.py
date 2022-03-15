from tkinter import *
from Gestor import Gestor
from Analizador import Analizador
import easygui
import os
import webbrowser

gestor = Gestor()
analizar = Analizador()

class Interfaz:
    def __init__(self):
        self.tipo = []
        self.fondo = []
        self.valor = []
        self.evento = []

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

        #DOCUMENTACION 110
        reportes = Label(miFrame, text="Reportes", font=("Comic Sans MS", 15))
        reportes.place(x=50,y=20)
        botonTokens = Button(miFrame, text="Reporte\nTokens", font=("Comic Sans MS", 10),width=12, height=2, command=self.ReporteTokens)
        botonTokens.place(x=160, y=10)
        botonErrores = Button(miFrame, text="Reporte\nErrores", font=("Comic Sans MS", 10),width=12, height=2, command=self.ReporteErrores)
        botonErrores.place(x=280, y=10)
        manuales = Label(miFrame, text="Manuales", font=("Comic Sans MS", 15))
        manuales.place(x=470,y=20)
        botonUsuario = Button(miFrame, text="Manual\nUsuario", font=("Comic Sans MS", 10),width=12, height=2)
        botonUsuario.place(x=580, y=10)
        botonTecnico = Button(miFrame, text="Manual\nTecnico", font=("Comic Sans MS", 10),width=12, height=2)
        botonTecnico.place(x=700, y=10)

        raiz.mainloop()

    def Analizar(self):
        texto = self.analizar.get(1.0, "end-1c")  #->PARA PODER SACAR LA INFORMACION DEL CAMPO
        #texto = self.analizar.insert(1.0, "HOLAAAAAAAAAAA\n")  #->PARA PODER METER EL TEXTO EN EL CAMPO
        #analizar.analizar(texto)
        #analizar.imprimirTokens()
        #analizar.imprimirErrores()
        analizar.analizar2(texto)
        analizar.imprimirT()
        analizar.imprimirE()

    def CargarArchivo(self):
        self.analizar.insert(1.0,gestor.CargarData())

    def obtenerData(self,token):
        if token.tipo == "Para HTML":
            return token.lexema
    
    def Todos(self):
        self.DataEvento()
        self.DataFondo()
        self.DataTipo()
        self.DataValor()
    
    def Prueba(self):
        for x in self.tipo:
            print(x)

    # Identificador_tipo dosPuntos comillaDoble Para HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3         i+4     i+5

    # Identificador_valor dosPuntos comillaDoble Para HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3         i+4     i+5 
    
    # Identificador_fondo dosPuntos comillaDoble Para HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3         i+4     i+5

    # Identificador_evento dosPuntos comillaDoble Para HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3         i+4     i+5 

    def DataTipo(self):
        tokens = analizar.Tokens
        #print("\n")
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_tipo":
                texto = self.obtenerData(tokens[i+3])
                self.tipo.append(texto)
                #print(texto)

    def DataValor(self):
        tokens = analizar.Tokens
        #print("\n")
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_valor":
                texto = self.obtenerData(tokens[i+3])
                self.valor.append(texto)
                #print(texto)

    def DataFondo(self):
        tokens = analizar.Tokens
        #print("\n")
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_fondo":
                texto = self.obtenerData(tokens[i+3])
                self.fondo.append(texto)
                #print(texto)

    def DataEvento(self):
        tokens = analizar.Tokens
        #print("\n")
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_evento":
                texto = self.obtenerData(tokens[i+3])
                self.evento.append(texto)
                #print(texto)

    #----------------------------REPORTES----------------------------

    def ReporteTokens(self):
        tokens = analizar.Tokens
        textoTabla = ""
        txtFinal = ('</div>'
        '</body>'
        '</html>')

        i = 0

        for x in tokens:
            i += 1
            textoTabla = textoTabla+'<tr>'+'<td>'+str(x.lexema)+'</td>'+'<td>'+str(x.linea)+'</td>'+'<td>'+str(x.columna)+'</td>'+'<td>'+str(x.tipo)+'</td>'+'</tr>'

        contenidoHTML = (
        '<!DOCTYPE html>'
        '<html>' 
        '<head> '
        '<meta charset="utf-8"> '
        '<title>Reporte Tokens</title>'
        '<link href="assets/css/bootstrap-responsive.css" type="text/css" rel="stylesheet">'
        '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" type="text/css" rel="stylesheet">'
        '<link rel="stylesheet" type="text/css"  href="Style.css">'
        '<link rel="stylesheet" type="text/css" href="bootstrap.css">'
        '</head>'
        '<body>'
        '<div class="container-fluid welcome-page" id="home">'
        '<div class="jumbotron">'
        '<h1>'
        '<span>Reporte Tokens</span>'
        '</h1>'
        '</div>'
        '</div>')
        
        file = open("./REPORTES/ReporteTokens.html","w")
        file.write(str(contenidoHTML))
        file.write('<h2>'
        '<span>Analisis Realizado</span>'
        '</h2>')

        txtHtml=(
        '<table class="table table-responsive">'
        '<thead>'
        '<tr>'
        '<th scope="col">Lexema</th>'
        '<th scope="col">Linea</th>'
        '<th scope="col">Columna</th>'
        '<th scope="col">Tipo</th>'
        '</tr>'
        '</thead>'
        '<tbody>')

        for x in tokens:
            i += 1
            txtHtml = txtHtml+'<tr>'+'<td>'+str(x.lexema)+'</td>'+'<td>'+str(x.linea)+'</td>'+'<td>'+str(x.columna)+'</td>'+'<td>'+str(x.tipo)+'</td>'+'</tr>'

        file.write(txtHtml)
        file.write('</tbody>'
        '</table>'
        '</div>'
        '</div>')

        file.write(txtFinal)
        file.close()
    
    def ReporteErrores(self):
        errores = analizar.Errores
        textoTabla = ""
        txtFinal = ('</div>'
        '</body>'
        '</html>')

        i = 0

        for x in errores:
            i += 1
            textoTabla = textoTabla+'<tr>'+'<td>'+str(x.descripcion)+'</td>'+'<td>'+str(x.linea)+'</td>'+'<td>'+str(x.columna)+'</td>'+'</tr>'

        contenidoHTML = (
        '<!DOCTYPE html>'
        '<html>' 
        '<head> '
        '<meta charset="utf-8"> '
        '<title>Reporte Tokens</title>'
        '<link href="assets/css/bootstrap-responsive.css" type="text/css" rel="stylesheet">'
        '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" type="text/css" rel="stylesheet">'
        '<link rel="stylesheet" type="text/css"  href="Style.css">'
        '<link rel="stylesheet" type="text/css" href="bootstrap.css">'
        '</head>'
        '<body>'
        '<div class="container-fluid welcome-page" id="home">'
        '<div class="jumbotron">'
        '<h1>'
        '<span>Reporte Errores</span>'
        '</h1>'
        '</div>'
        '</div>')
        
        file = open("./REPORTES/ReporteErrores.html","w")
        file.write(str(contenidoHTML))
        file.write('<h2>'
        '<span>Analisis Realizado</span>'
        '</h2>')

        txtHtml=(
        '<table class="table table-responsive">'
        '<thead>'
        '<tr>'
        '<th scope="col">Descripcion</th>'
        '<th scope="col">Linea</th>'
        '<th scope="col">Columna</th>'
        '</tr>'
        '</thead>'
        '<tbody>')

        for x in errores:
            i += 1
            txtHtml = txtHtml+'<tr>'+'<td>'+str(x.descripcion)+'</td>'+'<td>'+str(x.linea)+'</td>'+'<td>'+str(x.columna)+'</td>'+'</tr>'

        file.write(txtHtml)
        file.write('</tbody>'
        '</table>'
        '</div>'
        '</div>')

        file.write(txtFinal)
        file.close()
