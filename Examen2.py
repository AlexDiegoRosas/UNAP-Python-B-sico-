# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 08:18:33 2022

@author: Alex
"""

#Complete la palabra reservada de python en el siguiente programa:
x = 6

if x < 0:
    print("negativo")
elif x == 0:
    print ("cero")
else:
    print("positivo")

#%%
#Cual de las opciones es equivalente al codigo de python mostrado 
if 5 == 2:
    print("si")
else:
    print("No")
#%%
#print ("No")if 5 == 2 else print ("Si")
#%%
#if 5 == 2 print("Si"): print("No")
#%%
#if 5 == 2 print ("Si")else print("No")
#%%
print ("Si") if 5 == 2 else print ("No")
#%%
#if 5==2 print("si")else print("no")

#%%
#Que instruccion en python es necesario colocar, para que el programa muestre por pantalla solo números de 1 y 2
x = 0

while x < 5:
    x += 1
    if x == 3:
        break    
    print (x)
#%%
#cual es la salida que produce este bloque de codigo en python?

x = 0
while x < 3:
    x = x + 1
else:
    print (x)

#%%
#Complete la palabra reservada de python en el siguiente programa,
#para que muestre los siguientes colores: azul, amarillo y verde

colores = ["rojo",
           "azul",
           "amarillo",
           "verde"]
for x in colores:
    if x == "rojo":
        continue
    print (x)
#%%
#¿cual es la salida que produce este bloque de código en python?

for num in range (5):
    print (num)
#%%
#Que numero imprime el siguiente código de python?
x = range(7, 15, 2)
for n in x:
    print (n)
#%%
#cual es la salida que produce este bloquede codigo en pyhton?
x = 0
while x < 3:
    x = x + 1
else:
    for n in range (x,x+3):
        print (n)
#%%
# que es __init__ y muestre un ejemplo de uso
#Es un metodo que ayuda a contruir objetos en Python
#CLASE
class NombreClase:
    pass

primer_objeto = NombreClase()
#%%
#ATRIBUTOS Y MÉTODOS
class NinjaPrincipal:
    HP = 100
    resistencia = 50
    puntos_experiencia = 1
    vidas = 3
    def game_over(self):
        print("Game over")
        
ninja = NinjaPrincipal()
#print(ninja.HP)
ninja.HP = 0
ninja.vidas = 0
if ninja.HP == 0 and ninja.vidas ==0:
    ninja.game_over()
#%%
#METODO CONSTRUCTOR __init__
ninja_enemigo = NinjaPrincipal()
ninja_enemigo.HP = 25
ninja_enemigo.resistencia = 10
ninja_enemigo.vidas = 1
print(ninja_enemigo.HP, ninja_enemigo.resistencia, ninja_enemigo.vidas)
#%%
class NinjaPrincipal:
    def __init__(self,HP,resistencia,puntos_experiencia,vidas):
        self.HP = HP
        self.resistencia = resistencia
        self.puntos_experiencia = puntos_experiencia
        self.vidas = vidas
        def game_over(self):
            print("Game over")
        
ninja1 = NinjaPrincipal(100, 50, 1, 4)
ninja1.salto = True
ninja_enemigo2 = NinjaPrincipal(25, 10, 1, 1)
print(ninja_enemigo2.resistencia)
print(ninja1.salto)
#%%    
class animal:
    def __init__(self,nombre,patas,especie):
        self.nombre = nombre
        self.patas = patas
        self.especie = especie
    
perro = animal("Tobias",4,"can")
gato = animal("Humberto",4,"felido")

print (perro.nombre,perro.patas,perro.especie)
print (gato.nombre,gato.patas,gato.especie)
    

#%%
#Cual es la diferencia entre método y funciones, muestre un 
#Función: una función en un código independiente que incluye algo
#de lógica y debe llamarse de manera independiente y se define fuera de la clase.
#Método: un método es un fragmento de código independiente que se llama en referencia a algún objeto
#y se define dentro de la clase.

def multiplicar (num1,num2):
    print(num1*num2)

multiplicar(10, 5)

#Python lenguaje multiparadigma
#Las clases son modelos sobre los cuales se contruiran 
#nuestros objetos
#%%
#los objetos son instancias de esa clase

#creamos la clase Persona son los atributos nombre y edad
class Persona:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
juan = Persona("Juan", "Ramirez", 22, "Masculino" )
maria = Persona("Maria", "Quispe", 19, "Fenenino")
print(juan.edad)
print(maria.sexo)

class carro:
    marca = "toyota"

class ticla: 
    marca = "xd"

taxi = carro()
print(taxi.marca)

patru=ticla()
print(taxi.marca)

class VehiculoParticular:
    def __init__(self,marca,modelo,placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
taxi = VehiculoParticular ("Renault","Duster","Z1R423")

class Persona:
    pass

marlon = Persona()
katy = Persona()
juan = Persona()

marlon.edad = 22
katy.edad = 21


class Matematica:
    def __init__(self):
        self.num1 = 14
        self.num2 = 3

suma = Matematica()
print("la suma es: ", suma.num1 + suma.num2)

