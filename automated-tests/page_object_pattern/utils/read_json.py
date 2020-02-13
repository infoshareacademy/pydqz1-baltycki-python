import json


class JsonReader:
    @staticmethod
    def get_user_data():
        with open('/home/mateusz/repo/pydqz1-baltycki-python/automated-tests/page_object_pattern/utils/data.json') as file:
            user_data = json.load(file)
        return user_data
