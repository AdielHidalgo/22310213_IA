#En este programa se utilizaran las tuplas
#Tupla: son como las listas, pero se escriben entre (),
#las tuplas son inmutables, no se pueden modificar.
#En las tuplas no funcionan los comandos para modificar los datos

# 1.- crear y manipular tupla
"""
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = ('rojo', 'azul', 'verde', 'amarillo')

print("Esto es una Tupla: ",tupla)
print("Esto es una Lista:",lista)

#Ejemplo de concatenacion en tuplas
tuplaCombi = (10, 15, 20, 'El resultado de la operación es:')
print(tuplaCombi[3], tuplaCombi[2] + tuplaCombi[0] * tuplaCombi[1] / tuplaCombi[0])
"""
# 2.- Conversion de lista a tupla y viceversa
lista = ['Maria', 'Lourdes', 1 , 5]
#lo que hace es que los valores de la lista las guarda en una tupla
tupla = tuple(lista)
print(tupla)

tupla2 = ('rojo', 'azul', 'verde', 'amarillo')
#lo que hace es que los valores de la lista las guarda en una lista
lista2 = list(tupla2)
print(lista2)

"""
También podemos utilizar el método type() para saber el tipo de dato que es algo en Python:
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = tuple(lista)
print(type(tupla))
~~Resultado class 'tuple'~~
tupla = ('rojo', 'azul', 'verde', 'amarillo')
lista = list(tupla)
print(type(lista))
~~Resultado class 'list'~~
"""
