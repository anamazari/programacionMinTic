#función que me muestra o imprime algo
def saludar(nombre):
    print("Hola, ", nombre)

saludar("Ana")

#función retorna un valor (recibe un resultado) siempre devuelve algo
def sumar(a, b):
    return a + b

resultado = sumar(3, 5) # debo crear una variable para guardar el return (resultado)
print("El resultado es:", resultado)

#función dinámica
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número: "))

def sumar(num1, num2):     # def sumar(a + b)
    return num1 + num2     #    return a + b

resultado = sumar(num1, num2)
print("El resultado de la suma es: ", resultado)

#funciones con condiciones:
def sumar(a,b):
    if a == 0:
        a=1
    return a+b