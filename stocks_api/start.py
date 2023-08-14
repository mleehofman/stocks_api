"""Modules required for code"""
import os
import fmpsdk
from dotenv import load_dotenv

stock_list = ["QFIN", "AHLA"
    , "AMZ", "AAPL", "BIDU", "BSX", "5DQ2", "GRU", "MLB1", "MSFT", "08D", "NEE", "SAR", "SHELL"
    , "LLAP"]

undervaluedstocklist = ['ALB','BX','TRVC']

QUARTER = 'quarter'
ANNUAL = 'annual'
API_REQUESTS_PER_MINUTE = 300


class APIFunctions:# pylint: disable=too-few-public-methods
    """Class for all general API related functions"""

    def __init__(self):
        self.load_api_keys()

    def load_api_keys(self):
        """function to load API Key"""
        load_dotenv()
        apikey = os.getenv("FMP_API_KEY")
        return apikey


class TradesList:
    """Class for obtaining or generating list of stocks"""

    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()
        self.traded_categories = []
        self.stock_exchange = []

    def get_traded_list(self, api_key):
        """Functions to get a list of all available trades"""
        return fmpsdk.available_traded_list(apikey=api_key)

    def get_trade_exchange_categories(self, traded_list):
        """Functions to determine which stock category and stock exchange a trade belongs to"""
        for trade in traded_list:
            if trade['type'] not in self.traded_categories:
                self.traded_categories.append(trade['type'])
            if trade['exchangeShortName'] not in self.stock_exchange:
                self.stock_exchange.append(trade['exchangeShortName'])
        return self.traded_categories, self.stock_exchange
