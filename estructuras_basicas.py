#Aqui se explican los principales tipos de estructuras de datos
#@author: Alex

#Las estructuras de datos son aquellos objetos que se usan para almacenar información.
#Hay muchos tipos, pero estos son los básicos en Python

#############################
#LISTAS
#############################
#las listas son conjuntos de elementos ordenados donde cada elemento tiene una posisción.

frutas = ["naranja", "manzana", "pera", "fresa"]
print(frutas)
print(type(frutas))

##########################
#Accedemos a los elementos de una lista con []
#El indice de los elementos de una lista empieza en 0, eso quiere decir
#que el primer elemento se accede con [0]
print(frutas[0])
#######
#Podemos accder a un rango de elementos de una lista con [inicio:final-1:orden]
print(frutas[:2])
#accedemos a los elementos desde el 2 hasta el final
print(frutas[2:])
#Poedmos acceder a los elementos empezando por el final accediendo a la lista con numeros negativos
#Por ejemplo, accedemos a los ultimos de elementos

print(frutas[-2:])
#Podemos saltarnos elementos de n en n usando [::n], por ejemplo, si solo queremos
#los elementos impares
print(frutas[::2])
#si el orden es un numero negativo nos devolverá la lista en sentido inverso
print(frutas[::-1])
#podemos añadir elementos a listas con append. Esto modifica la lista original
frutas.append("melon")
print(frutas)
#podemos repetir una lista multiplicandola por un entero
print(frutas * 2)
#podemos concatenar listas con el simbolo +
ciudades = ["Murcia", "Cartagena"]
print(frutas + ciudades)#Prints concatenated lista

#Podemos modificar elementos de una lista 
frutas[0] = "mango"
print(frutas)
#Podemos alargar la lista sin importar el tamaño inicial
frutas[3:] = ["uva", "higo", "sandia", "pomelo"]
print(frutas)

#Podemos evaluar si un elemento existe en una lista 
print(frutas)
print("uva" in frutas)
print("patata" in frutas)

#podemos buscar la posición de un elemento en una lista

frutas = ["naranja", "manzana", "pera", "fresa"]
print(frutas)
print("Posición en la lista de la palabra pera es {}".format(frutas.index("pera")))

#Podemos eliminar un elemento en una posición concreta con pop
frutas.pop(2)
print(frutas)

#combinando index y pop podemos eliminar un elemento en concreto
frutas.pop(frutas.index("naranja"))
print(frutas)
#las listas se pueden ordenar con el metodo sort()
edades = [23,33,10,54,65,34,25]
edades.sort()
print(edades)

#poedemos generar listas de numeros con la funcion range()
print(list(range(10)))

#Los strings se pueden acceder de forma similar a las listas 
nombre = "Murcia"
print(nombre[0])
print(nombre[2:])


######################################
#TUPLAS (TUPLES)
#####################################

#lAS TUPLAS SON VERSIONES DE LAS LISTAS QUE NO SE PUEDE MODIFICAR 

mosqueteros = ("Athos", "Porthos", "Aramis")
print(type(mosqueteros))
print(mosqueteros)

#Podemos acceder a los elemtos de una tupla de igual forma que una lista 
print(mosqueteros[2:])
#sin embargo, no podemos modificarla 
#mosqueteros[3] = "D'artagnan" # decomentar para probar punto de inmodificabilidad de tuplas
##############################################
#Diccionarios
####################
#los diccionarios son un conjuto de claves (keys) asociadas a valores (values).
#sabineod una clave podemos encontrar el valor de dicha clave

inventario = {
	"melocotones": 3,
	"fresas": 1,
	"manzanas":4 
}
print(type(inventario))
print(inventario)

################
#pode¿mos ver las claves que tiene un diccionario con el metodo keys()
print(inventario.keys())
#el metodo .keys() no devuelve una lista, si queremos acceder a las claves como 
#una lista tenemos que convertirlas a una 
#print(inventario.keys()[0])# no debuelve lista error 
print(list(inventario.keys())[0])

#podemos ver los valores de un diccionario con el metodo values()
print(inventario.values())

#accedemos a los elemtos de un diccionario con []
print(inventario["fresas"])
#si la clave buscada no existe nos dará un error KeyError)
#print(inventario["melon"])


#podemos evaluar si una clave existe en un diccionario facilmente
print("melon" in inventario)
print("melocotones" in inventario)

#podemos eliminar una clave en un diccionario con pop()
kilos_fresas = inventario.pop("fresas")
print("tenemos {} kilos de fresas". format(kilos_fresas))
print(inventario)

#cada tipo de estructura de datos puede almacenar los otros!

#una lista con listas dentro
lista_trayectos = [
		["Murcia", "Valencia"],
		["Murcia", "Alicante"],
		["Albacete", "Valencia"],
		["Albacete", "Granada"]
		]
print(lista_trayectos[1][1])

#un diccionario con tuplas como valores
dict_trayectos = {
	"Murcia": ("Valencia", "Alicante"),
	"Albacete": ("Valencia", "Granada")
}
print(dict_trayectos["Murcia"])

#una lista que contiene diccionarios
lista_diccionarios = [
		{"origen": "Murcia", "destino": "Alicante"},
		{"origen": "Albacete", "destino": "Granada"}
]
print(lista_diccionarios)