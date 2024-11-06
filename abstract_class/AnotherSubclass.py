from abstract_class.AbstractClassExample import AbstractClassExample


class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The subclass is doing something")
