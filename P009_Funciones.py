###Funciones###
#Es un bloque de codigo que solo se ejecuta cuando lo llamemos, y lo podemos llamar cuantas veces sean necesarias
# 1.- Introduccion a la funciones (crear y llamar funciones)
"""
def saluda():
    print("Hola, En este programa vamos a aprender a realizar funciones")
saluda()

print("La familia Simpson\n")
#Nombre y parentesco son los argumentos que se tienen que definir cuando se llame a la funcion
def familiaS(nombre,parentesco):
    print(nombre + " Simpson-" + parentesco)

familiaS("Homer","Padre")
familiaS("Marge","Madre")
familiaS("Lisa","Hija")
familiaS("Bart","Hijo")
familiaS("Maggie","Hija")
"""
###Ejercicio #51 del tema
#Crea una función que realice una suma. Para ello, tendrás que añadir dos argumentos(numero1 y numero2).
#En su interior, especificarás un print() que muestre el resultado de la suma. 
#Deberás hacer tres llamadas que como resultado de la suma den los valores 30, 50 y 57000.
#Los números que introduzcas en la llamada pueden ser los que quieras siempre que coincidan los resultados en el print().
def Suma(num1,num2):
    print("El resultado de la suma de: ",num1,"+",num2,"=",num1+num2)
Suma(20,10)
Suma(35,15)
Suma(28500,28500)
# 2.- Cómo utilizar *args en las funciones
#se utiliza el args cuando no limitamos los argumentos y podemos definir cuantos queramos
"""
def alumnos(*args):
    print("El último alumno es: " + args[3] + " y el primero es: " + args[0] + ".")

alumnos("Andrés","Ana","Andrea","Antonio")
 
def alumnos_profesores(profesor,sustituto,*args):
    print("Profesor: " + profesor)
    print("Sustito: " + sustituto)
    for x in args:
        print("Alumno: " + x)
lista_alumnos=["Andres","Ana","Alejandro","Andrea"]

alumnos_profesores("Antonio","Amador", *lista_alumnos)
"""  
###Ejercicio #52 del tema
#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	print(len(args))

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

###Ejercicio #53 del tema
#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("Azul","Verde")

###Ejercicio #54 del tema ###
#Crea una función que realice la suma de cinco números utilizando solo *args. 
#Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().
def Suma5(*args):
	SumaS=args[0]+args[1]+args[2]+args[3]+args[4]
	print(SumaS)

Suma5(1,3,5,7,8)