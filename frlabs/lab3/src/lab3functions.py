import numpy as np
from copy import copy

cos=np.cos; sin=np.sin; pi=np.pi


def dh(d, theta, a, alpha):
    """
    Calcular la matriz de transformacion homogenea asociada con los parametros
    de Denavit-Hartenberg.
    Los valores d, theta, a, alpha son escalares.
    """
    # Escriba aqui la matriz de transformacion homogenea en funcion de los valores de d, theta, a, alpha
    T = np.array([[cos(theta),-cos(alpha)*sin(theta),sin(alpha)*sin(theta),a*cos(theta)],
                  [sin(theta),cos(alpha)*cos(theta),-sin(alpha)*cos(theta),a*sin(theta)],
                  [0,sin(alpha),cos(alpha),d],
                  [0,0,0,1]])

    return T
    
    

def fkine_robot(q):
    """
    Calcular la cinematica directa del robot UR5 dados sus valores articulares. 
    q es un vector numpy de la forma [q1, q2, q3, q4, q5, q6]
    """
    # Longitudes (en metros)
    # Matrices DH (completar), emplear la funcion dh con los parametros DH para cada articulacion
    #T1 = dh(0.352 ,-pi/2, q[0]+1.38, 0)
    #T2 = dh(0.295, q[1], 0, 0)
    #T3 = dh(0, q[2]+pi/2, 0.752,0)
    #T3 = dh(0, q[2],0.752,0)
    #T4 = dh(0, q[3], 1.149, pi/2)
    #T4 = dh(1.3, q[3], 0, pi/2)
    #T5 = dh(L5, q[4], 0, -pi/2)S
    #T6 = dh(L6, q[5], 0, 0)
    T0 =dh(0,0,0,pi/2)
    T1 =dh(q[0]+1.38,pi/2,0,-pi/2)
    T2 =dh(0,q[1]+pi/2,0.295,90)
    # Efector final con respecto a la base
    T =T0.dot(T1).dot(T2)#.dot(T3).dot(T4)
    return T


