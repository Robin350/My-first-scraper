#!/usr/bin/env python

import os
import requests
import logging

from bs4 import BeautifulSoup


def load_web_xml_content(url: str):

    """
    Loads the URL response into a BeautifulSoup object.

    :param url: URL to request the content, the response must be in XML
    return: The parsed response in a BeautifulSoup object
    """

    logging.info(f"Getting '{url}' XML content.")

    response = requests.get(url)

    if not response.ok:
        logging.error(f"Error requesting URL '{url}': {response.status_code}\n'{response.text}'")
        raise Exception(f"Error response '{response.status_code}' requesting URL '{url}'")

    try:
        soup = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        logging.error(f"Unexpected error converting response to soup: '{str(e)}'")
        raise e

    return soup
