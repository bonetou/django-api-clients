import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clients.models import Client

def create_clients(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        phone_number = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        active = random.choice([True, False])
        p = Client(name=name, email=email, cpf=cpf, phone_number=phone_number, active=active)
        p.save()

create_clients(100)