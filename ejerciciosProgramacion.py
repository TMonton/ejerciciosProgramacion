# 1. Realice un programa que solicite dos letras ingresadas por el usuario y
# verifique si son iguales o no, mostrando un mensaje.

"""letra1 = (input("Ingrese la primer letra: "))
letra2 = (input("Ingrese la segunda letra: "))

if (letra1 == letra2):
    print ("Las letras ingresadas son iguales!")
else:
    print("Las lestras ingresadas son diferentes!")"""
    
# 2. Hacer un programa que permita decidir si dos palabras son iguales o
# diferentes. Mostrar mensaje por pantalla.
"""palabra1 = input("Ingrese primer palabra: ")
palabra2 = input("Ingrese segunda palabra: ")

if palabra1 == palabra2:
    print ("Son iguales")
else:
    print ("son palabras diferentes.")"""
    
# 3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota
# en mesa femenina o masculina.

"""sexo1 = input("Ingrese la inicial de su sexo en mayuscula: ") 
if sexo1 == "F":
    print("Usted vota en mesa femenina.")
elif sexo1 == "M":
    print("Usted vota en mesa masculina.")
else:
    print("Usted no puede votar")"""
    
# 4. Realice un programa que lea dos números y diga cuál es el mayor.

"""numero1 = 5
numero2 = -5 

if numero1 > numero2:
    print(numero1, "Es el número más grande.")
else:
    print(numero2, "Es el número más grande.")"""
    
# 5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
# el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
# de cambio quiere, si de dólares a pesos o viceversa.

"""dolar_esta = 1055
dolar_o_peso = input("Ingrese si quiere dolares o pesos: ")


if dolar_o_peso == "dolares":
    ingrese = int(input( "Ingrese cuantos pesos a dolares desea cambiar: "))
    conversion = ingrese / dolar_esta
    print ("Usted compró", conversion, "dolares")
    
elif dolar_o_peso == "pesos":
   ingrese2 = int(input("Ingrese la cantidad de dolares a pesos que desea cambiar: "))
   conversion2 = ingrese2 * dolar_esta
   print("Usted compró",conversion2, "pesos")
    
else:
    print("No existe la ese cambio")"""
    
# 6. Realice un programa donde el usuario ingrese su edad. Si es mayor de
# 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
    
"""edad = int(input("Ingrese su edad: "))
if edad > 16:
    print("Usted puede votar")
else:
    print ("Usted no puede votar")"""


#Ejercicios estructura condicional compuesto (IF anidados).


# 1. Introducir los lados de un triángulo y visualizar por pantalla si dicho
# triángulo es equilátero, isósceles o escaleno.
    
"""l1 = input("Ingresar valor del lado: ")
l2 = input("Ingresar valor del lado: ")
l3 = input("Ingresar valor del lado: ")

if l1 == l2 == l3: 
    print ("El triangulo es equilatero")
elif (l1 == l2 or l1 == l3 or l2 == l3):
    print ("El triangulo es isóceles")
else:
    print ("El triangulo es escaleno")"""
    
# 2. Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.

"""importe = int(input("Ingresar el importe: "))
forma_pago = str(input("Ingrese forma de pago, contado, tarjeta, débito: "))

if forma_pago == "contado":
    importe1 = importe - importe / 100 * 10
    print (f"El precio con el 10% de descuento es ${importe1}")
elif forma_pago == "tarjeta":
    importe2 = importe + importe / 100 * 10
    print (f"El precio con un 10% incluido es ${importe2}")
elif forma_pago == "débito":
    importe3 = importe - importe / 100 * 5
    print (f"El precio con el 5% de descuento es ${importe3}")"""
    

# 3. Realice un programa que lea tres números, muestre cuál es el mayor y
# determine si es par o impar.

"""num1 = 8
num2 = 11
num3 = 5

if (num1 > num2) and (num1 > num3):
    print (num1, "Es el mayor de los tres")
    if num1 % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
elif (num2 > num1) and (num2 > num3): 
    print (num2, "Es el mayor de los tres")
    if num2 % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
elif (num3 > num1) and (num3 > num2):
    print (num3, "Es el mayor de los tres")
    if num3 % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")"""

# 4. Confeccione un programa que pida un número del 1 al 7 y diga el día de
# la semana correspondiente.

"""diadelasemana =  int(input("Ingrese el número de la semana del 1 al 7: "))

if diadelasemana == 1:
    print ("Hoy es Domingo ")
elif diadelasemana == 2:
    print ("Hoy es Lunes ")
elif diadelasemana == 3:
    print ("Hoy es Martes ")
elif diadelasemana == 4:
    print ("Hoy es Miercoles ")
elif diadelasemana == 5:
    print ("Hoy es Jueves ")
elif diadelasemana == 6:
    print ("Hoy es viernes ")
elif diadelasemana == 7:
    print ("Hoy es Sábado ")"""
    
# 5. Realice un programa que pida un número del 1 al 12 y diga el nombre
# del mes correspondiente.

"""mesdelaño =  int(input("Ingrese el número del mes del año (Del 1 al 12): "))

if mesdelaño == 1:
    print ("Este mes es Enero ")
elif mesdelaño == 2:
    print ("Este mes es Febrero ")
elif mesdelaño == 3:
    print ("Este mes es Marzo ")
elif mesdelaño == 4:
    print ("Este mes es Abril ")
elif mesdelaño == 5:
    print ("Este mes es Mayo ")
elif mesdelaño == 6:
    print ("Este mes es Junio ")
elif mesdelaño == 7:
    print ("Este mes es Julio ")
elif mesdelaño == 8:
    print ("Este mes es Agosto ")
elif mesdelaño == 9:
    print ("Este mes es Septiembre ")
elif mesdelaño == 10:
    print ("Este mes es Octubre ")
elif mesdelaño == 11:
    print ("Este mes es Noviembre ")
elif mesdelaño == 12:
    print ("Este mes es Diciembre ")"""



    

   
    

    


    


    
   
    

    






