# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#declarar funciones para + - x / y usarlas desde otra función general

def suma(x, y):
    suma = x + y
    print ("la suma de x e y es : suma")
    return
x = 3
y = 5
suma(x, y)
print("programa terminado")

def resta():
    resta = x - y
    return resta
def multiplicación(x, y):
    multiplicación = x * y
    return multiplicación
def división(x, y):
    división = x / y
    return división

# representar varias operaciones matemáticas en consola (print)

x = 2
y = 5
z1 = x + y
z2 = (x*y)/2
print(z1)
print(z2)


#representa comparaciones de los siguientes tipos (int, float, string)

int('432')
str('432')
float('432')

x = 5
type(x)


#PANDAS:

#1# cargar un excel con números

df1 = pd.read_excel('tabla.xls', index_col = 0)

#1.1# mostrar la suma de la primera columna
#group_1 = df1.groupby('data1')
data_sum = df1.groupby('data1').apply(sum)
print(data_sum)




#2# cargar un archivo de texto en pandas
df2 = pd.read_csv('texto_tarea.txt', header = None)

#3# añadir una columna a cualquiera de los archivos anteriores


columna_add = pd.Series([0,1,2,3], name ="columna_add")
df3 = df1.append("columna_add")

#4# Guardar el archivo final de 3 en excel

df4 = df3.to_xls('texto_tarea_toxls.xls')

#5# representar gráficamente la primera columna de 1


df1 = pd.read_excel('tabla.xls', index_col = 0)
plt.plot("df1")
plt.show()






















