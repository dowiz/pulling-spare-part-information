import os
import json
from dotenv import load_dotenv


def load_dict_from_dotenv(dict_name):

    # Load environment variables from .env file
    load_dotenv()

    # Get data from environment variables
    json_string = os.getenv(dict_name)
    received_dict = json.loads(json_string)

    return received_dict


def get_value_of_soup(soup, key):

    response_text = soup.text
    response_json = json.loads(response_text)
    value = response_json[key]

    return value
