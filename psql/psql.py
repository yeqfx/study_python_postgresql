class Database:
    def __init__(self, dbName):
        self.conn_params_dic = {
            "host"      : "db",
            "user"      : "postgres",
            "password"  : "postgres"
        }
        self.dbName = dbName

class Table(Database):
    def __init__(self, dbName):
        super.__init__(self, dbName)
        self.conn_params_dic["db"] = dbName