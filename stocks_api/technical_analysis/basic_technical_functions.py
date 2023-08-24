"""Modules required for code"""

import asyncio
import time
import fmpsdk
import pandas as pd
from stocks_api.start import APIFunctions, QUARTER


class Globals:
    """Definition of global variables"""
    STOCK_DATAFRAME = pd.DataFrame()


class EssentialFinancialInformation:
    """Functions for getting required financial information"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.api_functions = APIFunctions()
        self.api_key = self.api_functions.load_api_keys()
        self.trades_loop = asyncio.run(self.main())

    async def get_financial_information(self, delay, what):
        """Obtain financial indicators"""
        print(time.time(),'Start say_after(%s, %s)' % (delay,what))
        print(time.time(),what)
        print('now time to get financial information')
        # income_statement = fmpsdk.income_statement(apikey=self.api_key, symbol=self.symbol, period=QUARTER)
        # enterprise_values = fmpsdk.enterprise_values(apikey=self.api_key, symbol=self.symbol, period=QUARTER)
        # balance_sheet = fmpsdk.balance_sheet_statement_as_reported(apikey=self.api_key, symbol=self.symbol)

        indicators = ['symbol', 'date', 'period', 'priceBookValueRatio', 'priceToSalesRatio', 'priceToFreeCashFlowsRatio', 'enterpriseValueMultiple',]
        # key_metrics = fmpsdk.key_metrics(apikey=self.api_key,symbol='LLAP', period='quarter')

        ratios = fmpsdk.financial_ratios(apikey=self.api_key, symbol=self.symbol, period='quarter')
        collection_indicators = [[(key, value) for key, value in d.items() if key in indicators] for d in ratios]
        df_indicators = pd.DataFrame(columns=indicators)
        # Initialize an empty dictionary
        new_row = {}

        # Loop through the list of tuples and populate the dictionary
        for period in collection_indicators:
            for key, value in period:
                new_row[key] = value

            df_indicators = pd.concat([df_indicators, pd.DataFrame([new_row])], ignore_index=True)
            new_row.clear()

        selected_columns = indicators[3:]
        selected_df = df_indicators[selected_columns]
        selected_df_pct_change = selected_df.pct_change()

        # Rename columns in the resulting DataFrame
        selected_df_pct_change.columns = [col + '_pct_change' for col in selected_columns]

        # Join the calculated percentage changes back to the original DataFrame
        result_df = pd.concat([df_indicators, selected_df_pct_change], axis=1)

        Globals.STOCK_DATAFRAME = pd.concat([Globals.STOCK_DATAFRAME, result_df], ignore_index=True)

        print('ok')




        # df.at[1, 'Duration'] = ['30days', '35days']
        # print(df)

        # df = pd.DataFrame(
        #     [p, p.team, p.passing_att, p.passer_rating()] for p in game.players.passing()
        # )

        # ratio of equity available to common shareholders divided by the number of outstanding shares -
        # indication of how much shareholders are paying for the net assets of a company.
        # price_book_value_ration = ratios['priceBookValueRatio']
        #
        # forward_peg_ratio = ratios[0]['priceEarningsToGrowthRatio']

        # follow peg_ration with growth of stock


        #This metric can become confusing when it turns negative and is generally not a widely-used metric.
        # ev_ebitda_ratio = ratios['enterpriseValueMultiple']

        # The P/S ratio is calculated by dividing the stock price by the underlying company's sales per share.
        # A low ratio could imply the stock is undervalued, while a ratio that is higher-than-average could indicate
        # that the stock is overvalued. The P/S ratio does not take into account whether the company makes any earnings
        # or whether it will ever make earnings.
        # price_to_sales = ratios['priceToSalesRatio']

        # The higher the percentage of free cash flow embedded in a company's operating cash flow,
        # the greater the financial strength of the company.

        # price_to_free_cash_flow = ratios['priceToFreeCashFlowsRatio']

        # print(income_statement)
        # print(enterprise_values)
        # print(balance_sheet)

        return 'bla', 'bla'

        # return 'bla', 'bla' income_statement, enterprise_values

    async def main(self):
        """Start of async loop"""
        start_time = time.time()
        print(start_time, 'Before creating tasks.')
        task1 = asyncio.create_task(self.get_financial_information(0,'hello'))
        await task1
        end_time = time.time()
        print('Total time elapsed: %.2f seconds' % (end_time - start_time))

