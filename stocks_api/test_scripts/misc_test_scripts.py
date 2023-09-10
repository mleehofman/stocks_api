import finnhub
import requests
from stocks_api.start import APIFunctions
import asyncio

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


#
# response = requests.request("GET", rtest.url)

stock_metrics = []

# define an asynchronous iterator
class CustomIterator():
    # constructor, define some state
    def __init__(self, length):
        self.counter = 0
        self.length = length

    # create an instance of the iterator
    def __aiter__(self):
        return self

    # return the next awaitable
    async def __anext__(self):
        # check for no further items
        if self.counter >= self.length:
            raise StopAsyncIteration
        # block to simulate work
        await metric()
        # increment the counter
        self.counter += 1
        # return the ratio
        return stock_metrics


async def metric():
    stock_metrics.append('test')

# define a simple coroutine
async def custom_coroutine():
    # asynchronous for loop
    async for item in CustomIterator(10):
        # report the result
        print(item)

# start

coro = custom_coroutine()
asyncio.run(coro)




# # define an asynchronous iterator
# class CustomIterator():
#     # constructor, define some state
#     def __init__(self):
#         self.counter = 0
#
#     # create an instance of the iterator
#     def __aiter__(self):
#         return self
#
#     # return the next awaitable
#     async def __anext__(self):
#         # check for no further items
#         if self.counter >= 10:
#             raise StopAsyncIteration
#         # block to simulate work
#         await asyncio.sleep(1)
#         # increment the counter
#         self.counter += 1
#         # return the counter value
#         return 'bla'
#
# # define a simple coroutine
# async def custom_coroutine():
#     # asynchronous for loop
#     async for item in CustomIterator():
#         # report the result
#         print('test: ' + str(item))
#
# # start
# asyncio.run(custom_coroutine())


import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'Value': [10, 15, 13, 20]}

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Convert the 'Date' column to a datetime object (if not already)
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index (required for time-series plotting)
df.set_index('Date', inplace=True)

# Create a Pandas Series from the 'Value' column
my_series = df['Value']

# Plot the Pandas Series
my_series.plot()

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('My Series Plot')

# Show the plot
plt.show()
