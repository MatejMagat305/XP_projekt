
import psycopg2
from psycopg2 import pool
from small_stuff import MyError

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
                raise MyError(1)
                
        except (Exception, psycopg2.Error) as error:
            raise MyError(error)

    def close(self):
        if self.connection_pool:
            self.connection_pool.closeal()
    def execute_regist(self, script, name, password):
        try:
            connection=self.connection_pool.getconn()
            if connection==None:
                raise MyError()
            cursor = connection.cursor()
            inserted_values = (name, password)
            cursor.execute(script, inserted_values)
            
            connection.commit()
            connection.close()
            self.connection_pool.putconn(connection)

        except(Exception, psycopg2.Error) as error:
            raise MyError(error.__str__())


connection = Connection()
