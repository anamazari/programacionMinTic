# ejercicio 1:
#Escribe un programa que le pida número al usuario y le muestre si el número es par o impar

#num = int(input("Ingrese un número entero: "))

#if num % 2 == 0:
    #print("El número es par")
#else:
    #print("El número es impar")

# ejercicio 2:
#Deben crear un sistema el cual le pida al usuario 10 números, luego le muestre si el número es positivo o

#numero = int(input("Ingrese 10 números: "))
    #if numero > 0:
       #print("El número es positivo")
    #else:
        #print("El número es negativo")
   


#for i in range(10):
    #numero = int(input("Ingrese 10 números: "))
    #if numero > 0:
        #print("El número es positivo")
    #else:
        #print("El número es negativo")


# ejercicio 3:
# Crear un sistema que le pida 5 valores de producto al usuario, los productos mayores a 10000 deben 
# decirle al usuario que pague IVA, de lo contrario no debe decir nada.

#for i in range(5):
    #valorProducto = int(input("Ingrese el valor de 5 productos: "))
    #if valorProducto > 10000:
        #print("Debe pagar IVA")
    #else:
        #print(" ")

#ejercicio 4
#Crear un sistema el cual le pida al usuario su salario, si el salario es mayor a 3M debe restarle 20k al salario
#y mostrar el nuevo salario.

#salario = int(input("Por favor, ingrese su salario: "))

#if salario > 3000000:
    #nuevoSalario = salario - 20000
    #print(nuevoSalario)
#else:
    #print("Su salario queda igual")

#ejercicio 5
# Deben crear un sistema el cual pida al usuario una contraseña, si la contraseña es diferente a 1234 le va a decir
# que la contraseña es incorrecta y la volverá a pedir.

#for i in range(3):
    #contrasena = int(input("Por favor ingresar una contraseña: "))
    #if contrasena != 1234:
        #print("La contraseña es incorrecta, ingresela de nuevo por favor")
    #else:
        #print("La contraseña es correcta")


#contrasena = int(input("Por favor ingresar una contraseña: "))
#while contrasena != 1234:
    #print("La contraseña es incorrecta, ingresela de nuevo")
    #contrasena += 1

#forma correcta
contrasena = int(input("Por favor ingresar una contraseña: "))
contrasenaCorrecta = 1234

while contrasena != contrasenaCorrecta:
    print("La contraseña es incorrecta, ingresela de nuevo")
    contrasena = input("Ingrese su contrasena: ")
