import random
import json


def generate_name(ptf=True):
    name_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            name_list.append(person[0])
    user_name = random.choice(name_list)
    if ptf is True:
        with open("log.data", "a+") as f:
            f.write(user_name + "\n")
    return user_name


def generate_surname(ptf=True):
    surname_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            surname_list.append(person[1])
    user_surname = random.choice(surname_list)
    if ptf is True:
        with open("log.data", "a+") as f:
            f.write(user_surname + "\n")
    return user_surname


def generate_email(ptf=True):
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
        with open("log.data", "a+") as f:
            f.write(e_mail + "\n")
    return e_mail


def generate_nick(ptf=True):
    nick_list = []
    with open("nick.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            nick_list.append(line)
    nick = random.choice(nick_list) + str(random.randint(1, 100))
    if ptf is True:
        with open("log.data", "a+") as f:
            f.write(nick + "\n")
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
        with open("log.data", "a+") as f:
            save_address = address["Postal code"] + ", " + address["City"] + ", " + address["Street"]
            f.write(save_address + "\n")
    return address


''' 
def full_set(user_name, user_surname, nick, e_mail, address):
    data = {"First name": user_name, "Last name": user_surname,
            "Nick": nick, "E-mail": e_mail, "Address": address}

    for key, value in data.items():
        print(key + ": " + value)
    return data


def save_to_json(user_name, user_surname, nick, e_mail, address):
    import json

    json_data = {"First name": user_name, "Last name": user_surname, "Nick": nick, "E-mail": e_mail,
                 "Address": address}

    json_string = json.dumps(json_data)

    with open("data.json", "w") as f:
        f.write(json_string)


def save_to_xml(user_name, user_surname, nick, e_mail, address):
    import xml.etree.ElementTree as xml

    root = xml.Element("Test data")
    cl = xml.Element("User")
    root.append(cl)

    name1 = xml.SubElement(cl, "First name")
    name1.text = user_name

    surname1 = xml.SubElement(cl, "Last name")
    surname1.text = user_surname

    nick1 = xml.SubElement(cl, "Nick")
    nick1.text = nick

    email1 = xml.SubElement(cl, "Email")
    email1.text = e_mail

    address1 = xml.SubElement(cl, "Address")
    address1.text = address

    tree = xml.ElementTree(root)

    with open("User.xml", "wb") as files:
        tree.write(files)'''
