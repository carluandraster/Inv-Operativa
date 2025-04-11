import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from Proyecto import CalculadorDePesos as CP;

def imprimirPesos(archivo):
    matriz = pd.read_csv(f"Ejercicio 5/{archivo}.csv").to_numpy()
    calculador = CP.CalculadorDePesos(matriz)
    print(calculador.calcularPesos())       

archivos = ["criterios", "entrega", "calidad", "fecha", "cantidad", "conformidad", "funcionalidad"]
for archivo in archivos:
    imprimirPesos(archivo)