# Data access object - DAO
from flask import current_app as app
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
          lista_ordenada = []
          for item in lista_ciudades:
              lista_ordenada.uppend({
                  "id": item[0],
                  "descripcion": item[1]
              })
          return lista_ordenada
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
            app.logger.info(e)
            
        #siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False    
          
