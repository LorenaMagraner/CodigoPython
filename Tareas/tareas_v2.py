# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#declarar funciones para + - x / y usarlas desde otra función general

def suma(numeros):
    suma = sum(numeros)
    return  suma ## No se devuelve nada
numeros = [1,2]   
print("programa terminado")


def resta(numeros):
	resta = resta(numeros)  # has llamado a la variable igual que la funcion. Y estas llamando a la fuincion en bucle infinito (piensalo)
	return resta
numeros = [4 ,3]
print("programa terminado")


def multiplicación (numeros): 
	multiplicación = multiply(numeros)
	return multiplicación
numeros =[2, 3]
print ("programa terminado")

def división (numeros):
	división = divide(numeros)
	return división
numeros = [7,2]
print ("programa terminado")


# representar varias operaciones matemáticas en consola (print)

x = 2
y = 5
z1 = x + y
z2 = (x*y)/2
print(z1)
print(z2)

# Si usas las operaciones por defecto, ara qué te sisrven las que has declarado?


#representa comparaciones de los siguientes tipos (int, float, string)

# ¿Dónde se representan en la consola?
x = str('421')
print (x+x)
str('432')

y = 4/float('3')
print(y)

b = 4//3
print(b)

x = 5
print(type(x))




#PANDAS:

#1# cargar un excel con números
df1 = pd.read_excel('tabla.xls', index_col = 0)

#1.1# mostrar la suma de la primera columna
df1 = pd.DataFrame(df1)
df2 = df1.sum()
print (df2)
#estoy casi casi, con esto me da la suma justo de las otras dos....
#pero no doy con la solucion, si pongo (axis=0) me da lo mismo, si pongo
#axis=1 me suma la dos y la tres, y cualquier otra opción, error. por?




#2# cargar un archivo de texto en pandas
df2 = pd.read_csv('texto_tarea.txt')


#3# añadir una columna a cualquiera de los archivos anteriores


df1 = pd.read_excel('tabla.xls', index_col = 0)
columna_add = pd.Series([0,1,2,3], name ="columna_add")
df3 = df1.append(columna_add) 




#4# Guardar el archivo final de 3 en excel

df4 = df3.to_excel('texto_tarea_toxls.xls')

#5# representar gráficamente la primera columna de 1


df1 = pd.read_excel('tabla.xls', index_col = 0)
plt.plot("df1")  # así no es, es df1.plot()
plt.show()






















