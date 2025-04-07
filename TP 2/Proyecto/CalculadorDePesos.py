import numpy as np

class CalculadorDePesos:
    def __init__(self, matrizDeDecision):
        self.__matrizDeDecision = matrizDeDecision
    
    def setMatriz(self, matrizDeDecision):
        self.__matrizDeDecision = matrizDeDecision
    
    def getMatriz(self):
        return self.__matrizDeDecision
    
    def normalizarMatriz(self):
        col_sums = self.__matrizDeDecision.sum(axis = 0)
        return self.__matrizDeDecision / col_sums
    
    def calcularPesos(self):
        return np.mean(self.normalizarMatriz(), axis = 1)