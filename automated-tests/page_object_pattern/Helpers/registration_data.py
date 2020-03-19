import random
from page_object_pattern.Helpers.Data_generator import *


class RegistrationData:
    def __init__(self):
        self.email_input = generate_email()
        self.first_name_input = generate_name()
        self.last_name_input = generate_surname()
        self.password_input = generate_nick()
        self.city_code, self.city_name, self.city_street = generate_addr_components()
        self.city_code_format = self.city_code.replace("-", "")
        self.mobile_phone_input = random.randint(1, 1000)
        self.state_value_input = str(random.randint(1, 51))
