class Contador:
    def __init__(self, valorLimite, valorInicial=0, valorIncremento=1):
        self.contador = valorInicial
        self.__valorInicial = valorInicial
        self.__valorIncremento = valorIncremento
        self.__valorLimite = valorLimite

    def getValorInicial(self):
        return self.__valorInicial
    
    def getValorIncremento(self):
        return self.__valorIncremento
    
    def getValorLimite(self):
        return self.__valorLimite