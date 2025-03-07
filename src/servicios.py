import mysql.connector
from mysql.connector import Error
import time
from frames.db_config import DB_USER, DB_PASSWORD
from creadorbasededatos import CrearBaseDatos  # Importa la clase para crear la base de datos

class CreateConnection:
    def __init__(self):
        self.usuario = DB_USER
        self.contrasena = DB_PASSWORD

    def create_connection(self):
        """Create a database connection to the MySQL database"""
        try:
            connection = mysql.connector.connect(
               host='localhost',
               database='sistema_informacion_medica',
               user=self.usuario,
               password=self.contrasena
             )
            if connection.is_connected():
               return connection
        except Error as e:
            if "Unknown database" in str(e):
                # Si la base de datos no existe, intenta crearla
                creador = CrearBaseDatos()
                creador.crear_base_datos()
                # Intenta conectarse de nuevo
                try:
                    connection = mysql.connector.connect(
                        host='localhost',
                        database='sistema_informacion_medica',
                        user=self.usuario,
                        password=self.contrasena
                    )
                    if connection.is_connected():
                        return connection
                except Error:
                    pass
        except Exception:
            pass
        return None

    def check_connection(self, connection):
        """Check if the connection to the database is still active and return the result"""
        try:
            if connection.is_connected():
                return "Conectado"
            else:
                return "Desconectado"
        except Error:
            return "Desconectado"
        except Exception:
            return "Desconectado"

if __name__ == '__main__':
    db = CreateConnection()
    connection = db.create_connection()
    while True:
        estado = db.check_connection(connection)
        print(f"Estado de la conexión: {estado}")
        time.sleep(5)