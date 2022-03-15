# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:37:06 2022

@author: Alex
"""

#Las funciones son formas de separar la logica en piezas sin tener que ejecutarlas linea a linea,
#y ademas permitir reutilizar partes del codigo que se repiten

###################
#Las funciones se definen de la forma:
# def nombre_de_la_funcion[argumento1, argumento2,...]:
    #logica de la funcion
#########
#%%
def saludar():
    print("Hola mundo")
#Al escribir la función saludar, no tenemos que escriobir print cada vez
saludar()
saludar()    
#%%
#La principal ventaja de las funciones es que nos permite usar argumentos y
#flexibilizar la lógica de nuestro código
def saludar(nombre):
    print(f"Hola {nombre},¿como estas?")
saludar("Manuel")
saludar("Antonio")
#%%
#Como esta funcion necesita un argumento, si la llamamos sin ningun argumento
#Nos dara un error
saludar()
#%%
#La funciones tambien pueden tener valores por defecto en los argumentos.
def saludar_despistado(nombre = "amigo"):
    saludar(nombre)
    
saludar_despistado("Manuel")
saludar_despistado()
#%%
#Las funciones pueden devolver un valor.

def suma(a, b):
    return a + b
    print("Esto no se va a imprimir, porque la funcion acaba con el return")

resultado_suma1 = suma(2.5, 5)
print(resultado_suma1)
#%%
#ahora podemos usar el resultado de la funcion como input
resultado_suma2 = suma(resultado_suma1, 50)
print(resultado_suma2)
#%%
#Una funcion que no tiene un return devuelve None
def suma_erronea (a, b):
    resultado = a + b
    return resultado

resultado_suma1 = suma_erronea(2.5, 5)
print(resultado_suma1)
#%%
#Las funciones pueden tener un solo return, pero pueden devolver multiples cosas:
def sum_and_subtraction (a, b):
    Sum = a + b
    subtraction = a - b
    return Sum, subtraction
result = sum_and_subtraction(10, 5)
print(result)
print(type(result))
#%%
#podemos desempaquetar el resultado directamente
result_sum, result_subtraction = sum_and_subtraction(10, 5)
print(result_sum)
print(result_subtraction)
#%%
#Existe otra forma de crear funciones, las llamadas lambda o funciones anonimas
#Se define de la forma:
    #func_lambda = lambda input: ouput
#Las funciones lambda se suelen utilizar cuando queremos aplicar lógica sencilla
#para la cual definir una función "oficial" no es necesaria
###########

sum_lambda = lambda a, b: a + b
result_sum1 = sum_lambda(2.5, 5)
print(result_sum1)
#%%
#Ahora podemos usar el resultado de la funcion como input
result_sum2 = sum_lambda(result_sum1, 50)
print(result_sum2)
#%%
