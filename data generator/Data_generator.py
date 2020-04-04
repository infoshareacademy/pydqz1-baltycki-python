import random
import json


def save_to_json(value):
    with open("data.json", "a+", encoding='utf8') as f:
        if f.tell() == 0:
            json.dump(value, f, ensure_ascii=False, indent=4)
        else:
            separator = ',\n'
            f.write(separator)
            json.dump(value, f, ensure_ascii=False, indent=4)


def generate_name(ptf=True):
    name_to_json = {}
    name_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            name_list.append(person[0])
    user_name = random.choice(name_list)
    if ptf is True:
        name_to_json["First name"] = user_name
        save_to_json(name_to_json)
    return user_name


def generate_surname(ptf=True):
    surname_to_json = {}
    surname_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            surname_list.append(person[1])
    user_surname = random.choice(surname_list)
    if ptf is True:
        surname_to_json["Last name"] = user_surname
        save_to_json(surname_to_json)
    return user_surname


def generate_email(ptf=True):
    email_to_json = {}
    email_body = []
    with open("words.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            email_body.append(line)
    domain = [".com", ".pl"]
    local_part = random.choice(email_body)
    host_name = random.choice(email_body)
    mail_domain = random.choice(domain)
    e_mail = local_part + "@" + host_name + mail_domain
    if ptf is True:
        email_to_json["E-mail"] = e_mail
        save_to_json(email_to_json)
    return e_mail


def generate_nick(ptf=True):
    nick_to_json = {}
    nick_list = []
    with open("nick.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            nick_list.append(line)
    nick = random.choice(nick_list) + str(random.randint(1, 100))
    if ptf is True:
        nick_to_json["Nick"] = nick
        save_to_json(nick_to_json)
    return nick


def generate_address(ptf=True):
    address = {}
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
    address["Postal code"] = city_code
    address["City"] = city_name.strip('\n')
    address["Street"] = city_street + " " + str(random.randint(1, 100))
    if ptf is True:
        save_to_json(address)
    return address


def generate_full_set(ptf=True):
    data = {"First name": generate_name(ptf=False), "Last name": generate_surname(ptf=False),
            "Nick": generate_nick(ptf=False), "E-mail": generate_email(ptf=False), "Address": generate_address(ptf=False)}
    if ptf is True:
        save_to_json(data)
    return data