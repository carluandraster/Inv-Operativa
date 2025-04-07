import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Proyecto import AnalistaGlobal as AG

criterios = pd.read_csv("Ejercicio 2/criterios.csv").to_numpy()
rendimiento = pd.read_csv("Ejercicio 2/rendimiento.csv").to_numpy()
riesgo = pd.read_csv("Ejercicio 2/riesgo.csv").to_numpy()

analista = AG.AnalistaGlobal(criterios,rendimiento,riesgo)
nombreMatrices = ["criterios", "rendimiento", "riesgo"]
analista.resolver()
pesos = analista.getPesos()
print("b) Prioridad para cada matriz: ")
for nombre, peso in zip(nombreMatrices,pesos):
    print(f"Matriz de {nombre}: {peso}")
print("c) Prioridad global: ",analista.getU())