lista_productos =["jabón", "queso", "atun"]

for producto in lista_productos:
    if producto == "queso":
        print("No me gusta el queso")
    else:
        print(producto)

lista_numeros = [9, 5, -3]

for numero in lista_numeros:
    if numero < 0:
        print("Número negativo")
        lista_numeros.append(3)

print(lista_numeros)