from lib2to3.pgen2.tokenize import TokenError
from linecache import clearcache
from turtle import Turtle
from xmlrpc.client import FastMarshaller
from pyparsing import col, line
from soupsieve import select
from Token import Token
from Error import Error
from Tokens import Tokens
from Errores import Errores
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
        self.listaTokens=[]
        self.listaErrores=[]
    
    def agregarToken(self,caracter, linea, columna, token):
        self.Tokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''
    
    def agregarError(self,caracter, linea, columna):
        self.Errores.append(Error('Caracter ' + caracter + ' no reconocido.', linea, columna))

    def isLetter(self,caracter):
        if(ord(caracter) >= 65 and ord(caracter) <= 90
        or (ord(caracter)) >= 97 and ord(caracter) <= 122
        or ord(caracter) == 164 or ord(caracter) == 165):
            return True
        else:
            return False
        
    def isNum(self,caracter):
        if ((ord(caracter) >= 48 and ord(caracter) <= 57)):
            return True
        else:
            return False

    def isCharacter(self,caracter):
        if ((ord(caracter) >= 32 and ord(caracter) != 34)):
            return True
        elif (160 <= ord(caracter) <= 165 or ord(caracter) == 129 or ord(caracter == 130)):
            return True
        elif ord(caracter) == 34:
            return False

    #---------------------PRUEBA DE USO---------------------
    def analizar(self, texto):
        self.listaTokens=[]
        self.listaErrores=[]
        estado = 0
        fila = 1
        columna = 1
        lexema = ''
        i = 0
        while i < len(texto):
            x = texto[i]
            if estado == 0:
                if x == '~':
                    self.listaTokens.append(Tokens("~", "Signo raro", fila, columna))
                    columna+=1
                elif x == '>':
                    self.listaTokens.append(Tokens(">","Mayor que",fila,columna))
                    columna+=1
                elif x == '[':
                    self.listaTokens.append(Tokens("[","Corchete Izquierda",fila,columna))
                    columna+=1
                elif x == ']':
                    self.listaTokens.append(Tokens("]","Corchete derecho",fila,columna))
                    columna+=1
                elif x == '<':
                    self.listaTokens.append(Tokens("<","Menor que",fila,columna))
                    columna+=1
                elif x == ':':
                    self.listaTokens.append(Tokens(":","Dos puntos",fila,columna))
                    columna+=1
                elif x == ',':
                    self.listaTokens.append(Tokens(",","Coma",fila,columna))
                    columna+=1
                elif x == '"':
                    self.listaTokens.append(Tokens('"',"Comilla Doble",fila,columna))
                    columna+=1
                elif x == "'":
                    self.listaTokens.append(Tokens("'","Comilla Simple",fila,columna))
                    columna+=1
                elif x == '\n':
                    fila+=1
                    columna+=1
                elif self.isNum(x) == True:
                    lexema+=x
                    columna+=1
                    estado = 9 #VERIFICAR COMO IRIAN LOS ESTADOS
                elif self.isLetter(x) == True:
                    lexema+=x
                    columna+=1
                    estado = 11 #VERIFICAR COMO IRIAN LOS ESTADOS
                elif x == '$':
                    self.listaTokens.append(Tokens('$',"Fin Cadena",fila,columna))
                    print("Fin del analisis")
                else:
                    e = "Error lexico en fila "+str(fila)+" y columna "+str(columna)
                    self.listaErrores.append(Errores(fila,columna,e, "Simbolo, letra o digito"))
        
            #TERMINA LO FEO
            #EMPIEZA LO MAS FEO
            elif estado == 1:
                if x == '\n':
                    fila += 1
                    columna = 1
                    estado = 0
                else:
                    pass
            elif estado == 2:
                if x == "'":
                    columna+=1
                    estado = 3
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9:
                    pass
                elif x == '\n':
                    fila+=1
                    columna=1
            elif estado == 3:
                if x == "'":
                    self.listaTokens.append(Tokens("'''", 'Comilla Simple',fila,columna))
                    columna+=1
                    estado=4
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9:
                    pass
                elif x == '\n':
                    fila+=1
                    columna=1
                else:
                    e = "Error lexico en fila "+str(fila)+" y columna "+str(columna)
                    self.listaErrores.append(Errores(fila,columna,e, "Simbolo, letra o digito"))
            elif estado == 4:
                if x == "'":
                    columna += 1
                    estado = 5
                elif x == '\n':
                    fila+=1
                    columna=1
                else:
                    pass
            elif estado == 5:
                if x == "'":
                    columna+=1
                    estado = 6
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9:
                    pass
                elif x=='\n':
                    fila+=1
                    columna=1
            elif estado == 6:
                if x == "'":
                    self.listaTokens.append(Token("'''", 'ComillaSimple',fila,columna))
                    columna+=1
                    estado=0
                elif ord(x) == 32 or ord(x) == 10 or ord(x) == 9:
                    pass
                elif x=='\n':
                    fila+=1
                    columna=1
            elif estado == 7:
                if self.isCharacter(x)==True:
                    lexema+=x
                    columna+=1
                    estado = 8
                elif x=='"':
                    lexema=''
                    columna+=1
                    i-=1
                    estado=8
                else:
                    e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar"
                    self.listaErrores.append(Errores(fila, columna, e, "caracter o cadena vacía"))
            elif estado==8:
                if self.isCharacter(x)==True:
                    lexema+=x
                    columna+=1
                elif x=='"':
                    self.listaTokens.append(Token('cadena',lexema,fila,columna))
                    lexema=''
                    self.listaTokens.append(Token('"', 'ComillaDoble',fila,columna))
                    columna+=1
                    estado=0
                else:
                    e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar"
                    self.listaErrores.append(Errores(fila, columna, e, 'caracter o " '))
            elif estado==9:
                if self.isNum(x)==True:
                    lexema+=x
                    columna+=1
                elif x == '.':
                    lexema+=x
                    estado=10
                    columna+=1
                else: 
                    self.listaTokens.append(Token('entero',lexema ,fila,columna))
                    lexema=''
                    i-=1
                    estado=0
            elif estado==10:
                if self.isNum(x)==True:
                    lexema+=x
                    columna+=1
                else:
                    self.listaTokens.append(Token('real',lexema,fila, columna))
                    lexema=''
                    estado=0
                    i-=1
            elif estado == 11:
                if self.isLetter(x)==True:
                    lexema+=x
                else:
                    if lexema == 'formulario':
                        self.listaTokens.append(Tokens(lexema,'palabra reservada',fila,columna))
                    if lexema == 'tipo':
                        self.listaTokens.append(Tokens(lexema,'tipo',fila,columna))
                    elif lexema == 'valor':
                        self.listaTokens.append(Tokens(lexema,'valor',fila,columna))
                    elif lexema == 'fondo':
                        self.listaTokens.append(Tokens(lexema,'fondo',fila,columna))
                    elif lexema == 'valores':
                        self.listaTokens.append(Tokens(lexema,'valores',fila,columna))
                    elif lexema == 'evento':
                        self.listaTokens.append(Tokens(lexema,'evento',fila,columna))
                    else:
                        e='Error lexico en fila '+str(fila)+' y columna '+str(columna)+" revisar comando"
                        self.listaErrores.append(Errores(fila, columna, e, "Comando"))
                    lexema=''
                    i-=1
                    estado=0
            i+=1
        return self.listaTokens
                
    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Token","Lexema","Fila","Columna"]
        for token in self.listaTokens:
            x.add_row([token.token, token.lexema, token.fila,token.columna])
        print(x)

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Fila","Columna","Descripcion"]
        for error_ in self.listaErrores:
            x.add_row([error_.fila, error_.columna, error_.descripcion])
        print(x)
    
    #---------------------OTRA PRUEBA DE ANALIZAR---------------------
    def S0(self, caracter : str):
        "Estado Q0"
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '~':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter == '[':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        elif caracter == ':':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == '"':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        elif caracter == ',':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        elif caracter == "'":
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        elif caracter ==']':
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 12
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
                self.agregarToken(self.buffer, self.linea, self.columna, 'Para HTML')
                self.estado = 0
                self.i -= 1

    def S2(self, caracter : str):
        if caracter.isdigit():
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregarToken(self.buffer, self.linea, self.columna, 'Numero')
            self.estado = 0
            self.i -= 1

    def S3(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Signo raro')
        self.estado = 0
        self.i -= 1

    def S4(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Mayor que')
        self.estado = 0
        self.i -= 1

    def S5(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Corchete izquierdo')
        self.estado = 0
        self.i -= 1

    def S6(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Menor que')
        self.estado = 0
        self.i -= 1

    def S7(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Dos puntos')
        self.estado = 0
        self.i -= 1

    def S8(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Comilla doble')
        self.estado = 0
        self.i -= 1

    def S9(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Coma')
        self.estado = 0
        self.i -= 1

    def S10(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Comilla simple')
        self.estado = 0
        self.i -= 1

    def S11(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Corchete derecho')
        self.estado = 0
        self.i -= 1
    
    def S12(self, caracter : str):
        self.agregarToken(self.buffer, self.linea, self.columna, 'Signo menos')
        self.estado = 0
        self.i -= 1

    def analizar2(self,cadena):
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
            elif self.estado == 12:
                self.S12(cadena[self.i])
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
            
            
            


    