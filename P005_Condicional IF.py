#CONDICIONAL "IF"
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que
# == igual que
# != diferente que
# and operacion logica y
# or operacion logica ó 
"""
num1 = 1450
num2 = 60

if num1 != num2:
	print('Se ejecuta el if.')
if num1 == num2:
	print('Se ejecuta el if.')
if num1  num2:
	print('Se ejecuta el if.')

#condicion if- else
print("Toñito quiere comprar unos tenis de $250")
Toñito=250
print("Toñito tiene: $",Toñito)
if Toñito >=250:
    print("Toñito puede comprar los tenis, trae con queso")
else:
    print("Toñito no puede comprar los tenis,anda pobre")
"""
#condicion elif y entrada de datos
print("Estas en una tienda y estas pensando comprar unas papitas $20, una coca $25, unos chicles $2 y las tortillas $24")
Dinero = int(input("Dime con cuanta feria cuentas:  "))
if Dinero >= 20 and Dinero<25:
    print("Puedes comprar unas papitas")
elif Dinero >= 2 and Dinero<20:
    print("Puedes comprar unos chicles")
elif Dinero >= 24 and Dinero<=25:
    print("Puedes comprar una coca o las tortillas")
elif Dinero >= 71:
    print("Genial traes billete pa llevarte lo que estas pensando")
else:
    print("Sorry no te ajusta, regresa cuando traigas feria suficiente")



