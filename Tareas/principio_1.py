# -*- coding: utf-8 -*-
from math import cos
entero = int(3)
flotante = float(7.9)
cadena = str("hola mundo")
complejo = complex(4+5j)
boleano = bool("True")



entero = 3
suma = entero + entero

flotante = 7.9
cadena = "hola mundo"
complejo = 4+5j
boleano = True



suma2 = entero + flotante
suma3 = complejo + entero
suma4 = complejo + boleano


if suma:
    print("valor positivo")
else:
    print("suma es cero")
    
if not suma:
    print("ha sido cero") 
else:
    print("ha sido positivo")
    


lista = ["A", "T", "G", "C"]
diccionario = {"A":"adenina", "T":"timina", "C":"citosina", "G":"guanina"}
lista2 = [diccionario[elemento]  for elemento in lista]
lista3 = []
for elemento in lista:
    lista3.append(diccionario[elemento])

    
if lista2 == lista3:
    print("son iguales")
else:
    print("no son iguales")

conjunto = {"uno", "dos", "tres"}
conjunto2 = {"tres", "cuatro", "cinco"}


def f(x):
    return(3*x)


def fact(y):
    val = 1.0
    for i in range(1,y+1):
        val = val*i
    return val


def cos2(x):
    val = 0.0
    for n in range(10):
        val = val + (-1)**n * x**(2*n) / fact(2*n)
    return val



def Rastrigin(x, A, pi, An):
    val=0
    n = len(x)
    for i in range(n):
        aa = x[i]**2 - A*cos(2*pi*x[i])
        print(x[i], cos(2*pi*x[i]), aa)
        val = val + aa
    val = val + An
    return val

resultado= Rastrigin([1,3,5], 10, 3.14, 10)
print (resultado)





