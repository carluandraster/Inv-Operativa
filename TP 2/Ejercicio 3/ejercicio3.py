import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Proyecto import AnalistaGlobal as AG

criterios = pd.read_csv("Ejercicio 3/criterios.csv").to_numpy()
precio = pd.read_csv("Ejercicio 3/precio.csv").to_numpy()
calidad = pd.read_csv("Ejercicio 3/calidad.csv").to_numpy()
costo_de_mantenimiento = pd.read_csv("Ejercicio 3/costo_mantenimiento.csv").to_numpy()

analista = AG.AnalistaGlobal(criterios,precio,calidad,costo_de_mantenimiento)
analista.resolver()
print("Prioridad global: ",analista.getU())
print("Relaciones de consistencia: ",[float(x) for x in analista.getRCs()])