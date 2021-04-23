import time
import sys

from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

import secrets  # from secrets.py in this folder
def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("div", {"id": "not_found_body"})
    return len(out_of_stock_divs) == 0


def setup_twilio_client():
    account_sid = "ACab1821674b982a5c2e816b20395e8523"
    auth_token = "a22cf29268a7c984ed67ed467d3b84b2"
    return Client(account_sid, auth_token)


def send_notification():
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        body="Your item is available for purchase. https://www.costco.ca/northrock-sr1-68.58-cm-%2827-in.%29-road-bike.product.100674087.html",
        from_="+16473751293",
        to="+16476075290"
    )
    twilio_client.messages.create(
        body="Your item is available for purchase. https://www.costco.ca/northrock-sr1-68.58-cm-%2827-in.%29-road-bike.product.100674087.html",
        from_="+16473751293",
        to="+16479065290"
    )
    print("success")


def check_inventory():
    url = "https://www.costco.ca/northrock-sr1-68.58-cm-%2827-in.%29-road-bike.product.100674087.html"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        send_notification()
        print("In stock")
        sys.exit()
    else:
        print("Out of stock")

while True:
    check_inventory()
    time.sleep(60)  # Wait a minute and try again