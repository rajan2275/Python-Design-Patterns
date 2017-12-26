from abc import ABC, abstractmethod

class abstract_factory(ABC):
    @abstractmethod
    def get_attributes(self):
        pass

class image_factory(abstract_factory):
    def get_attributes(self):
       attributes = {'height': 50, 'width': 100, 'url': 'images/test.jpg'}
       return attributes


class text_factory(abstract_factory):
    def get_attributes(self):
       attributes = {'default_text': 'initial test.', 'max_length': 100, 'min_length': 5,  'format': 'text'}
       return attributes


class BaseClass:
    def __init__(self, abs_factory):
        self.abs_factory = abs_factory

    def attributes(self):
        return (self.factory_imp.get_attributes())


class image(BaseClass):
    def __init__(self):
        factory_imp = image()

class text(BaseClass):
    def __init__(self):
        factory_imp = text()


