from abc import ABC, abstractmethod
from faker import Faker


class BaseContact(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = Faker().phone_number()
        self.email = Faker().email()

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")


    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.full_name()}")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name()} - {self.phone_number} - {self.email}"