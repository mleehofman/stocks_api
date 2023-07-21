from stocks_api.start import APIFunctions, TradesList
from stocks_api.technical_analysis.basic_technical_functions import EssentialFinancialInformation


class SimpleTestScripts:

    def __init__(self, start_functions: APIFunctions, technical_functions: EssentialFinancialInformation):
        self.api_key = self.test_load_api_key()
        self.trades_list_class = TradesList()
        self.trades_list = self.trades_list_class.get_trades_list(self.api_key)
        # self.test = [stock for stock in self.stock_list]
        trade_categories = []
        exchange_list = []

        for trade in self.trades_list:
            if trade['type'] not in trade_categories:
                trade_categories.append(trade['type'])
            if trade['exchangeShortName'] not in exchange_list:
                exchange_list.append(trade['exchangeShortName'])
        # stock_list = [stock for stock in self.stock_list if stock['type'] == 'stock']

        # self.technical_functions = technical_functions
        # stock_list = self.technical_functions.get_available_commodities(api_key=self.api_key)
        print('ok')
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


SimpleTestScripts(APIFunctions, EssentialFinancialInformation)




