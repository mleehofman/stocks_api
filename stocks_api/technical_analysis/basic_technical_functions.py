import fmpsdk
import pandas as pd
from IPython.display import display
from stocks_api.start import APIFunctions


class EssentialFinancialInformation:
    """Class for obtaining information for technical analysis"""

    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()

    @classmethod
    def get_income_statement(cls, api_key, symbol):
        income_statement = fmpsdk.income_statement(apikey=api_key, symbol=symbol)
        # df = pd.DataFrame(income_statement)
        # display(df)

    @classmethod
    def get_technical_indicators(cls, api_key, symbol):
        technical_indicators = fmpsdk.technical_indicators(apikey=api_key, symbol=symbol, statistics_type='sma')
        df = pd.DataFrame(technical_indicators)
        display(df)
