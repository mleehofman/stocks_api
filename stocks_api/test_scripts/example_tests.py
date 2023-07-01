import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json


degiro = degiroapi.DeGiro()
degiro.login("mhnhofman", "#tKDng2.VnkT4rW")

print('ok')

cashfunds = degiro.getdata(degiroapi.Data.Type.CASHFUNDS)
for data in cashfunds:
    print(data)