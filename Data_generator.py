import random
import json


def main():
    menu = """
    Select F for first name
    Select L for last name
    Select N for nick
    Select E for e-mail
    Select A for address
    Select S for full set 
    Select J for JSON
    Select X for XML 
    Select Q to quit

    Select: 
    """

    selection = input(menu)

    while selection not in ("Q", "q"):
        if selection in ("F", "f"):
            user_name = generate_name()
            print("First name: {}".format(user_name))
        elif selection in ("L", "l"):
            user_surname = generate_surname()
            print("Last name: {}".format(user_surname))
        elif selection in ("N", "n"):
            nick = generate_nick()
            print("Nick: {}".format(nick))
        elif selection in ("E", "e"):
            e_mail = generate_email()
            print("E-mail: {}".format(e_mail))
        elif selection in ("A", "a"):
            address = generate_address()
            print("Address: {}".format(address))
        elif selection in ("S", "s"):
            pass
        elif selection in ("J", "j"):
            pass
        elif selection in ("X", "x"):
            pass
        else:
            print("Unknown command")
        input("Press any to continue...")
        selection = input(menu)
    print("Program terminated")


def generate_name():
    name_list = []
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


def generate_nick():
    nick_list = []
    with open("nick.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            nick_list.append(line)
    nickname = random.choice(nick_list)
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


main()
