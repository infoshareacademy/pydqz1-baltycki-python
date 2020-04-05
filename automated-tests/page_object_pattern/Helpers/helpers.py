import time
import pytest


class Helpers:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def slow_typing(element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.01)
