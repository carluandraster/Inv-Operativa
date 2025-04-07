import numpy as np
from .CalculadorDePesos import CalculadorDePesos
from .EstimadorConsistencia import EstimadorConsistencia

class AnalistaGlobal:
    def __init__(self, *matrices):
        self.__matrices = list(matrices)
        self.__pesos = list()
    
    def resolver(self):
        self.__CalculadorDePesos = CalculadorDePesos(self.__matrices[0])
        self.__w = self.__CalculadorDePesos.calcularPesos()
        self.__pesos.append(self.__w)
        self.__r = np.empty((np.size(self.__matrices[1],1),0))
        self.__EstimadorConsistencia = EstimadorConsistencia(self.__matrices[0], self.__w)
        self.__RCs = [self.__EstimadorConsistencia.getRC()]
        for i, matriz in enumerate(self.__matrices[1:], start=1):
            self.__CalculadorDePesos.setMatriz(matriz)
            self.__EstimadorConsistencia.setMatriz(matriz)
            columna_nueva = self.__CalculadorDePesos.calcularPesos()
            self.__pesos.append(columna_nueva)
            self.__EstimadorConsistencia.setPesos(columna_nueva)
            columna_nueva = columna_nueva.reshape(-1,1)
            self.__r = np.hstack((self.__r,columna_nueva))
            self.__RCs.append(self.__EstimadorConsistencia.getRC())
        self.__U = np.dot(self.__r,self.__w)
    
    def getPesos(self):
        return self.__pesos

    def getU(self):
        return self.__U
    
    def getRCs(self):
        return self.__RCs
    
    def __repr__(self):
        return f'''Relaciones de consistencia: {self.__RCs}
    Evaluación global: {self.__U}'''