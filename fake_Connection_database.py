
from Conection_database import Connection
from TestExceptions import ConnectionError

class fake_Conection_database(Connection):
    def __init__(self):
        self.good_sql_exe_script=""
        self.good_inserted_values_exe=(1,1)
        self.good_sql_query_script=""
        self.good_inserted_values_query=(1,1)
        self.result = set([1,2,3])
        self.values = {}
        self.increment = 1

    
    def close(self):
        pass

    def execute(self, script, inserted_values):
        if script !=  self.good_sql_exe_script:
                raise ConnectionError("error")
        self.values.put((inserted_values,self.increment)) 

    def executeQuery(self, script, inserted_values):
       if good_sql_query_script == script:
           return self.values.get(inserted_values,[])
       return []

