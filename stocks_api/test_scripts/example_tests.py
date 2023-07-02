# import degiroapi
# from degiroapi.product import Product
# from degiroapi.order import Order
# from degiroapi.utils import pretty_json
#
#
# degiro = degiroapi.DeGiro()
# degiro.login("mhnhofman", "#tKDng2.VnkT4rW")
#
# print('ok')
#
# cashfunds = degiro.getdata(degiroapi.Data.Type.CASHFUNDS)
# for data in cashfunds:
#     print(data)



# import requests
# response = requests.get('https://google.com/')
# print(response)

import requests
import os

# Get the API token from an environment variable
token = os.environ.get('NAUTOBOT_TOKEN')

# Add the Authorization header
headers = {'Authorization': f'0c613e62d120c625543dd47ad36a2d58'}

# This is the base URL for all Nautobot API calls
base_url = 'https://nautobot.demo.networktocode.com/api'

# Get the list of devices from Nautobot using the requests module and passing in the authorization header defined above
response = requests.get('https://nautobot.demo.networktocode.com/api/dcim/devices/', headers=headers)



