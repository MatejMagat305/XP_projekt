
from Conection_database import Connection
from TestExceptions import ConnectionError

class fake_Conection_database(Connection):
    def __init__(self):
        self.good_sql_exe_script=""
        self.good_sql_query_script=""
        self.values = {}
        self.increment = 1
    
    def close(self):
        pass

    def execute(self, script, inserted_values):
        if script !=  self.good_sql_exe_script:
                raise ConnectionError("error")
        self.values[inserted_values]=self.increment
        self.increment+=1

    def executeQuery(self, script, inserted_values):
       if self.good_sql_query_script == script:
           return list([self.values.get(inserted_values,None)])
       return []

