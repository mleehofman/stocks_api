import fmpsdk
import pandas as pd
from stocks_api.start import APIFunctions


class EssentialFinancialInformation:
    """Class for obtaining information for technical analysis"""

    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()

    @classmethod
    def get_income_statement(cls, api_key, symbol):
        income_statement = fmpsdk.income_statement(apikey=api_key, symbol=symbol)
        df = pd.DataFrame(income_statement)
