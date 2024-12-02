contrasena = input("Ingrese una contraseña: ")
confirmacion = input("Confirme la contraseña: ")
while contrasena != confirmacion:
    print("Contraseñas no coinciden, por favor validar")
    contrasena = input("Ingrese una contraseña: ")
    confirmacion = input("Confirme la contraseña: ")
print("Programa finalizado")