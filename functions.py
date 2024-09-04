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
