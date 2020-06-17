
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
            
    def execute(self, script, inserted_values=None):
        try:
            connection = self.connection_pool.getconn()
            if connection == None:
                raise ConnectionError("Nepodarilo sa ziskat spojenie.")
            cursor = connection.cursor()
            if(inserted_values is None):
                cursor.execute(script)
            else:
                cursor.execute(script, inserted_values)
            
            connection.commit()
        except(Exception, psycopg2.Error) as error:
            raise ConnectionError(error.__str__())
        finally:
            if(connection):
                connection.close()
                self.connection_pool.putconn(connection)
        
    def executeQuery(self, script, inserted_values=None):
        try:
            connection = self.connection_pool.getconn()
            if connection == None:
                raise ConnectionError("Nepodarilo sa ziskat spojenie.")
            
            cursor = connection.cursor()
            if(inserted_values is None):
                cursor.execute(script)
            else:
                cursor.execute(script, inserted_values)
                
            returns_value = cursor.fetchall()
            connection.commit()
            return returns_value           

        except(Exception, psycopg2.Error) as error:
            raise ConnectionError(error.__str__())
        finally:
            if(connection):
                connection.close()
                self.connection_pool.putconn(connection)


    def run_create_script(self, text_file):
        def get_commands(text_file):
            all_text = ""
            text_file = open(text_file, 'r')
            
            for line in text_file:
                all_text += line.strip()

            return all_text.split(';')[:-1] # Last is only ''

        try:
            connection = self.connection_pool.getconn()
            cursor = connection.cursor()
            commands = get_commands(text_file)

            for command in commands:
                cursor.execute(command)
            connection.commit()

            print("Create script run succesfully!")
        except(Exception, psycopg2.Error) as error:
            raise ConnectionError(error.__str__())
        finally:
            if(connection):
                connection.close()
                self.connection_pool.putconn(connection)


if __name__ == "__main__":
    c = Connection()
    c.run_create_script("create_script.txt")

        












        
        

