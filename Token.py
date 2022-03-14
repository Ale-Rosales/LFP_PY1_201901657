class Token:

    def __init__(self, lexema : str, linea : int, columna : str, tipo : str):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo

    def imprimirToken(self):
        print(self.lexema, self.linea, self.columna, self.tipo)