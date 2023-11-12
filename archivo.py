# Un programa que pide al usuario que ingrese un nombre de archivo y lo abre
nombre = input("Ingrese el nombre del archivo: ")
archivo = open(nombre, "r")
contenido = archivo.read()
print("El contenido del archivo es:")
print(contenido)
archivo.close()
