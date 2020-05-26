
from Conection_database import Connection
from TestExceptions import ConnectionError

class fake_Conection_database(Connection):
    def __init__(self):
        self.good_sql_exe_script=""
        self.good_inserted_values_exe=(1,1)
        self.good_sql_query_script=""
        self.good_inserted_values_query=(1,1)
        self.result = set([1,2,3])

    
    def close(self):
        pass

    def execute(self, script, inserted_values):
        if script !=  self.good_sql_exe_script:
            if inserted_values != self.good_inserted_values_exe:
                raise ConnectionError("error") 

    def executeQuery(self, script, inserted_values):
       if good_sql_query_script == script:
           if good_inserted_values_query == inserted_values:
               return self.result
       return set()

connection = fake_Conection_database()
