#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:03:24 2017

@author: santi
"""

from matplotlib import pyplot as plt
import seaborn as sbn 
import numpy as np 

'''vamos a representar los términos de la función coseno. 
defino factorial que es una función dentro de la función coseno.
defino la función coseno. 


'''
PI = 3.141592654

def fact(y):
    val = 1.0
    for i in range(1,y+1):
        val = val*i
    return val

def cos(x, nn=10):
    """
    función coseno calculada a través de la aproximación de Taylor. 
    x: ángulo en radianes
    nn: número de términos de la aproximación de Taylor
    return: vector con los términos de la aproximación de Taylor
    
    """
    x = x - int(x / 2/ PI) * 2*PI  #transportamos el ángulo al intervalo [-pi, pi]
    vector = np.empty(nn, dtype=np.double)
    for n in range(nn):
        vector[n] = (-1)**n * x**(2*n) / fact(2*n)
    return vector


def Rastrigin_vect(x, An, A):
    return An + np.sum(x*x + A*np.cos(2*np.pi*x), axis=1)


terminos = cos(400, nn=30)
print(terminos.sum())
plt.plot(terminos, marker= 'o', linestyle='-.')
plt.title("Términos de función coseno aproximada por Taylor")
plt.xlabel("Número de términos")
plt.ylabel("Valor del término")
plt.savefig ("función_coseno.png")



fig1 = plt.figure()
ax1 = fig1.add_subplot(1,2,1)
ax1.set_axis_bgcolor("w")
ax1.axhline(0, color='k', alpha=0.7)
ax1.axvline(0, color='k', alpha=0.7)
ax1.plot(terminos, marker= 'o', linestyle=':', linewidth=0.5)
ax1.set_title("Términos de función coseno aproximada por Taylor")
ax1.set_ylabel("Valor del término")
ax1.set_xlabel("Número de términos")

terminos_rastrigin = Rastrigin_vect(x=np.random.rand(10, 3), An=10, A=10)
ax2 = fig1.add_subplot(1,2,2)
ax2.set_axis_bgcolor("w")
ax2.axhline(0, color='k', alpha=0.7)
ax2.axvline(0, color='k', alpha=0.7)
ax2.plot(terminos_rastrigin, marker= 'o', linestyle=':', linewidth=2, label='rastigin')
ax2.set_title("Términos de función coseno aproximada por Taylor")
ax2.set_ylabel("Valor del término")
ax2.set_xlabel("Número de términos")
ax2.legend()

fig2 = plt.figure()
bx1 = fig2.add_subplot(1,1,1)
bx1.set_axis_bgcolor("w")
bx1.axhline(0, color='k', alpha=0.7, linewidth=0.5)
bx1.axvline(0, color='k', alpha=0.7, linewidth=0.5)

ind = np.linspace(0, 9, 10)
width = 0.5
bx1.bar(ind, terminos_rastrigin, width, color='r', alpha=1, label='bars')
bx1.plot(terminos_rastrigin, marker= 'o', linestyle=':', linewidth=2, label='rastigin')
bx1.set_title("Términos de función coseno aproximada por Taylor")
bx1.set_ylabel("Valor del término")
bx1.set_xlabel("Número de términos")
bx1.legend()








plt.show()