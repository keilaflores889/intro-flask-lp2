import psycopg2
class Conexion:

    """Metodo contructor de tu perro
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=postgres host=localhost pasword=12345678")
        
        """getConexion

            retorna la instancia de la base de datos
        """
    def getConexion(self):
        return self.con 