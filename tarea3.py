# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:24:52 2022

@author: Alex
"""
#########################################
#EJERCICIOS
#########################################
#%%
#Crear funcion resta que resta 2 números y devuelve el resultado

def subtraction (a, b):
    sub = a - b
    return(sub)
res = subtraction(5, 2)
print(res)

#%%
#Crear funcion lambda que combierte un string a minusculas
#func_lambda = lambda input: ouput

conversion_lambda = lambda c:c.lower()
resultado = conversion_lambda("HOLA")
print(resultado)
#%%
conver = lambda i:i.upper()
res = conver("hola")
print(res)
#%%
#Crear funcion que acepta 3 argumentos, 2 numeros y un string. Si el string es
#"suma". devolver la usma de los dos numeros, si el string es "resta" devolver la resta
def operacion (a,b,c):
    if a=="suma":
        suma = b + c
        return(suma)
    elif a=="resta":
        resta = b - c
        return(resta)

res = operacion("suma", 12, 3)
print(res)
sums = operacion("resta",15,5)
print(sums)
#%%
x = input("Escriba la operación que desea realizar: 'suma' o 'resta' ")
y = int(input("Escriba el primer número: "))
z =int(input("Escriba el segundo número: "))

oper = operacion(x,y,z)
print("El resultado de la operación es: ", oper)
#%%
#Crear una funcion que pregunte al usuario una frase y devuelva dicha frase con palabras
#en orden inverso. Por ejemplo, si el susuario dice "la lluvia en Sevilla"
#la funcion devolverá "Sevilla en lluvia la"

def invertir_frase(cadena):
    return cadena[::-1]

frase = input("Ingeres una frase por favor: ")
print(invertir_frase(frase))
#%%
def cambio(frase):
    frase = frase.split(' ')[::-1]# .split(' ')Divide la cadena en una lista de palabras, [::-1] Se hace la inversión
    frase = ' '.join(frase)# Se convierte en cadena 
    return frase
texto = input("Ingrese una frase por favor: ")
print(cambio(texto))
        
#%%
#Crear una funcion que detecte si una palabra o frase es palindromo
#(un palindromo es aquella palabra o frase que se lee de igual forma de un sentido u otro)

def palindromo(frase):
    #convertimos a minusculas todo
    frase = frase.lower()
    #Reemplazamos espcaios por caracter vacio
    frase = frase.replace(' ','')
    #preguntemos si la longitud de la cadena es par
    long = len(frase)
    if long % 2 ==0:
        izquierda = frase[:long // 2]
        derecha = frase[long // 2:]
    else:
        izquierda = frase[:long // 2]
        derecha = frase[long // 2 + 1:]
        #invertimos la cadena derecha
    return izquierda == derecha[::-1]
palabra = input(str("Ingrese una frase y comprueba si es palindromo: "))
print(palindromo(palabra))
if palindromo(palabra)== True:
    print("La frase que ingreso es palindroma")
else:
    print("La frase que ingreso no es palindroma")
#A luna ese anula

#%%
#Crear un funcion que dada una lista de listas, nos devuelva una lista simple (es decir, sin ninguna lista dentro)
# por ejemplo, si a dicha funcion le pasamos el argumento

#List_nesteada = [
#    [1,2,3],
#    [4,5,6,7],
#    [8,9]
#]
#La funcion devolvera la lista [1,2,3,4,5,6,7,8,9]
nueva_lista = []
def nestear(lista):
    for i in lista: #atraviesa las listas anidadas
        for item in i: #itera sobre los elementos de cada lista anidada y los añade a una nueva lista.
            nueva_lista.append(item)
    return nueva_lista
List_nesteada = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]
print(nestear(List_nesteada))
#%%
lista2 = list(input("Ingrese su lista de lista: "))
print(lista2)
