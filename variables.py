# Aquí se explican los principales tipos de varibles.
#@author: Alex

#******************
# Python tiene muchos tipos de variables básicas que forman parte del núcleo del lenguaje, son los que se llama primitivas.
#****************************************
#Las primitivas mas comunes son strings, numeros, booleanos********


#********************************************#
#STRINGS
#********************************************#

print("Se usa para representar texto")

var_str = "Hola"
var_str2 = "Mundo"

print(type(var_str))
print(type(var_str2))

#*******************************************#
# Los strrings se pueden unir para formar strings más largos. Hay varias maneras de unir strigns (lo que se llama interpolación de strings)
#*************************************************************#

# Podemos usar el simbolo + para "sumar" (concatenar) strings#

var_str_unido = var_str+ " "+var_str2
print(var_str_unido)
#%%
#*********************************************#
#Podemos "multiplicar" strings!

n = "monja "
print(n*10)
#%%
#******************************************#
#Tambien podemos usar el método format, que nos permite instertar unos strings dentro de otros.
nombre = "Manuel"
ciudad = "Murcia"
presentacion = "Hola, me llamo {}, soy de {}" #format(nombre,ciudad)
print(presentacion.format(nombre,ciudad))

nombre2 = "Maria"
ciudad2 = "Madrid"
print (presentacion.format(nombre2, ciudad2))
#**********************************************#

#Usando el metodo format se pude indicar como formatear las variables
#Por ejemplo, redondear numeros decimales.

import math
print(math.pi)
pi_str = "Los primeros digitos de pi son: {}".format(math.pi)
print(pi_str)
#Podemos restringir que se imprima con 2 decimales
pi_str1 = "Los primeros digitos de pi son: {:.2f}".format(math.pi)
print(pi_str1)
#Si pasamos 0 decimales hemos redondeado a un entero
pi_str2 = "Los primeros digitos de pi son: {:.0f}".format(math.pi)
print(pi_str2)

#***************************************************#
#Otra manera de usar interpolación de strings {solo disponible en python 3.6 en adelante} es referenciar directamente las variables en el string convirtiendolo en un f-string(se convierte un string poniendole la letra f delate)
#********#
presentacion2 = f"Hola, me llamo {nombre}, soy de {ciudad}"
print(presentacion2)
#%%
#nombre = "Juan"
#print(presentacion2)
#%%
#***********************
# MAS OPERACIONES CONS STRINGS
#**************************#

titulo = "Introducción a PYTHON"

print("convertimos un string en mayusculas con upper")
print(titulo.upper())

print("convertimos un string en minusculas con lower")
print(titulo.lower())

print("Ponemos la primera letra en mayúscula con capitalize")
print(titulo.capitalize())

print("usamos ")
#%%%%%%
#Se puede separar uns string en multiples usando el método split()

colores_str = "rojo|amarillo|verde|azul"
colores_lista = colores_str.split("|")
print(colores_lista)
print(type(colores_lista))
#%%
#*****************************#
#NUMEROS
#********************************#
print("Hay dos tipos báiscos de primitivas numericas en python, int(enteros) y float (decimales)")
entero = 23
print(type(entero))
decimal = 23.1
print(type(decimal))
#%%%
print(type(23.))

#*****************************#
print("Podemos convertir números a decimales fácilmente")
print(type(str(entero)))
print("dos + "+ str(decimal))
#%%%
print("Tambien podemos usar numeros en interpolacion de strings")
nombre = "Manuel"
ciudad = "Murcia"
edad = 33
print(f"Hola, me llamo {nombre}, soy de {ciudad} y tengo {edad} años")
#%%%
print("de igual forma, podemos convertir strings a números")
numero_string = "24"
print(int(numero_string)+5)
print(float(numero_string)+5)
#%%%%
print("Hay que asegurarse de que sena números validos")
numero_string_invalido = "24.5" #decimales con punto, coma error
print(float(numero_string_invalido))
#%%%
print("de igual forma, no podemos convertir un string float a un entero")
#print(int("24.1")) nota descomentar para probar punto anterior
#%%

#**********************************************#
#OPERACIONES BÁSICAS
#**********************************************#

#Podemos usar los simbolos básicos de aritmetica para relaizar operaciones
print("OPERACIONES BÁSICAS")
#suma
print("2+2=",2+2)
#resta
print("4-9=",4-9)
#multiplicación
print("3*2=",3*2)
#division
print("7/2=",7/2)
#%%
#*********************************#
#Aparte, tenemos operaciones que podemos hacer
print("#################################")
print("Otras Operaciones")
a = 7
b = 2
#multiplo inferior, realizar la división eliminado el resto
print(f"{a}//{b}=",a//b)
#modulo, realiza una división y quedarse solo con el resto
print(f"{a}%{b}=", a%b)
#negación, cambiar de sentido un valor
print(f"negacion de {a}=", -a)
#potencias, elevar al cuadrado, al cubo, etc.
print(f"{a}**{b}=",a**b)
#%%%
####################################
#BOOLEANOS
############################
print("#################################")
print("Boleanos")

#Una variable boolena es aquella que solo pude ser verdadera o falsa

verdadero = True
falso = False

print(type(verdadero))
print(type(falso))
#%%
######################################
#Como tipo de primitiva especial, tenemos None, que es la variable nula.
print("##################################")
print("Primitiva especial None")

nulo = None
print(type(nulo))
#%%
#Cualquier tipo de variable se puede convertir a booleano, trasformandose en True
print(bool("papa"))

#0 se transforma en False
print(bool(0))

#salvo None se convierte a False
print(bool(nulo))
#%%
###############################################
#COMPARACIONES LÓGICAS
####################################
#Podemos hacer comparaciones entre variables, el resultado de estas comparaciones siempre es una variable booleana
print("##########################")
print("COMPARACIONES LOGICAS")
a = 7
b = 2

# a mayor o igual a b
print(f"{a}>{b}",a>b)
# b menor o igual a a
print(f"{b}<{a}",b<=a)
# b es igual a 2
print(f"{b}=2",b==2)
# podemos obtener el opuesto de un resultado logico con not
print(f"not {a}!=23", not a !=23)
# podemos evaluar que varias condiciones se cumplen en and
print(f"{a}!=23 and {a}>{b}",a !=23 and a>b)
#podemos usar or para evaluar si se cumple una condicion u otra
print(f"{a}!=23 or {b}>={a}", a != 23 and b<= a)


###################################
#Para comparar si algo es verdadero o flaso, no usamos "==", sino que usamos "is"

print("verdadero is True=", verdadero is True)
