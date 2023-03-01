import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
symbol = 'AAPL'
request_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=WAT4XIJWKVJIUH0E
print(request_url)

response = requests.get(request_url)
print('type response: ',type(response)) #> <class 'requests.models.Response'>
print('response status code: ', response.status_code) #> 200
print('type response text', type(response.text)) #> <class 'str'>

parsed_response = json.loads(response.text)
print(type(parsed_response)) #> <class 'dict'>


latest_close = parsed_response["Time Series (5min)"]["2023-02-24 17:55:00"]["4. close"]
print("LATEST CLOSING PRICE: ", latest_close)

