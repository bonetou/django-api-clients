import re
from validate_docbr import CPF

cpf = CPF()

# Validar CPF
cpf.validate("012.345.678-90")  # True
cpf.validate("012.345.678-91")  # False

def cpf_valid(id_number):
    cpf = CPF()
    return cpf.validate(id_number)

def name_valid(name):
    return name.isalpha()

def phone_number_valid(phone_number):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(model, phone_number)