from tkinter import *
from tkinter import messagebox as MessageBox
from Boton import Boton
from Contenido import Contenido
from Etiqueta import Etiqueta
from Texto import Texto
from Gestor import Gestor
from Analizador import Analizador
import easygui
import os
import webbrowser

gestor = Gestor()
analizar = Analizador()

class Interfaz:
    def __init__(self):
        self.evento = []
        self.Texto = []
        self.Etiqueta = []
        self.Boton = []
        self.Contenido = []

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
        botonUsuario = Button(miFrame, text="Manual\nUsuario", font=("Comic Sans MS", 10),width=12, height=2, command=self.Usuario)
        botonUsuario.place(x=580, y=10)
        botonTecnico = Button(miFrame, text="Manual\nTecnico", font=("Comic Sans MS", 10),width=12, height=2, command=self.Tecnico)
        botonTecnico.place(x=700, y=10)

        raiz.mainloop()

    #----------------------------FUNCIONES DE BOTONES (CARGAR Y ANALIZAR)----------------------------

    def Analizar(self):
        texto = self.analizar.get(1.0, "end-1c")  #->PARA PODER SACAR LA INFORMACION DEL CAMPO
        #texto = self.analizar.insert(1.0, "HOLAAAAAAAAAAA\n")  #->PARA PODER METER EL TEXTO EN EL CAMPO
        #analizar.analizar(texto)
        #analizar.imprimirTokens()
        #analizar.imprimirErrores()
        if len(texto) == 0:
            MessageBox.showwarning("Alerta", "No hay texto para analizar")
        else:
            analizar.analizar2(texto)
            #analizar.imprimirT()
            #analizar.imprimirE()
            self.Data()
            self.Formulario(texto)

    def CargarArchivo(self):
        self.analizar.insert(1.0,gestor.CargarData())

    #----------------------------PRUEBAS PARA CREAR FORMULARIO----------------------------

    def agregarContenido(self, tipo, valor, fondo, valores, evento):
        self.Contenido.append(Contenido(tipo, valor, fondo, valores, evento))

    def agregarContenidoBoton(self, tipo, valor, evento):
        self.Boton.append(Boton(tipo, valor, evento))

    def agregarContenidoTexto(self, tipo, valor, fondo):
        self.Texto.append(Texto(tipo, valor, fondo))

    def agregarContenidoEtiqueta(self, tipo, valor):
        self.Etiqueta.append(Etiqueta(tipo, valor))
    
    def print(self):
        for x in self.Boton:
            print("Tipo: "+x.tipo
            +"\nValor: "+x.valor
            +"\nEvento: "+x.evento)
            print("\n")
    
    def print2(self):
        for y in self.Etiqueta:
            print("Tipo: "+y.tipo
            +"\nValor: "+y.valor)
            print("\n")

    def print3(self):
        for z in self.Texto:
            print("Tipo: "+z.tipo
            +"\nValor: "+z.valor
            +"\nFondo: "+z.fondo)
            print("\n")

    def print4(self):
        for r in self.Contenido:
            print("Tipo: "+r.tipo
            +"\nValor: "+r.valor)
            print("\n")
        
    def print5(self):
        for t in self.evento:
            print(t)
            print("\n")

    def Data(self):
        #self.DataFondo()
        #self.DataTipo()
        #self.RadioSelect()
        #self.DataValor()
        self.ValorData()
        #self.BotonData()
        #self.EtiquetaData()
        self.DataEvento()
 
    # Identificador_tipo(RADIO/SELECT) dosPuntos comillaDoble   HTML   Menos    HTML    comillaDoble ¿Coma?
    #       i                             i+1       i+2         i+3     i+4     i+5         i+6        i+7

    # Identificador_tipo dosPuntos comillaDoble     HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3        i+4     i+5 
    
    # Identificador_fondo dosPuntos comillaDoble    HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3         i+4     i+5

    # Identificador_evento dosPuntos comillaDoble   HTML comillaDoble ¿Coma?
    #       i               i+1         i+2         i+3         i+4     i+5 

    def Prueba(self):
        self.print()
        #self.print2()
        #self.print3()
        self.print4()
        #self.print5()

    def RadioSelect(self):
        tokens = analizar.Tokens
        for i in range(0, len(tokens)):
            if tokens[i].tipo == "Identificador_tipo":
                if tokens[i+4].tipo == "Signo menos":
                    texto = tokens[i+3].lexema+tokens[i+4].lexema+tokens[i+5].lexema
                    self.tipo.append(texto)
                    #print(texto)

    def DataTipo(self):
        tokens = analizar.Tokens
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_tipo":
                if tokens[i+2].tipo == "Comilla doble" and tokens[i+4].tipo == "Comilla doble":
                    texto = tokens[i+3].lexema
                    self.tipo.append(texto)
                #texto = self.obtenerData(tokens[i])
                #self.tipo.append(texto)
                #print(texto)
 
    def DataValor(self):
        tokens = analizar.Tokens
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_valor":
                texto = self.obtenerData(tokens[i+3])
                self.valor.append(texto)
                #print(texto)

    def DataFondo(self):
        tokens = analizar.Tokens
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_fondo":
                texto = self.obtenerData(tokens[i+3])
                self.fondo.append(texto)
                #print(texto)

    def DataEvento(self):
        tokens = analizar.Tokens
        for i in range(0,len(tokens)):
            if tokens[i].tipo == "Identificador_evento":
                if tokens[i+2].tipo == "Comilla doble" and tokens[i+4].tipo == "Comilla doble":
                    texto = tokens[i+3].lexema
                    self.evento.append(texto)

    def ValorData(self):
        tokens = analizar.Tokens
        i = 0
        while tokens[i].tipo != "Corchete izquierdo":
            i+=1
        while tokens[i].tipo != "Corchete derecho":
            i+=1
            while tokens[i].tipo != "Menor que":
                i+=1
            i+=1
            while tokens[i].tipo != "Identificador_tipo":
                i+=1
            i+=1
            while tokens[i].tipo != "Dos puntos":
                i+=1
            i+=1
            while tokens[i].tipo != "Comilla doble":
                i+=1
            i+=1
            tipo = ""
            valores = ""
            evento = ""
            fondo = ""
            while tokens[i].tipo != "Comilla doble":
                tipo = tipo + tokens[i].lexema
                i+=1
            i+=1
            while tokens[i].tipo != "Coma":
                i+=1
            i+=1
            while tokens[i].tipo != "Identificador_valor":
                i+=1
            i+=1
            while tokens[i].tipo != "Dos puntos":
                i+=1
            i+=1
            while tokens[i].tipo != "Comilla doble":
                i+=1
            i+=1
            valor = ""
            while tokens[i].tipo != "Comilla doble":
                valor = valor + tokens[i].lexema
                i+=1
            i+=1
            while tokens[i].tipo != "Mayor que":
                i+=1
            i+=1
            while tokens[i].tipo != "Coma":
                if tokens[i].tipo == "Corchete derecho":
                    self.agregarContenido(tipo, valor, fondo, valores, evento)
                    break
                else:
                    i+=1
            if tokens[i].tipo == "Coma":
                self.agregarContenido(tipo, valor, fondo, valores, evento)
            else:
                pass
        return i

    def BotonData(self):
        tokens = analizar.Tokens
        i = 0
        while tokens[i].tipo != "Corchete izquierdo":
            i+=1
        while tokens[i].tipo != "Corchete derecho":
            i+=1
            while tokens[i].tipo != "Menor que":
                i+=1
            i+=1
            while tokens[i].tipo != "Identificador_tipo":
                i+=1
            i+=1
            while tokens[i].tipo != "Dos puntos":
                i+=1
            i+=1
            while tokens[i].tipo != "Comilla doble":
                i+=1
            i+=1
            tipo = ""
            while tokens[i].tipo != "Comilla doble":
                tipo = tipo + tokens[i].lexema
                i+=1
            i+=1
            if tipo == "boton":
                while tokens[i].tipo != "Coma":
                    i+=1
                i+=1
                while tokens[i].tipo != "Identificador_valor":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                valor = ""
                while tokens[i].tipo != "Comilla doble":
                    valor = valor + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    i+=1
                i+=1
                while tokens[i].tipo != "Identificador_evento":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                evento = ""
                while tokens[i].tipo != "Comilla doble":
                    evento = evento + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Mayor que":
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    if tokens[i].tipo == "Corchete derecho":
                        self.agregarContenidoBoton(tipo, valor, evento)
                        break
                    else:
                        i+=1
                if tokens[i].tipo == "Coma":
                    self.agregarContenidoBoton(tipo, valor, evento)
                else:
                    pass
        return i


    def EtiquetaData(self):
        tokens = analizar.Tokens
        i = 0
        while tokens[i].tipo != "Corchete izquierdo":
            i+=1
        while tokens[i].tipo != "Corchete derecho":
            i+=1
            while tokens[i].tipo != "Menor que":
                i+=1
            i+=1
            while tokens[i].tipo != "Identificador_tipo":
                i+=1
            i+=1
            while tokens[i].tipo != "Dos puntos":
                i+=1
            i+=1
            while tokens[i].tipo != "Comilla doble":
                i+=1
            i+=1
            tipo = ""
            while tokens[i].tipo != "Comilla doble":
                tipo = tipo + tokens[i].lexema
                i+=1
            i+=1
            if tipo == "etiqueta":
                while tokens[i].tipo != "Coma":
                    i+=1
                i+=1
                while tokens[i].tipo != "Identificador_valor":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                valor = ""
                while tokens[i].tipo != "Comilla doble":
                    valor = valor + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Mayor que":
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    if tokens[i].tipo == "Corchete derecho":
                        self.agregarContenidoEtiqueta(tipo, valor)
                        break
                    else:
                        i+=1
                if tokens[i].tipo == "Coma":
                    self.agregarContenidoEtiqueta(tipo, valor)
                else:
                    pass
                #return i
            elif tipo == "boton":
                while tokens[i].tipo != "Identificador_valor":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                valor1 = ""
                while tokens[i].tipo != "Comilla doble":
                    valor1 = valor1 + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    i+=1
                i+=1
                while tokens[i].tipo != "Identificador_evento":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                evento = ""
                while tokens[i].tipo != "Comilla doble":
                    evento = evento + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Mayor que":
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    if tokens[i].tipo == "Corchete derecho":
                        self.agregarContenidoBoton(tipo, valor1, evento)
                        break
                    else:
                        i+=1
                if tokens[i].tipo == "Coma":
                    self.agregarContenidoBoton(tipo, valor1, evento)
                else:
                    pass
                #return i
            elif tipo == "texto":
                while tokens[i].tipo != "Identificador_valor":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                valor2 = ""
                while tokens[i].tipo != "Comilla doble":
                    valor2 = valor2 + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    i+=1
                i+=1
                while tokens[i].tipo != "Identificador_evento":
                    i+=1
                i+=1
                while tokens[i].tipo != "Dos puntos":
                    i+=1
                i+=1
                while tokens[i].tipo != "Comilla doble":
                    i+=1
                i+=1
                fondo = ""
                while tokens[i].tipo != "Comilla doble":
                    fondo = fondo + tokens[i].lexema
                    i+=1
                i+=1
                while tokens[i].tipo != "Mayor que":
                    i+=1
                i+=1
                while tokens[i].tipo != "Coma":
                    if tokens[i].tipo == "Corchete derecho":
                        self.agregarContenidoTexto(tipo, valor2, fondo)
                        break
                    else:
                        i+=1
                if tokens[i].tipo == "Coma":
                    self.agregarContenidoTexto(tipo, valor2, fondo)
                else:
                    pass
        return i

            

    #----------------------------FORMULARIO----------------------------

    def Formulario(self,texto):
        txtFinal = ('</div>'
        '<script src="script.js"></script>'
        '</body>'
        '</html>')

        contenidoHTML = (
        '<!DOCTYPE html>'
        '<html>' 
        '<head> '
        '<meta charset="utf-8"> '
        '<title>Formulario</title>'
        '<link rel="stylesheet" type="text/css"  href="Style.css">'
        '<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" type="text/css" rel="stylesheet">'
        '<link rel="stylesheet" type="text/css" href="bootstrap.css">'
        '</head>'
        '<body>'
        '<div class="container-fluid welcome-page" id="home">'
        '<div class="jumbotron">'
        '<h1>'
        '<span>Formulario</span>'
        '</h1>'
        '</div>'
        '</div>')

        file = open("./REPORTES/Formulario.html","w")
        file.write(str(contenidoHTML))
        #file.write('<h2>'
        #'<span>Formulario del Analisis</span>'
        #'</h2>')

        #-------------------------------LABEL-------------------------------

        for label in self.Contenido:
            if label.tipo == "etiqueta":
                file.write('<br>')
                file.write('<label>'+str(label.valor)+'</label><br>')
                file.write('<br>')
            
        #-------------------------------INPUT-------------------------------

        for input in self.Contenido:
            if input.tipo == "texto":
                file.write('<br>')
                file.write('<input type="text" id="inputF" placeholder="PlaceHolder"></input>')
                file.write('<br>')
        file.write('<br>')
        file.write('<br>')

        #-------------------------------RADIO BUTTONS-------------------------------
        
        for radio in self.Contenido:
            if radio.tipo == "grupo-radio":
                file.write('<br>')
                file.write('<label>'+str(radio.valor)+'</label><br>')
                file.write('<input id="op1" type="radio" name="opciones" value="Opcion1">')
                file.write('<label for="op1">'+str("Opcion1")+'</label><br>')
                file.write('<input id="op2" type="radio" name="opciones" value="Opcion2">')
                file.write('<label for="op2">'+str("Opcion2")+'</label><br>')
                file.write('<input id="op3" type="radio" name="opciones" value="Opcion3">')
                file.write('<label for="op3">'+str("Opcion3")+'</label><br>')
                file.write('<br>')

        file.write('<br>')
        file.write('<br>')

        #-------------------------------SELECT-------------------------------
        
        for select in self.Contenido:
            if select.tipo == "grupo-option":
                file.write('<br>')
                file.write('<label>'+str(select.valor)+'</label><br>')
                file.write('<select name="select" id="seleccion">')
                file.write('<option value="" selected="selected" hidde="hidden">'+str("Escoger opcion")+'</option>')
                file.write('<option value="Select1">'+str("Select1")+'</option>')
                file.write('<option value="Select2">'+str("Select2")+'</option>')
                file.write('<option value="Select3">'+str("Select3")+'</option>')
                file.write('</select>')
                file.write('<br>')

        file.write('<br>')
        file.write('<br>')
        file.write('<br>')

        #-------------------------------BOTON-------------------------------
        # -> info | -> entrada
        for boton in self.Contenido:
            for x in self.evento:
                if boton.tipo == "boton":
                    if x == "info":
                        file.write('<br>')
                        file.write('<button onclick="TomarDatos()">'+str(boton.valor)+'</button>')
                        file.write('<br>')
                    else:
                        file.write('<br>')
                        file.write('<button onclick="Entrada()">'+str(boton.valor)+'</button>')
                        file.write('<br>')
        file.write('<br>')
        file.write('<br>')

        #-------------------------------iFRAME #1-------------------------------
        
        frame = open("./REPORTES/Frame1.html","w")
        frame.write('<!DOCTYPE html>'
        '<html>' 
        '<head> '
        '<meta charset="utf-8"> '
        '<title>Frame</title>'
        '<style>'
        'body {background-color: rgb(245, 245, 245);}'
        '</style>'
        '</head>'
        '<body>')
        frame.write('<center><p>'+texto+'</p></center>')
        frame.write('</body>'
        '</html>')
        frame.close()

        file.write('<div id="frame">')
        #file.write('<iframe src="Frame.html" id="framee" height="200" width="300"></iframe>')
        file.write('</div>')
        file.write('<br>')
        file.write('<br>')
        file.write('<br>')

        #-------------------------------iFRAME #1-------------------------------

        #-------------------------------iFRAME #2-------------------------------
        
        frame = open("./REPORTES/Frame2.html","w")
        frame.write('<!DOCTYPE html>'
        '<html>' 
        '<head> '
        '<meta charset="utf-8"> '
        '<title>Frame</title>'
        '<style>'
        'body {background-color: rgb(245, 245, 245);}'
        '</style>'
        '</head>'
        '<body>')
        frame.write('<div id="contenido">')
        frame.write('</div>')
        frame.write('<script src="frame.js"></script>'
        '</body>'
        '</html>')
        frame.close()

        file.write('<div id="frame">')
        #file.write('<iframe src="Frame.html" id="framee" height="200" width="300"></iframe>')
        file.write('</div>')
        file.write('<br>')
        file.write('<br>')
        file.write('<br>')

        #-------------------------------iFRAME #2-------------------------------

        file.write(txtFinal)
        file.close()
        webbrowser.open("file:///"+os.getcwd()+"/REPORTES/Formulario.html")


    #----------------------------REPORTES----------------------------

    def ReporteTokens(self):
        tokens = analizar.Tokens
        if len(tokens) == 0:
            MessageBox.showwarning("Alerta", "Sin contenido para reporte")
        else:
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
            webbrowser.open("file:///"+os.getcwd()+"/REPORTES/ReporteTokens.html")
    
    def ReporteErrores(self):
        errores = analizar.Errores
        if len(errores) == 0:
            MessageBox.showwarning("Alerta", "Sin contenido para reporte")
        else:
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
            webbrowser.open("file:///"+os.getcwd()+"/REPORTES/ReporteErrores.html")

    #----------------------------DOCUMENTACION----------------------------
    def Usuario(self):
        webbrowser.open("file:///"+os.getcwd()+"/DOCUMENTACION/ManualUsuario.pdf")

    def Tecnico(self):
        webbrowser.open("file:///"+os.getcwd()+"/DOCUMENTACION/ManualTecnico.pdf")
