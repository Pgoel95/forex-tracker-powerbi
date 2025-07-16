# forex-tracker-powerbi

This project automates the collection of currency exchange rates, stores them in a CSV file, and presents them visually using Power BI. The data is updated daily via Windows Task Scheduler.

# Features

- Scrapes live currency exchange data from x-rates.com
- Automates daily data collection using Python and Task Scheduler
- Stores data in a '.CSV' file for historical tracking
- Builds a Power BI report to visualize exchange trends and % change
- Dynamic visuals, slicers, conditional formatting, and emoji indicators

# Technologies Used
- Python (Requests, BeautifulSoup, Pandas)
- Windows Task Scheduler
- Power BI
- Github

# Folder Structure
- `Scripts/`: Python scraping script + Task Scheduler instructions
- `Data/`: CSV file (auto-updated)

# How it Works
1. **Scraping**: `currency_scraper.py` pulls data daily from [https://www.x-rates.com/historical/?from=INR&amount=1&date=2025-07-16]
2. **Automation**: Task Scheduler triggers the script daily
3. **Storage**: Data saved to `exchange_rates.csv` inside `data/` folder
4. **Visualization**: Power BI connects to the CSV and refreshes visuals

