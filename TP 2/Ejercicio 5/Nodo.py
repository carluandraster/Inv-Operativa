class NodoAnalisis:
    def __init__(self, nombre, matriz, hijos=None):
        self._nombre = nombre
        self._matriz = matriz
        if hijos != None:
            self._hijos = hijos
        else:
            self._hijos = []

    def es_hoja(self):
        return len(self.hijos) == 0

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)