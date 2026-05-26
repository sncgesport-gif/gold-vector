import os
import requests

BOT = os.getenv("BOT_TOKEN")
CHAT = os.getenv("CHAT_ID")
API = os.getenv("ALPHA_KEY")

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT}/sendMessage",
        json={
            "chat_id": CHAT,
            "text": msg
        }
    )

url = (
"https://www.alphavantage.co/query?"
"function=TIME_SERIES_INTRADAY"
"&symbol=XAUUSD"
"&interval=15min"
f"&apikey={API}"
)

r = requests.get(url).json()

try:
    data = r["Time Series (15min)"]

    latest = list(data.values())[0]

    close = latest["4. close"]
    high = latest["2. high"]
    low = latest["3. low"]

    msg=f"""
🟡 XAUUSD LIVE

Price:
{close}

Range:
{low} → {high}

Research:
Live market fetched

Status:
ONLINE
"""

except Exception:

    msg="""
❌ XAUUSD fetch failed
Check API key
"""

send(msg)

print("done")
