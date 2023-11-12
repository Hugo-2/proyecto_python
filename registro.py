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

# Pedir al cliente que ingrese sus datos personales
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dni = input("Ingrese su DNI: ")
email = input("Ingrese su email: ")

# Crear una consulta SQL que inserte los datos del cliente en la tabla de clientes
# Se debe cambiar el nombre de la tabla y los campos según corresponda
sql_insert = "INSERT INTO clientes (nombre, apellido, dni, email) VALUES (?, ?, ?, ?)"

# Ejecutar la consulta SQL usando el cursor y pasando los datos del cliente como parámetros
# Esto evita la inyección SQL
cursor.execute(sql_insert, nombre, apellido, dni, email)

# Guardar los cambios en la base de datos
conn.commit()

# Crear una consulta SQL que busque el nivel de privilegio del cliente en la tabla de privilegios
# Se debe cambiar el nombre de la tabla y los campos según corresponda
sql_select = "SELECT nivel FROM privilegios WHERE dni = ?"

# Ejecutar la consulta SQL usando el cursor y pasando el DNI del cliente como parámetro
cursor.execute(sql_select, dni)

# Obtener el resultado de la consulta SQL
result = cursor.fetchone()

# Comprobar si hay algún registro que coincida con el DNI del cliente
if result:
    # Obtener el nivel de privilegio del cliente
    nivel = result[0]

    # Comprobar si el nivel de privilegio es suficiente para realizar una operación
    # Se debe cambiar el valor mínimo según el criterio deseado
    if nivel >= 3:
        # El cliente tiene permiso para realizar la operación
        print("El cliente", nombre, apellido, "tiene permiso para realizar la operación.")
    else:
        # El cliente no tiene permiso para realizar la operación
        print("El cliente", nombre, apellido, "no tiene permiso para realizar la operación.")
else:
    # El cliente no tiene ningún registro de privilegio
    print("El cliente", nombre, apellido, "no tiene ningún registro de privilegio.")

# Cerrar el cursor y la conexión con la base de datos
cursor.close()
conn.close()
