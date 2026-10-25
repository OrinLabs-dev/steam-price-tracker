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


TELEGRAM_BOT_TOKEN = 'YOUR-BOT-TOKEN-HERE'
chat_id = 'YOUR-CHATID-HERE'

TRACKED_GAMES = [
    "https://store.steampowered.com/app/4080220/EA_SPORTS_FC_27/",
    "https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/",
    "https://store.steampowered.com/app/4704690/MECCHA_CHAMELEON/",
    "https://store.steampowered.com/app/3240220/Grand_Theft_Auto_V_Enhanced/",
    "https://store.steampowered.com/app/3241660/REPO/",
    'https://store.steampowered.com/app/4656000/BOMBANANA/',
    
]

PRICE_DROP_THRESHOLD_PERCENT = 12  #Set to desired discount threshold at which the alert will be sent.
