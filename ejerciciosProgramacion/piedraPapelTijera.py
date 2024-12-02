print("Vamos a jugar piedra, papel o tijera")

print (" a. Ines b. Juan")
nombre = input("Elija su jugador Ines o Juan: ")
nombre1 = "Ines"
nombre2 = "Juan"

posicion1 = "Piedra"
pocicion2 = "Papel"
posicion3 = "Tijeras"


if nombre1 == "a":
    print("Jugará como Ines")
elif nombre == "b":
    print("Jugará como Juan")
elif nombre == "a" and posicion == "w":
    print("Ines escogió Piedra")
elif nombre == "b" and posicion == "w":
    print("Juan escogió Piedra") 
