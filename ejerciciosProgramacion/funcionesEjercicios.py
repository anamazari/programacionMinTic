#función ejercicio división:
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número: "))

def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return("Disculpe, b el segundo numero no puede ser cero, por favor escoja otro número porque no se puede dividir entre 0")

resultado = dividir(num1, num2)
print("El resultado de la división es: ", resultado)


