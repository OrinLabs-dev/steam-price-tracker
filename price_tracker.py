#price_tracker.py
from scraper import get_price
from database import insert_price, create_table, get_all_prices, get_last_price
from datetime import datetime
from config_example import TRACKED_GAMES, PRICE_DROP_THRESHOLD_PERCENT
from notifier import send_alert, send_chart
import schedule
import time
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
sys.stderr = open(ERROR_LOG_PATH, 'a')



def run():
    logging.info("run() called")
    create_table()
    for game in TRACKED_GAMES:
        time.sleep(3.5)
        try:
            url = game
            price, name = get_price(url)
            if price is None:
                continue
            old_price = get_last_price(url)
            now = datetime.now().strftime("%Y-%b-%d")
            insert_price(name, url, price, now)
            if old_price is None:
                continue
            percent_drop = ((old_price - price) / old_price) * 100
            if percent_drop >= PRICE_DROP_THRESHOLD_PERCENT:
                send_alert(name, round(percent_drop), url)
        except Exception as e:
            logging.error(f"Error scraping {game}: {e}")
    print(get_all_prices())


if __name__ == "__main__":
    schedule.every(1).days.do(run)
    schedule.every(30).days.do(send_chart)

    while True:
        remaining = schedule.idle_seconds()
        
        if remaining is not None and remaining > 0:
            mins, secs = divmod(int(remaining), 60)
            hours, mins = divmod(mins, 60)
            timer_format = f"Next run in: {hours:02d}:{mins:02d}:{secs:02d}"
            print(timer_format, end='\r', flush=True)
            
        schedule.run_pending()
        time.sleep(1)