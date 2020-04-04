import random
import json

user_name = ""
user_surname = ""
email = ""
nick = ""
address = ""


def generate_name():
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            name_list.append(person[0])
    user_name = random.choice(name_list)
    return user_name


def generate_surname():
    surname_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            surname_list.append(person[1])
    user_surname = random.choice(surname_list)
    return user_surname


def generate_email():
    email_body = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            email_body.append(line)
    domain = [".com", ".pl"]
    local_part = random.choice(email_body)
    host_name = random.choice(email_body)
    mail_domain = random.choice(domain)
    full_mail = local_part + "@" + host_name + mail_domain
    return full_mail


email = generate_email()


def generate_nick():
    with open("nick.txt", "r") as f:
        for line in f:
            person = line.strip('\n')
            nick.append(person)
    nickname = random.choice(nick)
    return nickname



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
    city_code = random.choice(code)
    city_name = random.choice(city)
    city_street = random.choice(street)
    full_address = city_code + " " + city_name.strip('\n') + ", " + city_street + " " + str(random.randint(1, 100))
    return full_address


address = generate_address()
