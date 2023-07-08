import fmpsdk
from stocks_api.start import APIFunctions


def test_load_api_keys():
    # Company Valuation Methods
    api_functions = APIFunctions()
    api_key = api_functions.load_api_keys()
    symbol: str = "AAPL"
    print(f"Company Profile: {fmpsdk.company_profile(apikey=api_key, symbol=symbol)}")


