#chart.py
from database import get_all_prices
from scraper import get_price
import matplotlib.pyplot as plt
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



def chart():

    fig, ax = plt.subplots()
    chart_data = {}
    for row in get_all_prices():
        name = row[1]
        date = row[4]
        price = row[3]
        if name in chart_data:
            pass
        else:
            chart_data[name] = []
        chart_data[name].append((date, price))
    for game_name, records in chart_data.items():
        dates, prices = map(list, zip(*records))
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.plot(dates, prices, label=game_name)

    plt.legend(frameon=True, loc='best', bbox_to_anchor=(0.5, 1.02))
    plt.tight_layout()
    CHART_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.png')   
    plt.savefig(CHART_PATH)
    print(chart_data)
if __name__ == '__main__':
    chart()