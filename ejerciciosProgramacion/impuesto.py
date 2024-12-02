edad = int(input("Por favor ingrese su edad: "))
ingresos = int(input("Por favor ingrese sus ingresos: "))

if edad >= 18 and ingresos >= 3000000:
    print("Usted debe tributar")
else:
    print("Usted no debe tributar")