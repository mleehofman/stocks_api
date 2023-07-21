import os
import fmpsdk
from dotenv import load_dotenv

stock_list = ["QFIN", "AHLA"
    , "AMZ", "AAPL", "BIDU", "BSX", "5DQ2", "GRU", "MLB1", "MSFT", "08D", "NEE", "SAR", "SHELL"
    , "LLAP"]

undervaluedstocklist = ['ALB','BX','TRVC']

quarter = 'quarter'
annual = 'annual'
api_request_per_minute = 300


class APIFunctions:
    """Class for all general API related functions"""

    def __init__(self):
        self.load_api_keys()

    def load_api_keys(self):
        load_dotenv()
        apikey = os.getenv("FMP_API_KEY")
        return apikey


class TradesList:
    """Class for obtaining or generating list of stocks"""

    def __init__(self):
        # self.stock_list_input = stock_list_input
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()

    def get_trades_list(self, api_key):
        return fmpsdk.available_traded_list(apikey=api_key)
