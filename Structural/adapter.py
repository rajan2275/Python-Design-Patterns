"""
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
"""

from abc import ABC, abstractmethod

# ----------------
# Target Interface
# ----------------
class Target(ABC):
    """
        Interface for Client
    """
    def __init__(self):
       self._adaptee = Adaptee()

    @abstractmethod
    def request(self):
        pass

# ----------------
# Adapter Class
# ----------------
class Adapter(Target):
    def request(self):
        self._adaptee.adaptee_request()

# ----------------
# Adaptee Class
# --------------
class Adaptee:
    def adaptee_request(self):
        print("Adaptee function called.")


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()