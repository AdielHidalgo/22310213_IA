#Bucle WHILE
"""
x = 1
while x <= 10:
    print(x)
    x += 1

#1.- Bucle infinito controlado
frase = "Lo que escribas, lo repito:"
frase += "\nIntroduce el comando 'salir' para finalizar el programa. \n"

mensaje = ""

while mensaje != "salir":
    mensaje= input(frase)
    print(mensaje)

print("Se ha salido del bucle.")

# 2.- Bucle while con condicion if
x = 1

while x <= 10:
	print(x)
#interrumpe el ciclo while aunque este no se haya cumplido en su totalida
	if x == 5:
		break
	x += 1
"""
x = 0

while x < 10:
	x += 1
#No considera los numeros 5 y 7 
	if x == 5 or x == 7:
		continue
	print(x)