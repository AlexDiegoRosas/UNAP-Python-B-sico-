#Aqui se explican los principale métodos de control de flujo
#@author Alex

#################################
# IF - ELSE
#################################

#Usamos if-else para tomar desciciones y ejecutar distintas partes del código
#en funcion de una condición

#NOTA: en python, la manera de indicar si estamos dentro de un bucle 
#(o una funcion) es mediante el identado es decir poniendo 4 espacios delante
#del código [en spyder pulsar la tecla tabulador inserta 4 espacios automaticamente
#%%
#La manera mas sencilla de implementar una evaluación logica es con un if

temperatura = 25

if temperatura <=25:
	#El código se identa 4 espacios para indicar que estamos dentro del if
	print("Ponte una rebequita que refresca")
#%%
#Si queremos tomar distintas condiciones en funcion de una condicion
#otra ocurra podemos usar if - else

temperatura = 15

if temperatura <=10:
	respuesta_abuela = "�Ponte un abrigo, que hace frio y te vas a resfriar"
elif temperatura <=20:
	respuesta_abuela = "�Ponte una rebequita que refresca!"
elif temperatura <=30:
	respuesta_abuela = "Nenico no vuelvas muy tarde �eh?"
else:
	respuesta_abuela = "�ve por la sombra que hace calor!"
print(respuesta_abuela)
#%%
#Tambien se pueden insertar ifs dentro de otros ifs (esto se llama nestear)

temperatura = 25
lluvia = False

if 20 < temperatura <30:
	if not lluvia:
		#True evalua a True, usando not obtenemos el opuesto
		print("�Vamos de picnic!")
#%%
################################
#BUCLES FOR (FOR LOOPS)
################################

#Los bucles FOR sirven para iterar entre los elementos de una lista uno por uno
#o de cualquier elemento de python que soorte iteraci�n
################################

numeros = [1,2,3,4,5,6,7,80,9,10]

for numero in numeros:
    if numero <=10:
        print(f"numero valido {numero}")
    else:
        print(f"�ERROR! n�mero {numero} mayor de 10")
#%%
#Hay veces que queremos romper un bucle for si ocurre una condici�n, podemos romper
#el loop con break

numeros = [1,2,3,4,5,6,7,80,9,10]

for numero in numeros:
    if numero <=10:
        print(f"numero valido {numero}")
    else:
        print(f"¡ERROR! numero {numero} mayor de 10, SALIENDO DEL BUCLE")
        break
#%%
#Hay veces que en vez de romper el loop, simplemente no hacer nada
# en una iteracion en concreto, para eso podemos usar pass

numeros = [1,2,3,4,5,6,7,80,9,10]

for numero in numeros:
    if numero <10:
        print(f"numero valido {numero}")
    else:
        #pass se usa simplemente en aquellos casos en los que ha y que poner
        #algo en un segmento del codgio, pero no hace nada.
        pass
#%%
#Continue al contrario de pass, nos lleva directamente a la siguiente iteraci�n
#del bucle

numero = [1,2,3,4,5,6,7,80,9,10]

for numero in numeros:
    if numero <=10:
        print(f"nmero valido {numero}")
    else:
        continue
        print("Esto no se va a imprimir")
#%%
#Hay una foma mas simplificada de iterar los elementos de una lista
a = [numero for numero in numeros if numero < 10]
#%%
inventario = {
    "melocotones": 3,
    "fresas": 1,
    "manzanas": 4
    }
#Podemos iterar las claves de un diccionario cn un for
for fruta in inventario:
    print(fruta)
#%%
#Podemos iterar las claves y los valores de un diccionario a la vez en un bucle for usando items()
for fruta, cantidad in inventario.items():
    print("Tenemos {} kilos/s de {} ". format(cantidad, fruta))
#%%
#No solo las listas sin iterable (es decir , soportan bucles for ), los strings tambien:

nombre = "MURCIA"

for letra in nombre:
    print("Dame una {}: ".format(letra))
#%%
#######################
#TRY EXCEPT
#######################
#En ocaciones los programas fallan lanzando una excepci�n, pero una manera de poder hacer que un programa
#continue su funcionamiento pese haber fallado es "atrapando" la excepcion.
#En python esto se hace mediante el bloque try-except


#IMPORTANTE: Siempre que atrapamos una excepci�n, es importante por lo menos imprimir el mensaje de error
#Asi nos aseguramos de nuestro programa no est� fallando catastroficamente sin que nos demos cuenta.

numero_str = "10.5"

try:
    #d