from smtplib import SMTP
from os import environ
from requests import get
from bs4 import BeautifulSoup

EMAIL = environ["user"]
TO_EMAIL = environ["to_email"]
PASSWORD = environ["password"]
URL = "https://pcpartpicker.com/product/gjpQzy/corsair-vengeance-16-gb-2-x-8-gb-ddr5-4800-sodimm-cl40-memory-cmsx16gx5m2a4800c40"

response = get(
    url=URL,
    timeout=10,
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
        "Accept-Language": "en-US,en;q=0.5",
        },
    )
soup = BeautifulSoup(response.text, "html.parser")

# This finds the class that PC Part Picker seems to use for the lowest price
# and converts it to a floating point number.
price_text = float(soup.find(class_="td__base priority--2").text.split("$")[1])

# print(price_text)

# $60 is the target price.
# This if statement sends an email once the price gets below the target. ($60, in this case.)
if price_text <= 60:
    with SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(
            EMAIL,
            PASSWORD
            )
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Buy the thing.\n\nBuy the thing. {URL}"
            )
