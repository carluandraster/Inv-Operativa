import sys
import os
import pandas as pd

# Agregás la ruta al directorio "TP 2"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Ahora podés importar el paquete Proyecto
from Proyecto import CalculadorDePesos as CP
from Proyecto import EstimadorConsistencia as EC

df = pd.read_csv("Ejercicio 1/Ejercicio 1 2.0/matriz.csv")
matriz = df.to_numpy()
calc_pesos = CP.CalculadorDePesos(matriz)
pesos = calc_pesos.calcularPesos()
print("Pesos: ",pesos)

est_cons = EC.EstimadorConsistencia(matriz,pesos)
rc = est_cons.getRC()
print("Relacion de consistencia: ",rc)
if (rc<=0.1):
    print("La matriz considerada no presenta inconsistencias serias")