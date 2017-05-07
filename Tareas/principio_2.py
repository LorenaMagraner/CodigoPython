#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:08:13 2017

@author: santi
"""

import numpy as np

#inicialización de arrays
vacia_1d = np.empty(10, dtype=np.double)
ceros_1d = np.zeros(10, dtype=np.double)
unos_1d = np.ones(10, dtype=np.int)


vacia_2d = np.empty((2,5), dtype=np.double)
ceros_2d = np.zeros((2,5), dtype=np.double)
unos_2d = np.ones((2,5), dtype=np.double)

#operaciones
tres_2d = np.ones((2,5), dtype=np.double)*3
unos_2d_3 = unos_2d.dot(tres_2d.transpose())

#slicing
np.random.seed(3)
matrix1 = np.random.rand(4,5)
matrix2 = matrix1[1:3,1:3]
matrix3 = matrix1[:,0]
matrix4 = matrix1[2, :]

#operaciones agregadas
tres_2d_suma_eje_cero = tres_2d.sum(axis=0)
tres_2d_suma_eje_uno = tres_2d.sum(axis=1)
tres_2d_media_eje_uno = tres_2d.mean(axis=1)
tres_2d_desviacion_eje_uno = tres_2d.std(axis=None)
matrix1_varianza = np.sqrt(matrix1.std(axis=None))
matrix_var = np.sqrt(np.std(matrix1))
lista = np.mean([2,3,4,2])
array = np.array([3,2,4,5])

#concatenar arrays
array2 = np.hstack((array,array)) #en eje cero
array3 = np.vstack((array,array)) #en eje uno 
array4 = np.r_[array,array] #junta por filas
array5 = np.c_[array, array] # junta por columnas

#operaciones vectorizadas
def Rastrigin_vect(x, An, A):
    return An + np.sum(x*x + A*np.cos(2*np.pi*x))

x = np.array((1,3,5))
print(Rastrigin_vect(x,10,10))


