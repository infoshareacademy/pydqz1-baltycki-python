import random

user_name = ""
user_surname = ""
email = ""
nick = ""
address = []

def generate_name():
    pass

def generate_surname():
    surname_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            surname_list.append(person[1])
    user_surname = random.choice(surname_list)
    return user_surname

def generate_email():
    pass

def generate_nick():
    with open("nick.txt", "r") as f:
        for line in f:
            person = line.strip('\n')
            nick.append(person)
    nickname = random.choice(nick)
    return nickname


def generate_address():
    pass