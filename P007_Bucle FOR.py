#BUCLE "FOR"

# 1.- 

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