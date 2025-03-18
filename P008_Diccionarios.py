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

#EJERCICIO DE VIDEO #48
#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print(). El resultado será esto en la consola:
#Resultado: El modelo Corsair K55 RGB cuesta 59,99 $.
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99$'}
print("El modelo",teclado2['Modelo'],"cuesta",teclado2['Precio'])
"""
## 2.- Diccionarios con bucle for
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
Precio = 89,99. 

for x,y in teclado1.items():
    print(x,"=",y+".")
"""

# 3.- Metodos en los diccionarios
"""
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99',
    "ID" : "001"
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
"""
# ~len~ sirve para mostrar la cantidad de elementos en un diccionario, tambien se puede sumar
#print(len(teclado1)+len(teclado2))

# ~pop~ para eliminar un elemento del diccionario
#teclado1.pop("Categoría")
#print(teclado1)

# ~del~ sirve para eliminar elementos del diccionario o hasta el mismo diccionario
#del teclado1['Precio']
#print(teclado1)
#del teclado1 "Elimina todo el diccionario"
#print(teclado1) "Arroja errores porque no lo detecto"

# ~clear~ limpia un diccionador mas no lo elimina solo deja los {} vacios
#teclado1.clear()
#print(teclado1)

#Se pueden modificar los datos del diccionario, tambien se pueden añadir elementos o categorias
#teclado1['Precio'] = "85"
#teclado1["color"] = "Negro"
#print(teclado1)

# ~copy~ realiza una copia de un diccionario
#tecladoCopia = teclado1.copy()
#print(tecladoCopia)

# ~dict~ tambien se puede usar para copiar un diccionario
#tecladoCopia = dict(teclado1)
#print(tecladoCopia)
#"Tambiens se puede usar para crear nuevos diccionarios"
#teclado3 = dict(Categoría = "teclados",
#                Modelo = "Razer Cynosa Chroma",
#                 Precio = "59.99" )
#print(teclado3)

#~dict.frontkeys, para autogenerar valores repetitivos
#teclado3 = ("Categoría","Modelo","Precio")
#teclado3= dict.fromkeys(teclado3,"Vacío") #muestra las categorias del diccionario pero sin sus elementos y los muestra como "vacio"
#print(teclado3)

# ~keys~ para mostrar las categorias sin los elementos
#vistaTeclado = teclado1.keys()
#print(vistaTeclado)

# ~update~ para añadir elementos al diccionario
#teclado1.update({"color" : "Negro"})
#print(teclado1)

#Se puede realizar busqueda en un diccionario con un if
"""
if "ID" in teclado2:
    print("El producto tiene un ID especificado.")
else:
    print("El producto no tiene un ID especificado. Por favor, introduce un ID")
"""
# Se puede anidar diccionarios dentro de un diccionario
"""
teclados = {
"teclado1" : {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99',
    "ID" : "001"
},

"teclado2" : {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
    }
}
print(teclados)
"""
###Ejercicio del video #50
#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99',
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
teclado2.pop("Precio")
#print(teclado1)
print(teclado2)