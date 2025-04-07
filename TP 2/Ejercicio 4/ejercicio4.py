import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Proyecto import AnalistaGlobal as AG

criterios = pd.read_csv("Ejercicio 4/criterios.csv").to_numpy()
costo = pd.read_csv("Ejercicio 4/costo.csv").to_numpy()
herramientas = pd.read_csv("Ejercicio 4/herramientas.csv").to_numpy()
personalizacion = pd.read_csv("Ejercicio 4/personalizacion.csv").to_numpy()
soporte = pd.read_csv("Ejercicio 4/soporte.csv").to_numpy()

analista = AG.AnalistaGlobal(criterios, costo, herramientas, personalizacion, soporte)
analista.resolver()
print("Relaciones de consistencia: ")
inconsistencias = False
for RC in analista.getRCs():
    print(RC)
    if (RC > 0.1):
        inconsistencias = True
if (inconsistencias):
    print("Se encontraron inconsistencias")
else:
    print("No se encontraron inconsistencias")
print(analista.getU())