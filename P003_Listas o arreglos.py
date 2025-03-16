####En este programa se va a trabajar con listas####
#~~~~  1.- Introducción a las listas ~~~~
#Un lista es una coleccion de elementos, una variable con multiples valores

Automoviles = ["Nissan",'WW','BMW','Tesla']
print(Automoviles)
#Para imprimir un solo elemento de la lista se especifica la posicion del elemento
print("\n",Automoviles[3],"\n\n\n")

#~~~ 2.- Posiciones negativas ~~~
#En una lista las posiciones negativas son las posiciones en las cuales se empiza desde el
#ultimo elemento de la lista hacia el primero.

Alumnos = ['Lupe','Ramon','Jona','Raul','Lucrecio','Armando','Josefina']

print("El último alumno de la lista es: ",Alumnos[-1])

#~~~ 3.- eliminar lista con ´del´ ~~~
numeros = [1,2,3,4,5,6,7,8,9,10]
del numeros[3]
del numeros[-1]
print(numeros)

#~~~ 4.- Eliminar elementos con ´remove´ ~~
Alumnos2 = ['Lupe','Ramon','Jona','Raul','Lucrecio','Armando','Josefina']
Alumnos2.remove("Jona")
Alumnos2.remove("Armando")
print(Alumnos2)