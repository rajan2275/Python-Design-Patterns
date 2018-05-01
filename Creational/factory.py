# ---------------------------------------------------------------------------------------------------
# Gang of Four definition
# ---------------------------------------------------------------------------------------------------
# Define an interface for creating an object, but let subclasses decide which class to instantiate. 
# The Factory method lets a class defer instantiation it uses to subclasses.
# 
# In example, client code is deciding about object instantiation.
# ---------------------------------------------------------------------------------------------------

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
