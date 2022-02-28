#!/usr/bin/env python
import logging

from googletrans import Translator, constants


def translate(text: str, to_language: str):

    """
    Translates given text from the auto-detected google translate
    language to the specified language.

    :param text: Text to translate, the language will be auto-detected
    :param to_language: Destination language code

    return: The text translated as a string
    """

    if to_language not in googletrans.LANGUAGES + googletrans.LANGCODES:
        logging.error(
            f"Language code must be in: [{googletrans.LANGUAGES + googletrans.LANGCODES}]."
        )
        raise Exception("Unsupported language, check Google Translate language codes")

    logging.info(f"Translating '{text[0:15]}...' to '{to_language}'.")
    translator = Translator()

    translation = translator.translate(text, dest=to_language)
    logging.info("Translation successful.")

    return translation.text
