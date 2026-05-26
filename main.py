import os
import requests
import random

BOT_TOKEN=os.getenv("BOT_TOKEN")
CHAT_ID=os.getenv("CHAT_ID")

url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

direction=random.choice(["LONG","SHORT"])

msg=f"""
🟡 XAUUSD RESEARCH

Bias:
{direction}

Reference:
3395

Risk Boundary:
3388

Target:
3412

Confidence:
72%

Reason:
Momentum + Regime
"""

requests.post(
url,
json={
"chat_id":CHAT_ID,
"text":msg
}
)

print("sent")
