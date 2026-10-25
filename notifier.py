#notifier.py
from config_example import TELEGRAM_BOT_TOKEN, chat_id
import requests
from chart import chart
import os
import logging
import sys
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug.log')

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)
ERROR_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'error_log.txt')

chart_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.png')


def send_alert(name_game, percent_drop, game_url):
    
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': f'{name_game} has dropped by {percent_drop}%, Claim it before the offer ends! \nGo claim it here: {game_url}'
    }
    requests.post(url, data=data)

def send_chart():
    chart()
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
    data = {
        'chat_id' : chat_id,
        'caption': f"Here's the monthly prices chart, Take a look at prices over the past month"
    }
    with open(chart_path, 'rb') as f:
        requests.post(url, data=data, files={'photo': f})