'''
Alberto Ruiz Andres

h(x,y) = x/(x*x+1) - y/(y*y+1) + 2*(sqrt(x*x+y*y)-1)/((sqrt(x*x+y*y)-1)*(sqrt(x*x+y*y)-1)+1)   Rango [-6:6][-6:6]

'''


import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits import mplot3d
from pylab import *
from time import time


import random


# Funcion que se encarga de calcular los valores de la funcion matematica y añadirlos a la matriz
# Parametros: matriz, numFilas, numColumnas, indexFormula
def calculaValores(matrix, n, m):
    
    valorUnitarioFilas = 12/n
    valorUnitarioColumnas = 12/m

    #h(x,y) = x/(x*x+1) - y/(y*y+1) +2*(sqrt(x*x+y*y)-1)/((sqrt(x*x+y*y)-1)*(sqrt(x*x+y*y)-1)+1)   Rango [-6:6][-6:6]


    for i in range(n):
        for j in range(m):
            valorCalculado = ((((i*valorUnitarioFilas) -6 )) / (((i*valorUnitarioFilas) -6 )**2 + 1)) - ((((j*valorUnitarioFilas) -6 )) / (((j*valorUnitarioFilas) -6 )**2 + 1)) + (2*((math.sqrt(((i*valorUnitarioFilas) -6 )**2) + ((j*valorUnitarioFilas) -6 )**2) -1))/ ((math.sqrt((math.sqrt(((i*valorUnitarioFilas) -6 )**2) + ((j*valorUnitarioFilas) -6 )**2))-1)**2 +1 )
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
            x.append((i*12/n) -6 )
            y.append((j*12/m) -1 )
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

    HillClimbingModificada(matrix,n,m)



# Funcion que se encargara de colorear los puntos que han sido intermedios 
# Parametros: Matriz con los valores intermedios, maximo e inicial, numFilas, numColumnas
def dibujarValores2(matrizSolucion,n,m):
    x = []
    y = []
    for i in range(len(matrizSolucion[1])):
        x.append(((matrizSolucion[1][i][0])*12/n)-6) 
        y.append(((matrizSolucion[1][i][1])*12/m)-6) 
    x = np.array(x)
    y = np.array(y) 
    # posiciones intermedias iran en color negro
    # posicion incial ira en azul
    # posicion máxima ira en rojo  

    plot(x,y,'sk')
    plot(((matrizSolucion[2][0])*12/n)-6 ,((matrizSolucion[2][1])*12/m)-6, 'sb')
    plot(((matrizSolucion[0][0])*12/n)-6 ,((matrizSolucion[0][1])*12/m)-6, 'sr')
    #show()

# Funcion que realiza la llamada a HillClimbing tantas veces como puntos
# se hayan generado, el numero de puntos P, se genera de manera aleatoria
# siguiendo la semilla determinada P será siempre un valor entre [0, n/2]
# por decision del programador
def HillClimbingModificada(matrix,n,m):
    random.seed(a = 1312, version = 2) #seed = 1312, para el seguimiento
    #P = random.randint(0, n/2)
    #P = 700
    #P = 1000
    #P = 850
    #P = 820
    #P = 250
    #P = 300
    #P = 275
    #P = 900
    P =925

    print (P)
    for i in range(P):
        random.seed(a = i, version = 2)
        xRandom = random.randint(0, n-1)
        yRandom = random.randint(0, m-1)
        matrizIntermedia = [[-1,-1],[], [xRandom, yRandom]]
        matrizIntermedia = HillClimbing(matrix,n,m,xRandom,yRandom,matrizIntermedia)
        #dibujarValores2(matrizIntermedia,n,m)
    #show()
    
# Funcion Nueva para calcular el valor que introduzcan
def calculamelo(posicionX, posicionY):
    valorCalculado = ((((posicionX*12/n) -6 )) / (((posicionX*12/n) -6 )**2 + 1)) - ((((posicionY*12/n) -6 )) / (((posicionY*12/n) -6 )**2 + 1)) + (2*((math.sqrt(((posicionX*12/n) -6 )**2) + ((posicionY*12/n) -6 )**2) -1))/ ((math.sqrt((math.sqrt(((posicionX*12/n) -6 )**2) + ((posicionY*12/n) -6 )**2))-1)**2 +1 )
    return valorCalculado

