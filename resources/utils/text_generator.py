#!/usr/bin/env python

import os
import requests
import logging


def generate_random_text(text: str):

    """
    Generates random text using https://deepai.org given a input text.

    :param text: Text used as input to generate the random text
    return: The generated text as a string
    """

    logging.info(f"Getting random text from '{text}'.")

    response = requests.post(
        f"{os.environ.get(TEXT_GENERATOR_URL)}",
        data={"text": text},
        headers={"Api-Key": os.environ.get(TEXT_GENERATOR_API_KEY)}
    )

    if not response.ok:
        logging.error(f"Error requesting URL '{url}': {response.status_code}\n'{response.text}'")
        raise Exception(f"Error response '{response.status_code}' requesting URL '{url}'")

    return response.json()["output"]
