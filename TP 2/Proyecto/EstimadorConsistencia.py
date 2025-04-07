import numpy as np

class ErrorValor(Exception):
	def __init__(self,err):
		print(f'ERROR: {err}')


class EstimadorConsistencia:
    def __init__(self, matriz, pesos):
        self.__A = matriz
        self.__W = pesos
        self.__n = np.size(self.__W)
    
    def setMatriz(self, matrizDeDecision):
        self.__A = matrizDeDecision
    
    def setPesos(self, pesos):
        self.__W = pesos
        self.__n =  np.size(self.__W)
    
    def getLambdaMax(self):
        aw = np.dot(self.__A,self.__W)
        return np.mean(aw/self.__W)
    
    def getIC(self):
        return (self.getLambdaMax()-self.__n)/(self.__n - 1)
    
    def getIA(self):
        match self.__n:
            case 2:
                resultado = 0
            case 3:
                resultado = 0.58
            case 4:
                resultado = 0.9
            case 5:
                resultado = 1.12
            case 6:
                resultado = 1.24
            case 7:
                resultado = 1.32
            case 8:
                resultado = 1.41
            case 9:
                resultado = 1.45
            case 10:
                resultado = 1.49
            case _:
                raise ErrorValor("El valor ingresado no fue encontrado en la tabla proporcionada por la teoria")
        return resultado
    
    def getRC(self):
        ia = self.getIA()
        if (ia == 0):
            return -1
        else:
            return self.getIC()/ia