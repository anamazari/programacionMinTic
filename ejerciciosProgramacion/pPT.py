ines = input("Ingrese Ines: piedra, papel o tijera")
juan = input("Ingrese Juan: piedra, papel o tijera")

if ines == juan:
    print("Empataron")
elif ines == "piedra" and juan == "papel":
    print("Ganó Juan")
elif ines == "piedra" and juan == "tijera":
    print("Ganó Inés")
elif ines == "papel" and juan == "piedra":
    print("Ganó Inés")
elif ines == "papel" and juan == "tijera":
    print("Ganó Juan")
elif ines == "tijera" and juan == "piedra":
    print("Ganó Juan")
elif ines == "tijera" and juan == "papel":
    print("Ganó Inés")
else:
    print("Opción incorrecta")