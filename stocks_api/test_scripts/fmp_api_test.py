from stocks_api.start import APIFunctions, TradesList
from stocks_api.technical_analysis.basic_technical_functions import EssentialFinancialInformation, Globals


class SimpleTestScripts:
    """Class for testing iterating stocks for analysis"""
    def __init__(self, technical_functions: EssentialFinancialInformation):
        self.empty_stocklist()
        self.api_key = self.test_load_api_key()
        self.traded_list_class = TradesList()
        self.traded_list = self.traded_list_class.get_traded_list(self.api_key)
        self.trade_exchange_categories = self.traded_list_class.get_trade_exchange_categories(self.traded_list)
        self.technical_functions = technical_functions
        self.test_iterating_stock_list()

    def empty_stocklist(self):
        Globals.STOCK_DATAFRAME.drop(Globals.STOCK_DATAFRAME.index, inplace=True)
        empty_check = Globals.STOCK_DATAFRAME.empty
        print(f'is the dataframe empty: {empty_check}')

    def test_load_api_key(self):
        """function to load API Key"""
        api_functions = APIFunctions()
        return api_functions.load_api_keys()

    def test_iterating_stock_list(self):
        """function to iterate stock list"""
        for idx, trade in enumerate(self.traded_list):
            print(idx)
            if idx > 15:
                print('time to quit')
                break

            if trade['type'] != 'stock':
                print(trade['symbol'])
                print('is not a stock: ')
                print(trade['type'])
                continue
            print('now let us analyze a stock please')
            print(trade['symbol'])
            print('exchange')
            print(trade['exchange'])
            self.technical_functions(trade['symbol'])

        return Globals.STOCK_DATAFRAME


SimpleTestScripts(EssentialFinancialInformation)
