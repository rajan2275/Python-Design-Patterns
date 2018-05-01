
# -----------------------------------------------------------------------
# Singleton Pattern
# -----------------------------------------------------------------------
# singleton pattern restricts the instantiation of a class to one object. 
# -----------------------------------------------------------------------


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance



# s1 and s2 will refer to same object.
# ----------------------------------------
s1 = Singleton()
print("First object",  s1)

s2 = Singleton()
print("Second object",  s2)