# Funcion HillClimbing que de manera voraz encuentra el maximo valor 
# dentro de la matriz de valores.
# Parametros: matriz, numFilas, numColumnas, coordX del pivote, coordY del pivote,
# matriz que almacena los puntos por los que pasa
def HillClimbing(matrix, n, m, posicionX, posicionY, matrizIntermedia):
    posiciones = [[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    pivote = calculamelo(posicionX,posicionY)
    primero, segundo, tercero, cuarto = -1,-1,-1,-1

    if posicionX == 0:
        if posicionY == 0:
            primero = calculamelo(posicionX + 1,posicionY)
            segundo = calculamelo(posicionX,posicionY + 1)
            matrix[posicionX + 1][posicionY] = primero
            matrix[posicionX][posicionY + 1] = segundo
            posiciones[0] = [posicionX + 1, posicionY]
            posiciones[1] = [posicionX, posicionY + 1]

        elif posicionY != (m-1):
            primero = calculamelo(posicionX,posicionY - 1)
            segundo = calculamelo(posicionX,posicionY + 1)
            tercero = calculamelo(posicionX + 1,posicionY)
            matrix[posicionX][posicionY - 1] = primero
            matrix[posicionX][posicionY + 1] = segundo
            atrix[posicionX + 1][posicionY] = tercero
            posiciones[0] = [posicionX, posicionY - 1]
            posiciones[1] = [posicionX, posicionY + 1]
            posiciones[2] = [posicionX + 1, posicionY]

        else:
            primero = calculamelo(posicionX + 1,posicionY)
            segundo = calculamelo(posicionX,posicionY - 1)
            matrix[posicionX + 1][posicionY] = primero
            matrix[posicionX][posicionY - 1] = segundo
            posiciones[0] = [posicionX + 1, posicionY]
            posiciones[1] = [posicionX, posicionY - 1]

    elif posicionX != (n - 1):
        if posicionY == 0:
            primero = calculamelo(posicionX - 1,posicionY)
            segundo = calculamelo(posicionX + 1,posicionY)
            tercero = calculamelo(posicionX,posicionY + 1)
            matrix[posicionX - 1][posicionY] = primero
            matrix[posicionX + 1][posicionY] = segundo
            matrix[posicionX][posicionY + 1] = tercero
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX + 1, posicionY]
            posiciones[2] = [posicionX, posicionY + 1]

        elif posicionY != (m-1):
            primero = calculamelo(posicionX - 1,posicionY)
            segundo = calculamelo(posicionX + 1,posicionY)
            tercero = calculamelo(posicionX,posicionY + 1)
            cuarto = calculamelo(posicionX,posicionY - 1)
            matrix[posicionX - 1][posicionY] = primero
            matrix[posicionX + 1][posicionY] = segundo
            matrix[posicionX][posicionY + 1] = tercero
            matrix[posicionX][posicionY - 1] = cuarto
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX + 1, posicionY]
            posiciones[2] = [posicionX, posicionY + 1]
            posiciones[3] = [posicionX, posicionY - 1]

        else:
            primero = calculamelo(posicionX - 1,posicionY)
            segundo = calculamelo(posicionX + 1,posicionY)
            tercero = calculamelo(posicionX,posicionY - 1)
            matrix[posicionX - 1][posicionY] = primero
            matrix[posicionX + 1][posicionY] = segundo
            matrix[posicionX][posicionY - 1] = tercero
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX + 1, posicionY]
            posiciones[2] = [posicionX, posicionY - 1]
    
    else:
        if posicionY == 0:
            primero = calculamelo(posicionX - 1,posicionY)
            segundo = calculamelo(posicionX,posicionY + 1)
            matrix[posicionX - 1][posicionY] = primero
            matrix[posicionX][posicionY + 1] =segundo
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX, posicionY + 1]

        elif posicionY != (m-1):
            primero = calculamelo(posicionX,posicionY - 1)
            segundo = calculamelo(posicionX,posicionY + 1)
            tercero = calculamelo(posicionX - 1,posicionY)
            matrix[posicionX][posicionY - 1] = primero
            matrix[posicionX][posicionY + 1] = segundo
            matrix[posicionX - 1][posicionY] = tercero
            posiciones[0] = [posicionX, posicionY - 1]
            posiciones[1] = [posicionX, posicionY + 1]
            posiciones[2] = [posicionX - 1, posicionY]

        else:
            primero = calculamelo(posicionX - 1,posicionY)
            segundo = calculamelo(posicionX,posicionY - 1)
            matrix[posicionX - 1][posicionY] = primero
            matrix[posicionX][posicionY - 1] = segundo
            posiciones[0] = [posicionX - 1, posicionY]
            posiciones[1] = [posicionX, posicionY - 1] 

    #almacenamos en la matrizIntermedia, los valores de los valores que ha ido comparando
    '''
    for i in posiciones:
        if i[0] != -1:
            condicion = False
            for j in matrizIntermedia[1]:
                if i == j : condicion = True

            if condicion == False:
                matrizIntermedia[1].append(i)
            else: pass

        else: pass
    '''


    if pivote >= primero and pivote >= segundo and pivote >= tercero and pivote >= cuarto:
        if pivote not in matrix:
            matrizIntermedia[0]=[posicionX, posicionY]
            return matrizIntermedia
        else:
            return matrizIntermedia
    else:
        if pivote < primero and primero not in matrix:
            resultado = HillClimbing(matrix, n, m, posiciones[0][0],posiciones[0][1],matrizIntermedia)
            return resultado
        elif pivote < segundo and segundo not in matrix:
            resultado = HillClimbing(matrix, n, m, posiciones[1][0],posiciones[1][1],matrizIntermedia)
            return resultado
        elif pivote < tercero and tercero not in matrix:
            resultado = HillClimbing(matrix, n, m, posiciones[2][0],posiciones[2][1],matrizIntermedia)
            return resultado
        elif pivote < cuarto and cuarto not in matrix:
            resultado = HillClimbing(matrix, n, m, posiciones[3][0],posiciones[3][1],matrizIntermedia)
            return resultado
        else: 
            return matrizIntermedia



            


#main

import sys
sys.setrecursionlimit(3000)

n = int(input("introduce n: "))
m = int(input("introduce m: "))
while n <= 1 or m <= 1:
    n = int(input("introduce n: "))
    m = int(input("introduce m: "))
matrix = np.zeros((n, m))
start_time = time()

#matrix = calculaValores(matrix,n,m)
elapsed_time = time() - start_time
print("Tarda:  %.10f" %elapsed_time, " en completar la matriz")
start_time = time()
HillClimbingModificada(matrix,n,m)
elapsed_time = time() - start_time
print("Tarda: %.10f" %elapsed_time, " en completar la busqueda del maximo")

#time
#dibujarValores(matrix,n,m)

