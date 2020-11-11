# web_app/services/stocks_service.py

import requests
import json

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
print(request_url)

response = requests.get(request_url)
print(type(response))  # > <class 'requests.models.Response'>
print(response.status_code)  # > 200
print(type(response.text))  # > <class 'str'>

# transforms the string response into a usable python datatype (list or dict)
parsed_response = json.loads(response.text)
print(type(parsed_response))  # > <class 'dict'>

latest_close = parsed_response["Time Series (5min)"]["2020-11-10 19:50:00"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)


