#scraper.py
from bs4 import BeautifulSoup
import requests
import logging
import os
import sys
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug.log')

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)
ERROR_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_log.txt')



def get_price(url):
    headers = {
        'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    cookies = {
        'birthtime' : '804556800',
        'mature_content': '1'
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    name_div = soup.find('div', class_='apphub_AppName')
    name_game = name_div.text
    purchase_area = soup.find('div', id='game_area_purchase')
    buy_box = purchase_area.find('div', id=lambda x: x and x.startswith('game_area_purchase_section_add_to_cart_')) if purchase_area else None
    discount_div = buy_box.find('div', class_='discount_block') if buy_box else None

    sections = purchase_area.find_all('div', class_='game_area_purchase_game')

    if discount_div is not None and int(discount_div['data-discount']) > 0:
        original_price_div = discount_div.find('div', class_='discount_original_price')
        original_text = original_price_div.text
        original_dollars = float(original_text.replace('$', ''))
        discount_cents = discount_div['data-price-final']
        discount_dollars = float(discount_cents) / 100
        return discount_dollars, name_game
    else:
        price_div = purchase_area.find('div', class_='game_purchase_price') if purchase_area else None
        if price_div is None:
             return None, name_game
        price_cents = price_div['data-price-final']
        price_dollars = float(price_cents) / 100
        return price_dollars, name_game


if __name__ == "__main__":
    url = "https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/"
    price, name = get_price(url)
    print(f"{name}: {price}$")