import pandas as pd

def rango(num: float, fr_acumuladas):
    i = 0
    while(num>=fr_acumuladas[i+1]):
        i+=1
    return i

def simular(valores,vec_p, n: int, fr_acumuladas):
    for i in range(n):
        print(valores[rango(vec_p[i], fr_acumuladas)])

str_nombre_archivo = "Ejercicio 3/ejercicio3.xlsx";
df1 = pd.read_excel(str_nombre_archivo, sheet_name="Hoja1")
df2 = pd.read_excel(str_nombre_archivo, sheet_name="Números aleatorios")

valores = df1.iloc[0].index[1:13]
fr_acumuladas = df1.iloc[2].values[1:13]

mejor_tirada = df2["La mejor tirada"]

simular(valores,mejor_tirada, 30, fr_acumuladas)