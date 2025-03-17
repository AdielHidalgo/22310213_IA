#BUCLE "FOR"
"""
# 1.- Introduccion al for

#for x in "Phyton":
#    print(x)

Materias= ["Control","MAPI","Hidraulica","Vision","Mciro"]
#imprime todos los valores de las materias
#for x in Materias:
#    print(x)

#Excluye la materia que aparece en el if
#for x in Materias:
 #   if x == "MAPI":
  #      continue
   # print(x)
#Interrumpe el ciclo cuando se cumple la condicion if
for x in Materias:
    if x == "Hidraulica":
        break
    print(x)

# 2.- La funcion range() en el for

#Se le coloca un rango con inicio en 0 y incremento en 1
#for x in range(10):
 #   print(x)

#Se coloca un rango de 5-10 con incremento en 1
#for x in range(5,10):
 #   print(x)

#Se coloca un rango de 5 a 25 con incremento en 5
#for x in range(5,25,5):
 #   print(x)

#sacar los valores de una lista y que realice operaciones

print("Lista de números:\n")
numeros=[2,4,8,16,32,64,128]
for x in range(len(numeros)):
    print("Número de operación -> ",x, "Multiplicacion ->", numeros[x],"Resultados: ->", numeros[x] * numeros[x])
"""

#For anidado

num1 = ["1","2","3","4","5"]
num2 = "0"
num3= "A"
for x in num1:
    for y in num2:
        for z in num3:
            print(x + y + z)