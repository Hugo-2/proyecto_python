# Importar el módulo pyodbc
import pyodbc

# Establecer el string de conexión con la base de datos
# Se debe cambiar el driver, el server, el database, el user y el password según corresponda
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=ejemplo;'
    r'UID=usuario;'
    r'PWD=contraseña;'
    )

# Conectar con la base de datos usando el string de conexión
conn = pyodbc.connect(conn_str)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Pedir al usuario que ingrese su usuario y contraseña
user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

# Crear una consulta SQL que busque al usuario y la contraseña en la tabla de usuarios
# Se debe cambiar el nombre de la tabla y los campos según corresponda
sql = "SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?"

# Ejecutar la consulta SQL usando el cursor y pasando el usuario y la contraseña como parámetros
# Esto evita la inyección SQL
cursor.execute(sql, user, password)

# Obtener los resultados de la consulta SQL
results = cursor.fetchall()

# Comprobar si hay algún registro que coincida con el usuario y la contraseña
if results:
    # El usuario y la contraseña son correctos
    print("Bienvenido", user)
else:
    # El usuario y la contraseña son incorrectos o no existen
    print("Usuario o contraseña inválidos")

# Cerrar el cursor y la conexión con la base de datos
cursor.close()
conn.close()
