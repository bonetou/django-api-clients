def id_number_valid(id_number):
    return len(id_number) == 11

def name_valid(name):
    return name.isalpha()

def phone_number_valid(phone_number):
    return len(phone_number) < 14
