#!/usr/bin/env python

textbook_api = Blueprint("textbook_api", __name__)


@textbook_api.url_value_preprocessor
def remove_version(endpoint, values):
    values.pop("version")


@textbook_api.route("/textbooks", methods=["GET"])
def get_textbooks():
    return None


@textbook_api.route("/textbooks/<textbook_id>", methods=["GET"])
def get_textbook(textbook_id):
    return None
