
# ---------------------------------------------------
# Observer Pattern in publisher and subscriber model.
# ---------------------------------------------------
from abc import ABC, abstractmethod

class Publisher:
    def __init__(self):
        self.__subscribers = []
        self.__content = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        self.__subscribers.pop()

    def get_subscribers(self):
        return[type(x).__name__ for x in self.__subscribers]

    def updateSubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_content(self, content):
        self.__content = content

    def get_content(self):
        return ("Content:" + self.__content)

# -------------------------------------
# Subscriber base class
# -------------------------------------
class Subscriber(ABC):

    @abstractmethod
    def update(self):
        pass

# --------------------
# Subscriber 1
# --------------------
class SiteSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_content())

# --------------------
# Subscriber 2
# --------------------
class IntranetSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_content())

# --------------------
# Subscriber 3
# --------------------
class ApiSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_content())



publisher = Publisher()

for subs in [SiteSubscriber, IntranetSubscriber, ApiSubscriber]:
    subs(publisher)

print("All Subscriber: ", publisher.get_subscribers())
print("------------------------------------------------")

publisher.add_content('Update content on all subscribers.')
publisher.updateSubscribers()

print("------------------------------------------------")

publisher.detach()

print("Remaining Subscriber: ", publisher.get_subscribers())
print("------------------------------------------------")

publisher.add_content('Updated content for remaining subscriber.')
publisher.updateSubscribers()

