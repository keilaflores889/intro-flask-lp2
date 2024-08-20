# Data access object - DAO
from conexion.Conexion import Conexion

class CiudadDao:
    
    def getCiudades(self):

        ciudadSQL = """
        SELECT id, descripcion
        FROM ciudades
        """
        #objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
          cur.execute(ciudadSQL)
          #trae datos de db
          lista_ciudades = cur.fetchall()
          #retorno de datos
          return lista_ciudades
        except con.Error as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def guardarCiudad(self, descripcion):
        
        insertCiudadSQL = """
        INSERT INTO ciudades(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        #Ejecucion exitosa
        try:
            cur.execute(insertCiudadSQL, (descripcion,))
            #se confirma la isercion
            con.commit()

            return True

        #si algo falla aqui
        except con.Error as e:
            print(e)
            
        #siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False    
          
