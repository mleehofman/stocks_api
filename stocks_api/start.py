import os
import fmpsdk
from dotenv import load_dotenv

stock_list = ["QFIN", "AHLA"]
    # , "AMZ", "AAPL", "BIDU", "BSX", "5DQ2", "GRU", "MLB1", "MSFT", "08D", "NEE", "SAR", "SHELL"
    # , "LLAP"]

quarter = 'quarter'
annual = 'annual'


class APIFunctions:
    """Class for all general API related functions"""

    def __init__(self):
        self.load_api_keys()

    def load_api_keys(self):
        load_dotenv()
        apikey = os.getenv("FMP_API_KEY")
        return apikey


class StockList:
    """Class for obtaining or generating list of stocks"""

    def __init__(self, stock_list_input):
        self.stock_list_input = stock_list_input
        self.return_stock_list()

    def get_stock_list(self):
        return self.stock_list_input
