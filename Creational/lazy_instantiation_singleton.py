# Lazy instantiation in Singleton Pattern
# ---------------------------------------
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called.")
        else:
            print("Instance already created.", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance=Singleton()
        return cls.__instance


# Class is initialized and object is not created yet.
s = Singleton()

print ("Object created:", Singleton.getInstance())

# instance already created.
s1 = Singleton()

