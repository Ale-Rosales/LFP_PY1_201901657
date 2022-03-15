from http.client import ImproperConnectionState
import easygui
from Analizador import Analizador

class Gestor:

    def __init__(self) -> None:
        pass

    def rutaArchivo(self):
        ruta = easygui.fileopenbox()
        return ruta

    def CargarData(self):
        data = self.rutaArchivo()
        archivo = open(data, 'r', encoding = "utf-8")
        texto = archivo.read()
        #SIMBOLO TERMINAL
        texto+='\n$'
        archivo.close()
        return texto



        
