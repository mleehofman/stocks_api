from stocks_api.start import APIFunctions, TradesList
from stocks_api.technical_analysis.basic_technical_functions import SyncEssentialFinancialInformation


class SimpleTestScripts:

    def __init__(self, start_functions: APIFunctions, technical_functions: SyncEssentialFinancialInformation):
        self.api_key = self.test_load_api_key()
        self.traded_list_class = TradesList()

        self.traded_list = self.traded_list_class.get_traded_list(self.api_key)
        self.trade_exchange_categories = self.traded_list_class.get_trade_exchange_categories(self.traded_list)
        print('ok')

        self.technical_functions = technical_functions
        # self.stock_list = self.technical_functions.get_available_commodities(api_key=self.api_key)
        self.test_iterating_stock_list()

    def test_load_api_key(self):
        api_functions = APIFunctions()
        return api_functions.load_api_keys()

    def test_iterating_stock_list(self):


        index = 0
        while index < len(self.traded_list):
            for symbol in self.traded_list[index]:
                print(self.traded_list[index][symbol])
                # income_statement = self.technical_functions.get_income_statement(api_key=self.api_key, symbol=symbol)
                # # self.technical_functions.get_technical_indicators(api_key=self.api_key, symbol=symbol)
                # enterprise_values = self.technical_functions.get_enterprise_values(api_key=self.api_key, symbol=symbol)
                # self.technical_functions.calculate_ev_ebitda(income_statement, enterprise_values)
            index += 1
        # for symbol in self.trades_list:
        #     print(symbol)
            # income_statement = self.technical_functions.get_income_statement(api_key=self.api_key, symbol=symbol)
            # # self.technical_functions.get_technical_indicators(api_key=self.api_key, symbol=symbol)
            # enterprise_values = self.technical_functions.get_enterprise_values(api_key=self.api_key, symbol=symbol)
            # self.technical_functions.calculate_ev_ebitda(income_statement, enterprise_values)
            # print('ok')


SimpleTestScripts(APIFunctions, SyncEssentialFinancialInformation)




