import os
from dotenv import load_dotenv
import typing
import fmpsdk



# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = "0c613e62d120c625543dd47ad36a2d58"


def test_load_api_keys():
    load_dotenv()

    test = os.getenv("API_KEY")

    print('ok')

# Company Valuation Methods
symbol: str = "AAPL"
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)}")