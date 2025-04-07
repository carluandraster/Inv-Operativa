import sys
import os
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Proyecto import AnalistaGlobal as AG
from Proyecto import CalculadorDePesos as CP
import Nodo as nd

class AnalistaConSubcriterios(AG.AnalistaGlobal):
    def __init__(self, arbol_de_matrices: nd.NodoAnalisis):
        self.__matrices = arbol_de_matrices
    
    def recorrer_nodo(self, nodo: nd.NodoAnalisis):
        analista = AG.AnalistaGlobal(nodo._matriz, nodo._hijos)
        analista.resolver()
        return analista.getPesos
    
    def resolver(self):
        self.__r = np.empty((np.size(self.__matrices._hijos[0]._matriz,1),0))
        for hijo in self.__matrices._hijos:
            self.__r = np.hstack((self.__r,self.recorrer_nodo(hijo)))
        calculador = CP.CalculadorDePesos(self.__matrices._matriz)
        self.__w = calculador.calcularPesos()
        return np.dot(self.__r,self.__w)