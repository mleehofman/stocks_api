import finnhub
import requests
from stocks_api.start import APIFunctions

# # Setup client
# finnhub_client = finnhub.Client(api_key="ciq1401r01qihcguc03gciq1401r01qihcguc040")
#
# # Stock candles
# res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
# print(res)
#
# #Convert to Pandas Dataframe
# import pandas as pd
# print(pd.DataFrame(res))
#
# # Aggregate Indicators
# print(finnhub_client.aggregate_indicator('AAPL', 'D'))
#
# print(finnhub_client.company_earnings('TSLA', limit=5))
# print('ok')


# api_key = APIFunctions.load_api_keys(None)


# url = (f"https://financialmodelingprep.com/api/v3/enterprise-values/AAPL?apikey={api_key}")
# print('ok')

# symbol = "AAPL"
# api_key = "api_key"
# r = requests.get('https://api-football-v1.p.rapidapi.com/v3/fixtures/', params=url_params)
# rtest = requests.get(url)

print('test')
#
# response = requests.request("GET", rtest.url)



class A:
    def method_a(self, a, b):
        return a + b


class B:
    def method_b(self, a, b):
        return A().method_a(a, b)


b1 = B()

print(b1.method_b(10, 15))  # 👉️ 25
