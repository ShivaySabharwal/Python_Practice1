from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("In Laptop Class...")

class Whiteboard:
    def func1(self):
        print("I am writing...")

class Programmer:
    def work(self,other):
        print("I am coding...")
        other.process()

a1 = Laptop()
a1.process()
print()

a2 = Programmer()
a2.work(a1)