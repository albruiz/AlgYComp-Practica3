#Alberto Ruiz Andres
#sin(x) + sin(y) + cos(x)*sin(y)

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits import mplot3d
from pylab import *

import random


# Funcion que se encarga de calcular los valores de la funcion matematica
# sin(x) + sin(y) + cos(x)*sin(y) y añadirlos a la matriz
# Parametros: matriz, numFilas, numColumnas
def calculaValores(matrix, n, m):
    
    valorUnitario1 = math.pi/(n-1)
    valorUnitario2 = math.pi/(m-1)
    for i in range(n):
        for j in range(m):
            valorCalculado = math.sin(i*valorUnitario1) + math.sin(i*valorUnitario2) + math.cos(i*valorUnitario1)*math.sin(i*valorUnitario2)
            matrix[i][j]= valorCalculado
    
    return matrix

# Funcion que se encarga de dibujar los puntos de la matriz
# Parametros: matriz, numFilas, numColumnas
def dibujarValores(matrix,n,m):
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
    #He elegido 5 colores para representar los valores en la gráfica colores = "bgrcm"

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
    plot(xColorm,yColorm,'sy')
    ###
    random.seed(a = 1312, version = 2) #seed = 1312, para el seguimiento
    xRandom = random.randint(0, n-1)
    yRandom = random.randint(0, m-1)
    matrizIntermedia = [[-1,-1],[], [xRandom, yRandom]]
    matrizIntermedia = HillClimbing(matrix,n,m,xRandom,yRandom,matrizIntermedia)
    dibujarValores2(matrizIntermedia,n,m)
    show()


# Funcion que se encargara de colorear los puntos que han sido intermedios 
# Parametros: Matriz con los valores intermedios, maximo e inicial, numFilas, numColumnas
def dibujarValores2(matrizSolucion,n,m):
    x = []
    y = []
    for i in range(len(matrizSolucion[1])):
        x.append((matrizSolucion[1][i][0])*math.pi/n-1)
        y.append((matrizSolucion[1][i][1])*math.pi/m-1)
    x = np.array(x)
    y = np.array(y) 
    # posiciones intermedias iran en color negro
    # posicion incial ira en azul
    # posicion máxima ira en rojo  

    plot(x,y,'sk')
    plot((matrizSolucion[2][0])*math.pi/n-1,(matrizSolucion[2][1])*math.pi/m-1, 'sb')
    plot((matrizSolucion[0][0])*math.pi/n-1,(matrizSolucion[0][1])*math.pi/m-1, 'sr')
    #show()



