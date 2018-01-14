# ------------------------------
# Template Design Pattern.
# ------------------------------
# Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses 
# redefine certain steps of an algorithm without changing the algorithm's structure

from abc import ABC, abstractmethod

class Template(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def function1(self):
        pass

    @abstractmethod
    def function2(self):
        pass

    def execute(self):
        print("Run function1 and function2.")
        self.function1()
        self.function2()


class TemplateImplementation1(Template):
    def function1(self):
        print("TemplateImplementation1.function1() called.")


    def function2(self):
        print("TemplateImplementation1.function2() called.")


class TemplateImplementation2(Template):
    def function1(self):
        print("TemplateImplementation2.function1() called.")


    def function2(self):
        print("TemplateImplementation2.function2() called.")


template_implementation11 = TemplateImplementation1()
template_implementation11.execute()

print("-----------------------------------------------")

template_implementation12 = TemplateImplementation2()
template_implementation12.execute()


