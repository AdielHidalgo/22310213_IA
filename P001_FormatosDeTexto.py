#En este programa se explican los formatos de texto para nuestros strings
#String: es una cadena de caracteres
#Para definir las variables en phyton no se requiere determinar el tamaño solo se asigna el nombre de la variable y el valor


#En este programa se explican los formatos de texto para nuestros strings
#title()= pone en mayuscula la primera letra de cada palabra
#upper()= tranforma en mayusculas todo el string
#lower()= tranforma en minusculas todo el string
#\n sirve para dar un salto de linea
#\t sirve para aplicar un tabulador

Frase="mi perro se comió un lonche de un niño \n"
# se fuede definir asi 
#Frase=Frase.title() ó dentro del print
print(Frase.title())

Frase2="cuando yo iba por la calle una ancianita se cayó y grito: '¡Ay se me movió el piso!'\n"
print(Frase2.upper())

Frase3='A DOÑA DOLORES ESTA MAÑANA LE DOLIA LA PANZA\n'
print(Frase3.lower())

Frase4="Estos fueron los ganadores de los premios:\n\tJuan \n\tJonathan\n\tMaria"
print(Frase4)

Nombre="Adiel "
Apellidos="Hidalgo Ipiña"
Alumno='Datos del Alumno:\n'+"\n\t"+ Nombre + Apellidos
print(Alumno)