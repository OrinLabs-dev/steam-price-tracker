# Steam Price Tracker
A Python tool that tracks Steam game prices, sends Telegram alerts when prices go down, and creates price trend charts over time.

## About This Project
This project shows an automation workflow: web scraping, data storage, scheduled task automation, third-party API integration (Telegram), and data visualization. It is built as an example of automating a repetitive monitoring job. The same pattern can be used to track prices, availability, or other changing data on almost any website.

**Tech stack:** Python, `schedule` (task scheduling), Telegram Bot API, Matplotlib (charting)

## Features
- Collects prices for the Steam games being tracked using a User-Agent header and bypassing the age-gate cookie.
- Keeps price history in a local database.
- Automatically sends Telegram alerts when a Steam game's price drops by more than a chosen percentage.
- Alert messages show the discount percentage and a clickable link to the Steam store page.
- Makes price trend charts for each game using historical data.
- Runs on a daily schedule with a countdown timer, allowing it to stay running without supervision.

## How It Works
1. `scraper.py` retrieves the price for each tracked Steam game.
2. `database.py` saves that price with the date it was recorded.
3. `price_tracker.py` runs daily, compares the price to recent history, and checks whether the drop is larger than the set threshold.
4. If it is, `notifier.py` sends a Telegram alert that contains the game name, drop percentage, and Steam URL.
5. `chart.py` can be run alone to plot price trends over time for each tracked game.

## Setup
**Requirements:**
- Python 3.x
- A Telegram bot token and chat ID (for alerts)

**Steps:**
1. Clone the repository. Install the required packages. 
   - Use this command to install requirements ```bash
pip install -r requirements.txt
```
2. Open `config.py` and complete the following fields:
   - Your Telegram bot token and chat ID
   - `PRICE_DROP_THRESHOLD_PERCENT` (currently set to `12`; adjust to your preference)
   - The Steam games you want to track (see "Adding Games" below)

## Adding Games to Track
Games are added by typing their Steam store URL into `config.py`.

> **Planned improvement:** switching to tracking games by their Steam App ID instead of full URLs, which will make adding new games faster and less error-prone.

## Usage
Run the tracker:
```bash
python price_tracker.py
```
This starts the daily scheduler; it will check prices once each day and automatically send a Telegram alert if a tracked game's price drops past the threshold. Leave it running in the background, or set it up as a service, for continuous tracking.

To generate a price trend chart:
```bash
python chart.py
```
Note: charts become more useful after a few days of price history have been collected.

## Roadmap
- [ ] Track games by Steam App ID instead of manual URL entry
- [ ] Multi-site support (Epic Games Store, GOG)

## Notes
This project is easy to adapt. The scraping, alerting, and scheduling pattern used here can be extended to track prices or data changes on other sites and platforms.
