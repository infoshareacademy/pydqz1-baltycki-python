import time
import pytest


class Helpers:

    def __init__(self, driver7):
        self.driver = driver7

    @staticmethod
    def slow_typing(element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.01)
