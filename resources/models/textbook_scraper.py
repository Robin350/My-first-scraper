#!/usr/bin/env python

import os
import logging
import currencyconverter

from resources.utils import scraper, translator
from resources.models.textbook import Textbook


class TextbookScraper:

    TEXT_NUMBERS_TO_INT = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    HEADERS = ["ID", "Title", "Image URL", "Stars", "Content"]

    def __init__(self):

        self._base_url = os.environ.get("TEXTBOOK_WEB_BASEURL")
        self._current_page = None
        self._next_page = "/index.html"

        self.output_file = os.environ.get("OUTPUT_FILE")

        self.soup = None
        self.books = []

    def load_book_page(self):

        """
        Loads a book page into the book collection.
        """

        self.soup = scraper.load_web_xml_content(f"{self._base_url}{self._current_page}")

        books = soup.find_all("article", class_="product_pod")
        for book in books:
            book_data = {
                "image_url": book.find("div", class_="image_container").a.img["src"],
                "price": book.find("p", class_="price_color").getText()[2:],
                "star_rating": text_numbers_to_int[book.find("p", class_="star-rating")["class"][1]],
                "title": book.find("h3").a.getText(),
            }

            self.books.append(Textbook(**book_data))

        self._next_page = soup.find("li", class_="next")

    def load_all_books(self):

        """
        Loads all books from the TEXTBOOK_WEB_BASEURL pages
        """

        while self._next_page:
            self._current_page = self._next_page
            self.load_book_page()

    def print_books_csv(self):

        with open(self.output_file, "a") as output:
            output.write(self.headers.join(","))

        if not self.books:
            logging.warning("No books to write.")
        else:
            with open(self.output_file, "a") as output:
                for book in self.books:
                    output.write(
                        f"{book.id},{book.title},{book.image_url},{book.star_rating},{book.content}"
                    )
