import os
from dotenv import load_dotenv


class APIFunctions:
    """Class for all general API related functions"""

    def __init__(self):
        self.load_api_keys()

    def load_api_keys(self):
        load_dotenv()
        apikey = os.getenv("API_KEY")
        return apikey
