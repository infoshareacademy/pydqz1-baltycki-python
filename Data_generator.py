import random
import json

user_name = ""
user_surname = ""
email = ""
nick = ""
address = []

def generate_name():
    pass

def generate_surname():
    pass

def generate_email():
    email_body = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            email_body.append(line)
    domain = [".com", ".org", ".mil", ".net", ".edu", ".pl", ".de", ".fr", ".ie", ".us", ".co.uk"]
    local_part = email_body[random.randint(0, len(email_body) - 1)]
    host_name = email_body[random.randint(0, len(email_body) - 1)]
    mail_domain = (domain[random.randint(0, len(domain) - 1)])
    full_email = local_part + "@" + host_name + mail_domain
    return full_email

email = generate_email()

def generate_nick():
    pass

def generate_address():
    code = []
    street = []
    city = []
    with open("address.txt", "r") as f:
        for line in f:
            address_data = line.split(",")
            code.append(address_data[0])
            street.append(address_data[1])
            city.append(address_data[2])
    city_code = code[random.randint(0, len(code) - 1)]
    city_name = city[random.randint(0, len(city) - 1)]
    city_street = street[random.randint(0, len(street) - 1)]
    full_address = city_code + " " + city_name.strip('\n') + ", " + city_street + " " + str(random.randint(1,100))
    return full_address

address = generate_address()