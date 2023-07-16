import fmpsdk
import pandas as pd
from IPython.display import display
from stocks_api.start import APIFunctions, quarter


class EssentialFinancialInformation:
    """Class for obtaining information for technical analysis"""

    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()

    @classmethod
    def get_income_statement(cls, api_key, symbol):
        return fmpsdk.income_statement(apikey=api_key, symbol=symbol, period=quarter)
        # ebitda = income_statement[0]['ebitda']
        print('ok')
        # df = pd.DataFrame(income_statement)

    @classmethod
    def get_enterprise_values(cls, api_key, symbol):
        return fmpsdk.enterprise_values(apikey=api_key, symbol=symbol, period=quarter)
        # df = pd.DataFrame(enterprise_values)

    @classmethod
    def get_technical_indicators(cls, api_key, symbol):
        technical_indicators = fmpsdk.technical_indicators(apikey=api_key, symbol=symbol, statistics_type='sma')
        df = pd.DataFrame(technical_indicators)

    @classmethod
    def calculate_ev_ebitda(cls, income_statement, enterprise_values):
        ev_ebitda = enterprise_values[0]['enterpriseValue'] / income_statement[0]['ebitda']
        print(ev_ebitda)
        ##TODO: trigger when ev_ebitda ration is < 10

