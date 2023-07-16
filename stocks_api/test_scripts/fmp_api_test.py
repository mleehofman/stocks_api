from stocks_api.start import APIFunctions, stock_list
from stocks_api.technical_analysis.basic_technical_functions import EssentialFinancialInformation


class SimpleTestScripts:

    def __init__(self, technical_functions: EssentialFinancialInformation):
        self.api_key = self.test_load_api_key()
        self.stock_list = stock_list
        self.technical_functions = technical_functions
        self.test_iterating_stock_list()

    def test_load_api_key(self):
        api_functions = APIFunctions()
        return api_functions.load_api_keys()

    def test_iterating_stock_list(self):

        for symbol in self.stock_list:
            income_statement = self.technical_functions.get_income_statement(api_key=self.api_key, symbol=symbol)
            # self.technical_functions.get_technical_indicators(api_key=self.api_key, symbol=symbol)
            enterprise_values = self.technical_functions.get_enterprise_values(api_key=self.api_key, symbol=symbol)
            self.technical_functions.calculate_ev_ebitda(income_statement, enterprise_values)


SimpleTestScripts(EssentialFinancialInformation)




