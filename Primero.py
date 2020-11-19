#Primer Intento ejercicio Voraz
#Alberto Ruiz Andres
#sin(x) + sin(y) + cos(x)*sin(y)

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits import mplot3d
from pylab import *


def calculaValores(matrix, n, m):
    
    valorUnitario1 = math.pi/(n-1)
    valorUnitario2 = math.pi/(m-1)
    for i in range(n):
        for j in range(m):
            valorCalculado = math.sin(i*valorUnitario1) + math.sin(i*valorUnitario2) + math.cos(i*valorUnitario1)*math.sin(i*valorUnitario2)
            matrix[i][j]= valorCalculado
    
    return matrix

def nosPitnamosUnas(matrix,n,m):
    x = []
    y = []
    z = []
    for i in range(n):
        for j in range(m):
            x.append(i*math.pi/(n-1))
            y.append(j*math.pi/(n-1))
            z.append(matrix[i][j])
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    valorMaximo = np.amax(z)
    valorMinimo = np.amin(z)
    valorLimitador = (valorMaximo - valorMinimo)/5
    #He elegido 5 colores para representar los valores en la gráfica
    colores = "bgrcm"
    nuevoz = []
    xColorb, yColorb, xColorg, yColorg, xColorr, yColorr, xColorc, yColorc, xColorm, yColorm = [],[],[],[],[],[],[],[],[],[]

    for i in range(z.size):
        valorsito = (int) (z[i]/valorLimitador)
        if valorsito == 0:
            xColorb.append(x[i])
            yColorb.append(y[i])
        elif valorsito == 1:
            xColorg.append(x[i])
            yColorg.append(y[i])
        elif valorsito == 2:
            xColorr.append(x[i])
            yColorr.append(y[i])
        elif valorsito == 3:
            xColorc.append(x[i])
            yColorc.append(y[i])
        elif valorsito == 4 or valorsito == 5:
            xColorm.append(x[i])
            yColorm.append(y[i])

    plot(xColorb,yColorb,'sb')
    plot(xColorg,yColorg,'sg')
    plot(xColorr,yColorr,'sr')
    plot(xColorc,yColorc,'sc')
    plot(xColorm,yColorm,'sm')
    show()





n = int(input("introduce n: "))
m = int(input("introduce m: "))
while n <= 1 or m <= 1:
    n = int(input("introduce n: "))
    m = int(input("introduce m: "))
matrix = np.zeros((n, m))
matrix = calculaValores(matrix,n,m)
nosPitnamosUnas(matrix,n,m)

"""
sddsadasdas
for i in range(n):
    for j in range(m):
        print(round(matrix[i][j], 10),"\t",end="")
    print("\n")

"""


