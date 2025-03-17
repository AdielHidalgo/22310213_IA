#En este programa se utilizaran las tuplas
#Tupla: son como las listas, pero se escriben entre (),
#las tuplas son inmutables, no se pueden modificar.
#En las tuplas no funcionan los comandos para modificar los datos


lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = ('rojo', 'azul', 'verde', 'amarillo')

print("Esto es una Tupla: ",tupla)
print("Esto es una Lista:",lista)

#Ejemplo de concatenacion en tuplas
tuplaCombi = (10, 15, 20, 'El resultado de la operación es:')
print(tuplaCombi[3], tuplaCombi[2] + tuplaCombi[0] * tuplaCombi[1] / tuplaCombi[0])

