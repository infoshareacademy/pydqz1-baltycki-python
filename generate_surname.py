import random
import json

def surname():
    surname_list = []
    with open('person.txt', 'r') as f:
        for line in f:
            person = line.split()
            surname_list.append(person[1])
    return random.choice(surname_list)
