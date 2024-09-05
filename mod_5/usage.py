from mod_5.BusinessContact import BusinessContact
from faker import Faker
from mod_5.BaseContact import BaseContact

def create_contacts(contact_type, quantity):
    contacts = []
    if contact_type == "business":
        for _ in range(quantity):
            first_name = Faker().first_name()
            last_name = Faker().last_name()
            job_title = Faker().job()
            company_name = Faker().company()
            position = Faker().job()
            buis = BusinessContact(first_name, last_name, job_title, company_name, position)
            contacts.append(buis)
    elif contact_type == "basic":
        for _ in range(quantity):
            first_name = Faker().first_name()
            last_name = Faker().last_name()
            contacts.append(BaseContact(first_name, last_name))
    else:
        raise ValueError("Invalid contact type")
    return contacts


if __name__ == "__main__":

    business_contacts = create_contacts("business", 3)
    for contact in business_contacts:
        contact.contact()

    basic_contacts = create_contacts("basic", 2)
    for contact in basic_contacts:
        contact.contact()