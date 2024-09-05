from faker import Faker
from mod_5.BaseContact import BaseContact


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, job_title, company_name, position):
        super().__init__(first_name, last_name)
        self.position = position
        self.job_title = job_title
        self.company_name = company_name
        self.work_phone = Faker().phone_number()

    def contact(self):
        print(f"Wybieram numer {self.work_phone} i dzwonię do {self.full_name()}")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name()} - {self.work_phone} - {self.email} - {self.company_name} - {self.position}"