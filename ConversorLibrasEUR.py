# Tasas de cambio
dolar_euro = 0.91
libra_euro = 1.18
 
# Mensaje de bienvenida
titulo = "Bienvenido al conversor de divisas"
 
# Mostrar opciones que puede elegir el usuario
print(titulo)
opcion = input("¿Qué desea convertir?\n"
               "A - de dólar a euro\n"
               "B - de euro a dólar\n"
               "C - de libra a euro\n"
               "D - de euro a libra\n")
 
# Convertir la selección del usuario a mayúsculas para hacerla insensible a mayúsculas y minúsculas
opcion = opcion.upper()
 
# Dependiendo de la información proporcionada, cambiarán los valores
if opcion == "A":
    cantidad_dolares = float(input("Introduzca la cantidad de dólares: "))
    print("La cantidad de dólares en euros es: {}".format(cantidad_dolares * dolar_euro))
elif opcion == "B":
    cantidad_euros = float(input("Introduzca la cantidad de euros: "))
    print("La cantidad de euros en dólares es: {}".format(cantidad_euros / dolar_euro))
elif opcion == "C":
    cantidad_libras = float(input("Introduzca la cantidad de libras: "))
    print("La cantidad de libras en euros es: {}".format(cantidad_libras * libra_euro))
elif opcion == "D":
    cantidad_euros = float(input("Introduzca la cantidad de euros: "))
    print("La cantidad de euros en libras es: {}".format(cantidad_euros / libra_euro))
else:
    print("Opción no válida")