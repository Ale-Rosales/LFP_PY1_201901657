from lib2to3.pgen2.tokenize import TokenError
from linecache import clearcache
from turtle import Turtle
from xmlrpc.client import FastMarshaller
from pyparsing import col, line
from soupsieve import select
from Token import Token
from Error import Error
from prettytable import PrettyTable

class Analizador:

    def __init__(self):
        self.Tokens = []
        self.Errores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0
    
    def agregarToken(self,caracter, linea, columna, token):
        self.Tokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''
    
    def agregarError(self,caracter, linea, columna):
        self.Errores.append(Error('Caracter ' + caracter + ' no reconocido.', linea, columna))

    #---------------------OTRA PRUEBA DE ANALIZAR (ESTA PARECE LEER BIEN)---------------------
    def S0(self, caracter : str):
        "Estado Q0"
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        #elif caracter.isdigit():
            #self.estado = 2
            #self.buffer += caracter
            #self.columna += 1
        elif caracter == '~':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == '[':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == ':':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        elif caracter == '"':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == ',':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        elif caracter == "'":
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        elif caracter ==']':
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna = 0
        elif caracter in ['\t',' ']:
            self.columna +=1
        elif caracter == '$':
            print("Fin del analisis")
        else:
            self.agregarError(caracter,self.linea,self.columna)

    def S1(self, caracter : str):
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        else:
            if self.buffer in ['formulario', ]:
                self.agregarToken(self.buffer, self.linea, self.columna, 'Reservada_'+self.buffer)
                self.estado = 0
                self.i -= 1
            elif self.buffer in ['tipo', 'valor', 'fondo', 'valores', 'evento']:
                self.agregarToken(self.buffer, self.linea, self.columna, 'Identificador_'+self.buffer)
                self.estado = 0
                self.i -= 1
            else:
                self.agregarToken(self.buffer, self.linea, self.columna, 'Contenido_HTML')
                self.estado = 0
                self.i -= 1

    """def S2(self, caracter : str):
        if caracter.isdigit():
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregarToken(self.buffer, self.linea, self.columna, 'Numero')
            self.estado = 0
            self.i -= 1"""

    def S2(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Signo raro')
        self.estado = 0
        self.i -= 1

    def S3(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Mayor que')
        self.estado = 0
        self.i -= 1

    def S4(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Corchete izquierdo')
        self.estado = 0
        self.i -= 1

    def S5(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Menor que')
        self.estado = 0
        self.i -= 1

    def S6(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Dos puntos')
        self.estado = 0
        self.i -= 1

    def S7(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Comilla doble')
        self.estado = 0
        self.i -= 1

    def S8(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Coma')
        self.estado = 0
        self.i -= 1

    def S9(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Comilla simple')
        self.estado = 0
        self.i -= 1

    def S10(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Corchete derecho')
        self.estado = 0
        self.i -= 1
    
    def S11(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Signo menos')
        self.estado = 0
        self.i -= 1

    def analizar(self,cadena):
        self.Errores = []
        self.Tokens = []
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.S0(cadena[self.i])
            elif self.estado == 1:
                self.S1(cadena[self.i])
            elif self.estado == 2:
                self.S2(cadena[self.i])
            elif self.estado == 3:
                self.S3(cadena[self.i])
            elif self.estado == 4:
                self.S4(cadena[self.i])
            elif self.estado == 5:
                self.S5(cadena[self.i])
            elif self.estado == 6:
                self.S6(cadena[self.i])
            elif self.estado == 7:
                self.S7(cadena[self.i])
            elif self.estado == 8:
                self.S8(cadena[self.i])
            elif self.estado == 9:
                self.S9(cadena[self.i])
            elif self.estado == 10:
                self.S10(cadena[self.i])
            elif self.estado == 11:
                self.S11(cadena[self.i])
            self.i += 1
            
    def imprimirT(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.Tokens:
            x.add_row([token.lexema, token.linea, token.columna, token.tipo])
        print(x)

    def imprimirE(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion","linea","columna"]
        for error_ in self.Errores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)  
            
            
            


    