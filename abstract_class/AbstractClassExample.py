from abc import ABC, abstractmethod # Abstract Base Classes

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass