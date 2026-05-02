# cp_monitor.py

import requests
import feedparser
import json
import os
from datetime import datetime
import feedparser
from urllib.parse import urlencode
# ---------------- CONFIG ---------------- #

ARXIV_QUERY = """
("constraint programming" OR "cp-sat")
AND (scheduling OR "vehicle routing" OR rostering OR logistics)
"""
MEDIUM_FEEDS = [
    "https://medium.com/feed/tag/operations-research",
    "https://medium.com/feed/tag/optimization",
    "https://medium.com/feed/tag/supply-chain",
    "https://medium.com/feed/tag/mathematical-optimization"
]
GITHUB_QUERY = """
OR-Tools CP-SAT vehicle routing scheduling optimization
"""
DB_FILE = "cp_monitor_db.json"

# Industrial CP keywords (weighted)
KEYWORDS = {
    "cp-sat": 5,
    "or-tools": 5,
    "ortools": 5,
    "vehicle routing": 4,
    "vrp": 4,
    "scheduling": 3,
    "rostering": 3,
    "constraint programming": 3,
    "milp": 1,
    "optimization": 1
}

# ---------------- UTILS ---------------- #

def score(text):
    text = text.lower()
    return sum(weight for k, weight in KEYWORDS.items() if k in text)

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    return json.load(open(DB_FILE))

def save_db(data):
    json.dump(data, open(DB_FILE, "w"), indent=2)

def is_new(item, db):
    return item["id"] not in {x["id"] for x in db}

# ---------------- ARXIV ---------------- #



def fetch_arxiv():
    base_url = "http://export.arxiv.org/api/query"

    query = "cp-sat OR constraint programming OR vehicle routing OR scheduling"

    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": 20
    }

    url = f"{base_url}?{urlencode(params)}"

    feed = feedparser.parse(url)

    results = []
    for entry in feed.entries:
        text = entry.title + " " + entry.summary
        s = score(text)

        if s >= 4:
            results.append({
                "id": entry.id,
                "type": "paper",
                "title": entry.title,
                "link": entry.link,
                "score": s
            })

    return results

# ---------------- GITHUB ---------------- #

def fetch_github():
    url = f"https://api.github.com/search/repositories?q={GITHUB_QUERY}&sort=updated"
    r = requests.get(url)
    data = r.json()

    results = []
    for repo in data.get("items", [])[:15]:
        text = (repo.get("description") or "") + repo["name"]
        s = score(text)

        if s >= 4:
            results.append({
                "id": repo["html_url"],
                "type": "repo",
                "title": repo["full_name"],
                "link": repo["html_url"],
                "score": s
            })

    return results

# ---------------- MEDIUM ---------------- #

def fetch_medium():
    results = []

    for url in MEDIUM_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:15]:
            text = entry.title + " " + entry.summary

            s = score(text)

            # Medium is noisy → stricter filtering
            if s >= 5 and (
                "or-tools" in text.lower()
                or "cp-sat" in text.lower()
                or "vehicle routing" in text.lower()
                or "scheduling" in text.lower()
                or "optimization" in text.lower()
            ):
                results.append({
                    "id": entry.link,
                    "type": "medium",
                    "title": entry.title,
                    "link": entry.link,
                    "score": s
                })

    return results
# ---------------- MAIN ---------------- #

def main():
    print("🔍 Running Industrial CP Monitor...\n")

    db = load_db()

    items = []
    items += fetch_arxiv()
    items += fetch_github()
    items += fetch_medium()

    # 👇 ADD THIS BLOCK
    print(f"\n📊 Total fetched items: {len(items)}\n")
    for item in sorted(items, key=lambda x: x["score"], reverse=True):
        icon = "📄" if item["type"] == "paper" else "💻"
        print(f"{icon} [{item['score']}] {item['title']}")
        print(f"   {item['link']}\n")

    # keep only new
    new_items = [x for x in items if is_new(x, db)]
# ---------------- RUN ---------------- #

if __name__ == "__main__":
    main()