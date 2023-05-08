from pprint import pprint
from requests import get
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Corsair-Compatible-Installation-Multitasking-Compatibility/dp/B0B15DLTXJ/ref=sr_1_3?crid=344XB0EOM25GQ&keywords=gddr5%2Bsodimm&qid=1683562974&sprefix=gddr5%2Bsodimm%2Caps%2C103&sr=8-3&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&th=1"

response = get(url=URL)
