import numpy as np
import math

E = 1.5*10**9
mp = 1.67262178*10**-27
me = 9.102*10**-31
e = 1.602*10**-19
c = 2.99792458*10**8
gamma = (E*e/(mp*(c**2)))
beta = ((1/gamma)**2-1)*-1


def drift(L):
   d = np.array([[1, L,0,0,0,0],[0, 1,0,0,0,0],
                 [0,0,1, L,0,0],[0,0,0,1,0,0],
                [0,0,0,0,1,1/(beta**2*gamma**2)],[0,0,0,0,0,1]])
   return d
   
def fquad(L,K):
    foc = np.array([[math.cos(K*L), math.sin(K*L)/K,0,0,0,0],[-K*math.sin(K*L), math.cos(K*L),0,0,0,0],
                     [0,0,math.cosh(K*L),math.sinh(K*L)/K,0,0],[0,0,K*math.sinh(K*L), math.cosh(K*L),0,0],
                       [0,0,0,0,1,1/(beta**2*gamma**2)],[0,0,0,0,0,1]])
    return foc
    
def dquad(L,K):
    defoc = np.array([[math.cosh(K*L), math.sinh(K*L)/K,0,0,0,0],[K*math.sinh(K*L), math.cosh(K*L),0,0,0,0],
                       [0,0,math.cos(K*L), math.sin(K*L)/K,0,0],[0,0,-K*math.sin(K*L), math.cos(K*L),0,0],
                        [0,0,0,0,1,1/(beta**2*gamma**2)],[0,0,0,0,0,1]])
    return defoc
    
def initial(x,px,y,py,z,pz):
    #zp = (math.sqrt(E**2-(mp**2*c**4)))/c
    zp = pz
    xp = px/pz
    yp = py/pz
    x = np.array([[x],[xp],[y],[yp],[z],[zp]])
    return x
    
#Kanske så här
    
def testinitial(x,y,z,px,py,pz):
    x = x
    y = y
    z = z
    xp = px/pz
    yp = py/pz
    zp = pz
#    zp = ????    
    a = np.array([[x],[xp],[y],[yp],[z],[zp]])
    return a
   
    
def sections(a,initial):
    l = len(a)
    calc1 = a[l-1]
    calc2 = a[l-2]
    calc = np.dot(calc1,calc2)
    l = l-2
    while l > 0:
        calc1 = a[l-1]
        calc = np.dot(calc,calc1)
        l = l-1
    calc = np.dot(calc,initial)
    return calc
