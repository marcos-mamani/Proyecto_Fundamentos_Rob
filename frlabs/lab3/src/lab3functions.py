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
    #T0 =dh(0,0,0,-pi/2)
    #T1 =dh(-q[0]-1.38,0,0,pi/2)
    #T2 =dh(0.56,q[1],0.75,pi/2)
    #T3 =dh(0,q[2]+pi/2,1.7,0)
    #T4 =dh(-0.01,q[3],0,pi/2)
    #T4 =dh(0,q[3],0,pi/2)
    #T5 =dh(1,q[4],0,-pi/2)
   # T6 =dh(0,q[5],0,pi/2)
    #T7 =dh(0.25,q[6],-0.06,0)
    # Efector final con respecto a la base
    #T0 =dh(0,0,0,-pi/2)
    #T1 =dh(-q[0]-1.38,0,0,pi/2)
    #T2 =dh(0.56,q[1],0.75,pi/2)
    #T3 =dh(0,q[2]+pi/2,1.7,0)
    T0 =dh(0,0,0.395,-pi/2)
    T1 =dh(-q[0]+0.562,0,0,pi/2)
    T2 =dh(0.76403,q[1],0.73999,pi/2)
    #T2 =dh(0.76403,q[1],0.52,pi/2)
    #T2 =dh(0.58+1.60,q[1],0,pi/2)
    T3 =dh(0,q[2]+pi/2,1.145,0)
    #T4=dh(0,-q[3],0,pi/2)
    T4=dh(0,-q[3],0,pi/2)
    #T5 =dh(1.2501,q[4],0.24989,-pi/2)
    T5=dh(0,0,0.24989,0)
    T6 =dh(1.226,q[4],0,-pi/2)
    #T6 =dh(0,q[5],0,pi/2)
    #T7 =dh(0.176,0,0,0)
    T7 =dh(0.034,0,0,0)
    T8 =dh(0,q[5],0,pi/2)
    #T7 =dh(0.24996,q[6],0,0)
    #T7 =dh(0.04137,0,0,pi/2)
    T9 =dh(0.24996,q[6]+pi/2,0,pi/2)

    T =T0.dot(T1).dot(T2).dot(T3).dot(T4).dot(T5).dot(T6).dot(T7).dot(T8).dot(T9)
    return T


