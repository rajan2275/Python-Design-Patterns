# ----------------
# Command Pattern.
# ----------------
# Encapsulate a request as an object, thereby allowing for the parameterization of clients with different requests, 
# and the queuing or logging of requests. It also allows for the support of undoable operations.

class Installer:
    def __init__(self, source, dir):
        self.options = []
        self.dir = dir
        self.source = source

    def add_preferences(self, cmd):
        self.options.append(cmd)

    def install(self):
        for option in self.options:
            value = [v for k, v in option.items()]

            if (value[0]):
                print("installing files -- ", [k for k, v in option.items()], self.source, " to ", self.dir)
            else:
                print('Not installed: ', [k for k, v in option.items()])

installer =  Installer('C++ binaries', 'c:\\c++\\binaries')
installer.add_preferences({'c++':True})
installer.add_preferences({'c#': False})
installer.install()

