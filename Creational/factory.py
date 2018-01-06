from abc import ABC, abstractmethod

class Database(ABC):
   @abstractmethod
   def connection(self):
        pass

class SqlServer:
    def connection(self):
        return('Sql database connection')


class Oracle:
    def connection(self):
        return('Oracle database connecction.')


class DbFactory:
    def get_database_connection(self, database):
        return database.connection()


#  Client Code
# -----------------------------
factory = DbFactory()
print(factory.get_database_connection(SqlServer()))
print(factory.get_database_connection(Oracle()))