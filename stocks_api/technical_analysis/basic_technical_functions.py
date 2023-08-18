"""Modules required for code"""
# import signal
# import sys
import asyncio
import inspect
import aiohttp
# import json
import time
import fmpsdk
import pandas as pd
# from IPython.display import display
from stocks_api.start import APIFunctions, QUARTER


class EssentialFinancialInformation:

    def __init__(self, symbol):
        self.symbol = symbol
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()
        self.trades_loop = asyncio.run(self.main())

    async def get_financial_information(self, delay, what):
        # await asyncio.sleep(1)
        print(time.time(),'Start say_after(%s, %s)' % (delay,what))
        await asyncio.sleep(delay)
        print(time.time(),what)
        print('now time to get financial information')
        income_statement = fmpsdk.income_statement(apikey=self.api_key, symbol=self.symbol, period=QUARTER)
        enterprise_values = fmpsdk.enterprise_values(apikey=self.api_key, symbol=self.symbol, period=QUARTER)
        balance_sheet = fmpsdk.balance_sheet_statement_as_reported(apikey=self.api_key, symbol=self.symbol)


        fmpsdk.historical_chart(

        )
        print(income_statement)
        print(enterprise_values)
        print(balance_sheet)

        return income_statement, enterprise_values

    async def main(self):
        start_time = time.time()
        print(start_time, 'Before creating tasks.')
        task1 = asyncio.create_task(self.get_financial_information(0,'hello'))
        await task1
        end_time = time.time()
        print('Total time elapsed: %.2f seconds' % (end_time - start_time))


class SyncEssentialFinancialInformation:
    """Class for obtaining information for technical analysis"""

    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()

    @classmethod
    def get_technical_indicators(cls, api_key, symbol):
        """Obtain a company's technical indications"""
        technical_indicators = \
            fmpsdk.technical_indicators(apikey=api_key, symbol=symbol)
        data_frame = pd.DataFrame(technical_indicators)
        print(data_frame)

    @classmethod
    def get_available_commodities(cls, api_key):
        """Obtain all available commodities"""
        return fmpsdk.available_commodities(apikey=api_key)

    @classmethod
    def calculate_ev_ebitda(cls, income_statement, enterprise_values):
        """Evaluate the ev/ebitda value of a company"""
        if len(income_statement) == 0 or len(enterprise_values) == 0:
            ##TODO: add warning
            return
        ev_ebitda = enterprise_values[0]['enterpriseValue'] / income_statement[0]['ebitda']

        print(income_statement[0]['symbol'])

        ##TODO: trigger when ev_ebitda ration is <15

        print(f"the ratio is {ev_ebitda}")

        # if ev_ebitda < 15:
        #     print(f"the ratio is below 15, namely {ev_ebitda}")
