# Un programa que pide al usuario que ingrese un nombre de archivo y lo abre
# Vulnerabilidad: inyección de comandos
nombre = input("Ingrese el nombre del archivo: ")
archivo = open(nombre, "r")
contenido = archivo.read()
print("El contenido del archivo es:")
print(contenido)
archivo.close()

# Un programa que carga y analiza un archivo XML externo
# Vulnerabilidad: ataque de billones de risas
import xml.etree.ElementTree as ET
url = input("Ingrese la URL del archivo XML: ")
arbol = ET.parse(url)
raiz = arbol.getroot()
print("La raíz del archivo XML es:")
print(raiz.tag)

# Un programa que usa una expresión regular para validar un correo electrónico
# Vulnerabilidad: ataque de ReDoS
import re
email = input("Ingrese su correo electrónico: ")
patron = r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"
if re.match(patron, email):
    print("El correo electrónico es válido")
else:
    print("El correo electrónico no es válido")

# Un programa que usa pickle para deserializar un objeto
# Vulnerabilidad: ejecución de código arbitrario
import pickle
objeto = input("Ingrese el objeto serializado: ")
objeto = pickle.loads(objeto)
print("El objeto deserializado es:")
print(objeto)

# Un programa que usa eval para evaluar una expresión matemática
# Vulnerabilidad: ejecución de código arbitrario
expresion = input("Ingrese una expresión matemática: ")
resultado = eval(expresion)
print("El resultado de la expresión es:")
print(resultado)
