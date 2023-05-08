# from pprint import pprint
from requests import get
from bs4 import BeautifulSoup

URL = "https://drop.com/buy/massdrop-x-sennheiser-hd-58x-jubilee-headphones"

response = get(
    url=URL,
    timeout=10,
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
        "Accept-Language": "en-US,en;q=0.5",
        },
    )
soup = BeautifulSoup(response.text, "html.parser")

price_text = soup.find(class_="wdio__price Text__text__PazWx Text__type--price__1mumP")

print(price_text)
