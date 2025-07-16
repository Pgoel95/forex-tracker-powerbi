import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

def scrape_xrates(date_str, base="INR", amount=1):
    url = f"https://www.x-rates.com/historical/?from={base}&amount={amount}&date={date_str}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "html.parser")

    table = soup.find("table", class_="ratesTable")
    rows = []

    for tr in table.find_all("tr")[1:]:
        cols = tr.find_all("td")
        if len(cols) >= 3:
            currency = cols[0].get_text(strip=True)
            direct_rate = float(cols[1].get_text(strip=True))
            inverse_rate = float(cols[2].get_text(strip=True))
            rows.append({
                "Date": date_str,
                "Currency": currency,
                "INR to Currency": direct_rate,
                "Currency to INR": inverse_rate
            })
    return rows

def get_last_6_months_data():
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=180)
    dates = pd.date_range(start=start_date, end=end_date, freq='D').strftime("%Y-%m-%d")
    all_data = []

    for d in dates:
        print(f"Fetching {d}...")
        try:
            daily_data = scrape_xrates(d)
            all_data.extend(daily_data)
        except Exception as e:
            print(f"Failed on {d}: {e}")

    df = pd.DataFrame(all_data)
    df.to_csv("exchange_rates_6months.csv", index=False)
    print("CSV saved: exchange_rates_6months.csv")

if __name__ == "__main__":
    get_last_6_months_data()
