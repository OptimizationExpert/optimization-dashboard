import requests
import feedparser
import json
import os
from urllib.parse import urlencode
from collections import defaultdict
from datetime import datetime

# ================= CONFIG ================= #

ARXIV_QUERY = '("constraint programming" OR "cp-sat") AND (scheduling OR "vehicle routing" OR rostering OR logistics)'
GITHUB_QUERY = "OR-Tools CP-SAT vehicle routing scheduling optimization"

MEDIUM_FEEDS = [
    "https://medium.com/feed/tag/operations-research",
    "https://medium.com/feed/tag/optimization",
    "https://medium.com/feed/tag/supply-chain"
]

DB_FILE = "cp_db.json"

#BOT_TOKEN = os.environ["BOT_TOKEN"]
#CHAT_ID = os.environ["CHAT_ID"]
BOT_TOKEN = "8621241050:AAH_KM4oGAcRZD2yLLzsHZDffucZ58NBUZo"
CHAT_ID = "107917903"

KEYWORDS = {
    "cp-sat": 5,
    "or-tools": 5,
    "ortools": 5,
    "vehicle routing": 4,
    "vrp": 4,
    "scheduling": 3,
    "rostering": 3,
    "constraint programming": 3,
    "optimization": 1
}

# ================= CORE ================= #

def score(text):
    text = text.lower()
    return sum(w for k, w in KEYWORDS.items() if k in text)

def classify(text):
    text = text.lower()

    if "vrp" in text or "vehicle routing" in text:
        return "VRP"

    if "scheduling" in text or "rostering" in text:
        return "Scheduling"

    if "cp-sat" in text or "or-tools" in text or "constraint programming" in text:
        return "CP-SAT"

    return "Other"

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    return json.load(open(DB_FILE))

def save_db(db):
    json.dump(db, open(DB_FILE, "w"), indent=2)

def is_new(item, db):
    return item["id"] not in {x["id"] for x in db}

# ================= SOURCES ================= #

def fetch_arxiv():
    base = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{ARXIV_QUERY}",
        "start": 0,
        "max_results": 20
    }

    url = f"{base}?{urlencode(params)}"
    feed = feedparser.parse(url)

    out = []
    for e in feed.entries:
        text = e.title + " " + e.summary
        s = score(text)

        if s >= 3:
            out.append({
                "id": e.id,
                "type": "paper",
                "title": e.title,
                "link": e.link,
                "score": s
            })

    return out

def fetch_github():
    url = f"https://api.github.com/search/repositories?q={GITHUB_QUERY}&sort=updated"
    r = requests.get(url)
    data = r.json()

    out = []
    for repo in data.get("items", [])[:15]:
        text = (repo.get("description") or "") + repo["name"]
        s = score(text)

        if s >= 3:
            out.append({
                "id": repo["html_url"],
                "type": "repo",
                "title": repo["full_name"],
                "link": repo["html_url"],
                "score": s
            })

    return out

def fetch_medium():
    out = []

    for url in MEDIUM_FEEDS:
        feed = feedparser.parse(url)

        for e in feed.entries[:10]:
            text = e.title + " " + e.summary

            if (
                "or-tools" in text.lower()
                or "cp-sat" in text.lower()
                or "vehicle routing" in text.lower()
                or "scheduling" in text.lower()
            ):
                s = score(text)

                if s >= 5:
                    out.append({
                        "id": e.link,
                        "type": "medium",
                        "title": e.title,
                        "link": e.link,
                        "score": s
                    })

    return out

# ================= TELEGRAM ================= #

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    })

# ================= FORMAT ================= #

def build_message(items):
    grouped = defaultdict(list)

    for i in items:
        grouped[classify(i["title"])].append(i)

    icons = {
        "VRP": "🚚",
        "Scheduling": "📅",
        "CP-SAT": "⚙️",
        "Other": "📌"
    }

    msg = "🚀 <b>Industrial CP Intelligence Feed</b>\n\n"

    for cat in ["VRP", "Scheduling", "CP-SAT", "Other"]:
        if not grouped.get(cat):
            continue

        msg += f"{icons[cat]} <b>{cat}</b>\n"

        for i in sorted(grouped[cat], key=lambda x: x["score"], reverse=True)[:5]:
            msg += f"• [{i['score']}] {i['title']}\n{i['link']}\n\n"

    return msg

# ================= MAIN ================= #

def main():
    print("🔍 Running CP Intelligence Bot...")

    db = load_db()

    items = []
    items += fetch_arxiv()
    items += fetch_github()
    items += fetch_medium()

    new_items = [i for i in items if is_new(i, db)]
    new_items = items
    print(f"New items: {len(new_items)}")

    if new_items:
        msg = build_message(new_items)
        send_telegram(msg)
        db.extend(new_items)
        save_db(db)

    print("Done:", datetime.now())

# ================= RUN ================= #

if __name__ == "__main__":
    send_telegram("🚀 CP system running")
    main()