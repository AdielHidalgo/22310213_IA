#Diccionarios
#los diccionarios son los objetos en la POO, se trata de listas desordenadas, modificables

# 1.- Estructuta de un Diccionario
"""
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
muestraTeclado= dict(teclado2) #se crea una nueva variable pero el "dict" hace mencion que esa variable almacena un diccionario
consulta = teclado1['Modelo'],teclado1['Categoría']
print(consulta)
print(muestraTeclado)

#EJERCICIO DE VIDEO
#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print(). El resultado será esto en la consola:
#Resultado: El modelo Corsair K55 RGB cuesta 59,99 $.
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99$'}
print("El modelo",teclado2['Modelo'],"cuesta",teclado2['Precio'])
"""
## 2.- Diccionarios con bucle for

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
"""
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

#para mostrar tanto el valor como tipo, se coloca dos variables x y y en el contador
#El *items* sirve para mostrar todo lo que esta dentro del diccionario
for x,y in teclado1.items():
    print(x,":",y)
for x,y in teclado2.items():
    print(x,":",y)
#tambien se puede utilizar *values*, solo para mostrar los valores sin el concepto
for x in teclado1.values():
    print(x)
for x in teclado2.values():
    print(x)
#Otra forma de mostrar los valores es:
for x in teclado1:
    print(teclado1[x])
for x in teclado2:
    print(teclado2[x])
#sí no colocanos items o values, solo muestra los conceptos dentro del diccionario
for x in teclado1:
    print(x)
for x in teclado2:
    print(x)
#Se puede modificar un valor de un concepto del diccionario
teclado1['Precio'] = '85'
print(teclado1['Precio']) #otra forma de escribirlo y obtener el valor es: print(teclado1.get('Precio'))
"""
### Ejercicio de capitulo #49
#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
#Resultado:
"""
Categoría = Teclados.
Modelo = HyperX Alloy FPS Pro.
Precio = 89,99. """

for x,y in teclado1.items():
    print(x,"=",y+".")