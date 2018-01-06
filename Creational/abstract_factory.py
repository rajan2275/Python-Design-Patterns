# -----------------------------------------------------------------------------------------------------------------
# Abstract Factory example:  Web and intranet are two different applications. Both use Sql And No SQL databases,
# Web uses mongodb and SQL but intranet uses Oracle and OrientDB. Both have different implementations.
# -----------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class db_factory(ABC):
    @abstractmethod
    def create_sql_db(self):
        pass
    @abstractmethod
    def create_sql_db(self):
        pass

class web_factory(db_factory):
    def create_no_sql_db(self):
        return mongodb()
    def create_sql_db(self):
        return SQL()

class intranet_factory(db_factory):
    def create_no_sql_db(self):
        return orientdb()
    def create_sql_db(self):
        return Oracle()


class sql_database(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def select(self):
        pass

class SQL(sql_database):
    def save(self):
        print ("SQL save called.")
    def select(self):
        print("SQL select called.")

class Oracle(sql_database):
    def save(self):
        print ("Oracle save called.")
    def select(self):
        print("Oracle select called")


class no_sql_database(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def get_object(self):
        pass

class mongodb(no_sql_database):
    def insert(self):
        print("mongodb insert called.")
    def get_object(self):
        print("mongodb get_object called.")

class orientdb(no_sql_database):
    def insert(self):
        print("orientdb insert called.")
    def get_object(self):
        print("orientdb get_object called.")



class client:
    def get_database(self):
        abs_factory = web_factory()
        sql_factory = abs_factory.create_sql_db()
        sql_factory.save()
        sql_factory.select()

        # -------------------------------------------
        abs_factory = web_factory()
        sql_factory = abs_factory.create_no_sql_db()
        sql_factory.insert()
        sql_factory.get_object()

        # -------------------------------------------
        abs_factory = intranet_factory()
        ora_factory = abs_factory.create_sql_db()
        ora_factory.save()
        ora_factory.select()

        # -------------------------------------------
        abs_factory = intranet_factory()
        ora_factory = abs_factory.create_no_sql_db()
        ora_factory.insert()
        ora_factory.get_object()




client = client()
client.get_database()
