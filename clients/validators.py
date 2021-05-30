import re 

def id_number_valid(id_number):
    return len(id_number) == 11

def name_valid(name):
    return name.isalpha()

def phone_number_valid(phone_number):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(model, phone_number)