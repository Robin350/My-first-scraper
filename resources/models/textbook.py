#!/usr/bin/env python

import os
import logging

from threading import Lock
from resources.utils import text_generator

from currency_converter import CurrencyConverter


class Textbook:
    ID_COUNT = 1

    def __init__(self, title: str, price: int, star_rating: int, image_url: str):
        self.title = title

        assert 0 <= star_rating <= 5
        self.star_rating = star_rating

        c = CurrencyConverter()
        self.price = c.convert(float(price), "GBP", "EUR")
        self.image_url = image_url
        self.content = text_generator.generate_random_text(f"The text of {title} is:")

        self.id = self.generate_unique_id()

    def generate_unique_id(self):

        """
        Generates a unique ID in a sequential way
        """

        lock = Lock()

        lock.acquire()
        try:
            my_id = self.ID_COUNT
            self.ID_COUNT += 1
        finally:
            lock.release()  # release lock

        assert id not in self.books
        return my_id
