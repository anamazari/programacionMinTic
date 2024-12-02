edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Ingresa gratis")
elif edad >= 4 and edad <= 18:
    print("Debe pagar $5000")
else:
    edad > 18
    print("Debe pagar $10000")
