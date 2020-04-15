
import psycopg2
from psycopg2 import pool
from TestExceptions import ConnectionError

class Connection:

    def __init__(self):
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                                          user="magat4@uniba.sk",
                                          password="543210",
                                          host="db.dai.fmph.uniba.sk",
                                          port="5432",
                                          database="playground")
            if self.connection_pool==None:
                raise ConnectionError("Connection failed.")
                
        except (Exception, psycopg2.Error) as error:
            raise ConnectionError(error)

    def close(self):
        if self.connection_pool:
            self.connection_pool.closeall()
            
    def execute(self, script, inserted_values):
        try:
            connection = self.connection_pool.getconn()
            if connection == None:
                raise ConnectionError("Nepodarilo sa ziskat spojenie.")
            cursor = connection.cursor()              
            cursor.execute(script, inserted_values)
            
            connection.commit()
            connection.close()
            self.connection_pool.putconn(connection)

        except(Exception, psycopg2.Error) as error:
            raise ConnectionError(error.__str__())
        
    def executeQuery(self, script, inserted_values):
        pass

connection = Connection()
