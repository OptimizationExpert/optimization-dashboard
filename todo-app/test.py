import requests

BOT_TOKEN = "your_token_here"
CHAT_ID = "107917903"
BOT_TOKEN = "8621241050:AAH_KM4oGAcRZD2yLLzsHZDffucZ58NBUZo"
CHAT_ID = "107917903"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "🚀 TEST MESSAGE"
})

print(r.status_code)
print(r.text)