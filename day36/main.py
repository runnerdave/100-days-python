import os
import requests
import urllib3
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
alphavantage_api_key=os.environ.get("ALPHAVANTAGE_API_KEY")
stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alphavantage_api_key}'
response = requests.get(url=stock_url, verify=False)
response.raise_for_status()
data = response.json()
# Get the second date
second_date = list(data["Time Series (Daily)"].keys())[1]

# Get the value for "4. close" for the second date
close_value = data["Time Series (Daily)"][second_date]["4. close"]

def get_close_value_by_position(position) -> float:
    date = list(data["Time Series (Daily)"].keys())[position]
    return data["Time Series (Daily)"][date]["4. close"]

def up_or_down_points(value1, value2):
    up = "🔺"
    down = "🔻"
    if value1 > value2:
        percentage_difference = format((value1 - value2)/value1*100, ".2f")
        return f"{up} {percentage_difference}"
    else:
        percentage_difference = format((value2 - value1)/value2*100, ".2f")
        return f"{down} {percentage_difference}"

print("######### STOCK DATA #############")
day_before_yesterday = float(get_close_value_by_position(2))
yesterday = float(get_close_value_by_position(1))
print(f"yesterday close value:{yesterday}")
print(f"day before yesterday close value:{day_before_yesterday}")
print(f"{STOCK}: {up_or_down_points(yesterday, day_before_yesterday)}%")

news_api_key=os.environ.get("NEWS_API_KEY")
news_url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2024-05-24&sortBy=popularity&apiKey={news_api_key}'
response = requests.get(url=news_url, verify=False)
response.raise_for_status()
data = response.json()

print("######### NEWS DATA #############")
first_two_articles = list(data["articles"])[:2]
print("## 1st:")
print(first_two_articles[0]["title"])
print(first_two_articles[0]["description"])
print("## 2nd")
print(first_two_articles[1]["title"])
print(first_two_articles[1]["description"])
