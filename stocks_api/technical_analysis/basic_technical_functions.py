"""Modules required for code"""
# import signal
# import sys
import asyncio
import aiohttp
# import json
import fmpsdk
import pandas as pd
# from IPython.display import display
from stocks_api.start import APIFunctions, QUARTER


class EssentialFinancialInformation:# pylint: disable=too-few-public-methods
    """Class to obtain financial information about trade"""
    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()
        # self.loop = asyncio.get_event_loop()
        # self.client = aiohttp.ClientSession(loop=self.loop)

    # async def task(self, name, work_queue):
    #     """Class to obtain financial information about trade"""
    #     async with aiohttp.ClientSession() as session:
    #         while not work_queue.empty():
    #             url = await work_queue.get()
    #             print(f"Task {name} getting URL: {url}")
    #
    #             async with session.get(url) as response:
    #                 await response.text()
    #
    # async def main(self):
    #     """
    #     This is the main entry point for the program
    #     """
    #     # Create the queue of work
    #     work_queue = asyncio.Queue()
    #
    #     # Put some work in the queue
    #     for url in [
    #         "http://google.com",
    #         "http://yahoo.com",
    #         "http://linkedin.com",
    #         "http://apple.com",
    #         "http://microsoft.com",
    #         "http://facebook.com",
    #         "http://twitter.com",
    #     ]:
    #         await work_queue.put(url)
    #
    #     # Run the tasks
    #
    #     await asyncio.gather(
    #         asyncio.create_task(self.task("One", work_queue)),
    #         asyncio.create_task(self.task("Two", work_queue)),
    #     )



class SyncEssentialFinancialInformation:
    """Class for obtaining information for technical analysis"""

    def __init__(self):
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()

    @classmethod
    def get_income_statement(cls, api_key, symbol):
        """Obtain a company's income statement"""
        # test = fmpsdk.available_traded_list(apikey=api_key)
        # type = 'ok'
        # print('ok')
        return fmpsdk.income_statement(apikey=api_key, symbol=symbol, period=QUARTER)

    @classmethod
    def get_enterprise_values(cls, api_key, symbol):
        """Obtain a company's enterprise values"""
        return fmpsdk.enterprise_values(apikey=api_key, symbol=symbol, period=QUARTER)
        # df = pd.DataFrame(enterprise_values)

    @classmethod
    def get_technical_indicators(cls, api_key, symbol):
        """Obtain a company's technical indications"""
        technical_indicators = \
            fmpsdk.technical_indicators(apikey=api_key, symbol=symbol, statistics_type='sma')
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
