import pandas as pd

def rango(num: float, col_inf):
    i = 0
    while(num>=col_inf[i+1]):
        i+=1
    return i

def simular(vec_p, n: int, col_inf):
    for i in range(n):
        print(rango(vec_p[i], col_inf))


# Main
df = pd.read_excel("Ejercicio 2/ejercicio2.xlsx")

vecf_mejor_tirada = df[0:50]["La mejor tirada"]

col_linf = df[1:8]["DATOS ESPERADOS"]
col_linf = col_linf.to_numpy()
col_linf[6] = 1

simular(vecf_mejor_tirada, 10, col_linf)