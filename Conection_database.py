
import psycopg2
from psycopg2 import pool
from TestExceptions import ConnectionError

class Connection:

    def __init__(self):
        try:
            
            if self.connection_pool==None:
                raise ConnectionError("Connection failed.")
                
        except (Exception, psycopg2.Error) as error:
            raise ConnectionError(error)

    def close(self):
        if self.connection_pool:
            self.connection_pool.closeall()
            
    def execute(self, script, inserted_values):
        try:
            connection0 = self.connection_pool.getconn()
            if connection0 == None:
                raise ConnectionError("Nepodarilo sa ziskat spojenie.")
            cursor = connection0.cursor()              
            cursor.execute(script, inserted_values)
            
            connection0.commit()
            

        except(Exception, psycopg2.Error) as error:
            raise ConnectionError(error.__str__())
        finally:
            if(connection0):
                connection0.close()
                self.connection_pool.putconn(connection0)
        
    def executeQuery(self, script, inserted_values):
        try:
            connection0 = self.connection_pool.getconn()
            if connection0 == None:
                raise ConnectionError("Nepodarilo sa ziskat spojenie.")
            cursor = connection0.cursor()              
            cursor.execute(script, inserted_values)
            returns_value= cursor.fetchall()
            connection0.commit()
            return  returns_value           

        except(Exception, psycopg2.Error) as error:
            raise ConnectionError(error.__str__())
        finally:
            if(connection0):
                connection0.close()
                self.connection_pool.putconn(connection0)

