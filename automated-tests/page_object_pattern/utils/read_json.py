import json


class JsonReader:
    @staticmethod
    def get_user_data():
        with open('data.json') as file:
            user_data = json.load(file)
        return user_data