# Funcion HillClimbing que de manera voraz encuentra el maximo valor
# dentro de la matriz de valores.
# Parametros: matriz, numFilas, numColumnas, coordX del pivote, coordY del pivote,
# matriz que almacena los puntos por los que pasa
def HillClimbing(matrix, n, m, posicionX, posicionY, matrizIntermedia):
    posiciones = [[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    pivote = matrix[posicionX][posicionY]
    primero, segundo, tercero, cuarto = -1,-1,-1,-1
    if posicionX == 0:
        if posicionY == 0:
            primero = matrix[posicionX + 1][posicionY]
            segundo = matrix[posicionX][posicionY + 1]
            posiciones[0] = [posicionX + 1, posicionY]
            posiciones[1] = [posicionX, posicionY + 1]

        elif posicionY != (m-1):
            primero = matrix[posicionX][posicionY - 1]
            segundo = matrix[posicionX][posicionY + 1]
            tercero = matrix[posicionX + 1][posicionY]
            posiciones[0] = [posicionX, posicionY - 1]
            posiciones[1] = [posicionX, posicionY + 1]
            posiciones[2] = [posicionX + 1, posicionY]

        else:
            primero = matrix[posicionX + 1][posicionY]
            segundo = matrix[posicionX][posicionY - 1]
            posiciones[0] = [posicionX + 1, posicionY]
            posiciones[1] = [posicionX, posicionY - 1]

    elif posicionX != (n - 1):
        if posicionY == 0:
            primero = matrix[posicionX - 1][posicionY]
            segundo = matrix[posicionX + 1][posicionY]
            tercero = matrix[posicionX][posicionY + 1]
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX + 1, posicionY]
            posiciones[2] = [posicionX, posicionY + 1]

        elif posicionY != (m-1):
            primero = matrix[posicionX - 1][posicionY]
            segundo = matrix[posicionX + 1][posicionY] 
            tercero = matrix[posicionX][posicionY + 1] 
            cuarto = matrix[posicionX][posicionY - 1]
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX + 1, posicionY]
            posiciones[2] = [posicionX, posicionY + 1]
            posiciones[3] = [posicionX, posicionY - 1]

        else:
            primero = matrix[posicionX - 1][posicionY]
            segundo = matrix[posicionX + 1][posicionY]
            tercero = matrix[posicionX][posicionY - 1]
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX + 1, posicionY]
            posiciones[2] = [posicionX, posicionY - 1]
    
    else:
        if posicionY == 0:
            primero = matrix[posicionX - 1][posicionY]
            segundo = matrix[posicionX][posicionY + 1]
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX, posicionY + 1]

        elif posicionY != (m-1):
            primero = matrix[posicionX][posicionY - 1]
            segundo = matrix[posicionX][posicionY + 1]
            tercero = matrix[posicionX - 1][posicionY]
            posiciones[0] = [posicionX, posicionY - 1]
            posiciones[1] = [posicionX, posicionY + 1]
            posiciones[2] = [posicionX - 1, posicionY]

        else:
            primero = matrix[posicionX - 1][posicionY]
            segundo = matrix[posicionX][posicionY - 1]
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX, posicionY - 1] 

    #almacenamos en la matrizIntermedia, los valores de los valores que ha ido comparando
    for i in posiciones:
        if i[0] != -1:
            if i not in matrizIntermedia[1]:
                matrizIntermedia[1].append(i)
            else: pass
        else: pass

    if pivote >= primero and pivote >= segundo and pivote >= tercero and pivote >= cuarto:
        matrizIntermedia[0]=[posicionX, posicionY]
        return matrizIntermedia
    else:
        if pivote < primero:
            resultado = HillClimbing(matrix, n, m, posiciones[0][0],posiciones[0][1],matrizIntermedia)
            return resultado
        elif pivote < segundo:
            resultado = HillClimbing(matrix, n, m, posiciones[1][0],posiciones[1][1],matrizIntermedia)
            return resultado
        elif pivote < tercero:
            resultado = HillClimbing(matrix, n, m, posiciones[2][0],posiciones[2][1],matrizIntermedia)
            return resultado
        else:
            resultado = HillClimbing(matrix, n, m, posiciones[3][0],posiciones[3][1],matrizIntermedia)
            return resultado



            


#main
n = int(input("introduce n: "))
m = int(input("introduce m: "))
while n <= 1 or m <= 1:
    n = int(input("introduce n: "))
    m = int(input("introduce m: "))
matrix = np.zeros((n, m))
matrix = calculaValores(matrix,n,m)
dibujarValores(matrix,n,m)



random.seed(a = 1312, version = 2) #seed = 1312, para el seguimiento
xRandom = random.randint(0, n-1)
yRandom = random.randint(0, m-1)
matrizIntermedia = [[-1,-1],[], [xRandom, yRandom]]
matrizIntermedia = HillClimbing(matrix,n,m,xRandom,yRandom,matrizIntermedia)

dibujarValores2(matrizIntermedia,n,m)

'''
matrizPrueba = [[1,2,3,4],[2,3,4,5],[2,3,4,5],[5,6,7,8]]
random.seed(a = 1312, version = 2) #seed = 1312, para el seguimiento
xRandom = random.randint(0, 4-1)
yRandom = random.randint(0, 4-1)
valorMaximo = HillClimbing(matrizPrueba,4,4,xRandom,yRandom)
print(valorMaximo)

sddsadasdas
for i in range(n):
    for j in range(m):
        print(round(matrix[i][j], 10),"\t",end="")
    print("\n")

'''


