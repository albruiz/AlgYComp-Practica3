'''
Alberto Ruiz Andres

    f1(x,y) = sin(x) + cos(y) + sin(x) * cos(y) + sin(x*2)
    f2(x,y) = 2 * sin(x) * cos(y/2) + x +  log( abs(y-pi/2))
    f3(x,y) = sin(x) * cos(y) + sqrt(x*y)
    f4(x,y) =  sin( x*7 ) + cos( (y+pi/4)*4 ) + (x+y)

'''


import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits import mplot3d
from pylab import *

import random


# Funcion que se encarga de calcular los valores de la funcion matematica y añadirlos a la matriz
# Parametros: matriz, numFilas, numColumnas, indexFormula
def calculaValores(matrix, n, m, decision):
    
    valorUnitario1 = math.pi/(n-1)
    valorUnitario2 = math.pi/(m-1)

    #f1(x,y) = sin(x) + cos(y) + sin(x) * cos(y) + sin(x*2)
    if decision == 1 :
        for i in range(n):
            for j in range(m):
                valorCalculado = math.sin(i*valorUnitario1) + math.cos(j*valorUnitario2) + (math.sin(i*valorUnitario1) * math.cos(j*valorUnitario2)) + math.sin(2*(i*valorUnitario1))
                matrix[i][j]= valorCalculado

    #f2(x,y) = 2 * sin(x) * cos(y/2) + x +  log( abs(y-pi/2))
    elif decision == 2 :
        for i in range(n):
            for j in range(m):
                valorCalculado = 2 * math.sin(i*valorUnitario1) + math.cos((j*valorUnitario2)/2) + (i*valorUnitario1) + math.log((abs((j*valorUnitario2)-(math.pi/2))), 10)
                matrix[i][j]= valorCalculado
    
    #f3(x,y) = sin(x) * cos(y) + sqrt(x*y)
    elif decision == 3 :
        for i in range(n):
            for j in range(m):
                valorCalculado = (math.sin(i*valorUnitario1) * math.cos(j*valorUnitario2)) + math.sqrt((i*valorUnitario1)*(j*valorUnitario2))
                matrix[i][j]= valorCalculado

    #f4(x,y) =  sin( x*7 ) - cos(4y) + (x+y)
    else:
        for i in range(n):
            for j in range(m):
                valorCalculado = math.sin(7*(i*valorUnitario1)) + math.cos(4*(j*valorUnitario2)) + (i*valorUnitario1)+(j*valorUnitario2)
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
        x.append(((matrizSolucion[1][i][0])*math.pi)/(n-1))
        y.append(((matrizSolucion[1][i][1])*math.pi)/(m-1))
    x = np.array(x)
    y = np.array(y) 
    # posiciones intermedias iran en color negro
    # posicion incial ira en azul
    # posicion máxima ira en rojo  

    plot(x,y,'sk')
    plot(((matrizSolucion[2][0])*math.pi)/(n-1),((matrizSolucion[2][1])*math.pi)/(m-1), 'sb')
    plot(((matrizSolucion[0][0])*math.pi)/(n-1),((matrizSolucion[0][1])*math.pi)/(m-1), 'sr')
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
eleccion = -1
condicion = False
while condicion == False :
    print("Introduce un numero entre el 1 y el 4 para elegir la funcion sobre la que trabajaremos \n 1) f1(x,y) = sin(x) + cos(y) + sin(x) * cos(y) + sin(x*2) \n 2) f2(x,y) = 2 * sin(x) * cos(y/2) + x +  log( abs(y-pi/2)) \n 3) f3(x,y) = sin(x) * cos(y) + sqrt(x*y) \n 4) f4(x,y) =  sin( x*7 ) + cos( (y+pi/4)*4 ) + (x+y) \n ")
    eleccion = int(input())
    if eleccion == 1 or eleccion == 2 or eleccion == 3 or eleccion == 4:
        condicion = True

matrix = calculaValores(matrix,n,m, eleccion)
dibujarValores(matrix,n,m)
