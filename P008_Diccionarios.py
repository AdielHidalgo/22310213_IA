#Diccionarios
#los diccionarios son los objetos en la POO, se trata de listas desordenadas, modificables

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99\n'
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