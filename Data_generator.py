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
