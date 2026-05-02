import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://optimizationexpert.github.io/optimization-dashboard"
KEYWORDS = ["constraint", "cp", "cp-sat", "optaplanner", "timefold",
            "constraint programming", "milp", "optimal routing"]

def fetch_topics():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")

    # adjust selector after inspecting page
    items = soup.find_all("a")

    topics = []
    for item in items:
        text = item.get_text(strip=True).lower()
        if any(k in text for k in KEYWORDS):
            topics.append(text)

    return list(set(topics))

def load_old():
    if not os.path.exists("topics.json"):
        return []
    return json.load(open("topics.json"))

def save(topics):
    json.dump(topics, open("topics.json", "w"))

def main():
    new_topics = fetch_topics()
    old_topics = load_old()

    diff = [t for t in new_topics if t not in old_topics]

    if diff:
        print("NEW CP TOPICS:")
        for d in diff:
            print("-", d)
        # send to Slack/email here
    else:
        print("No new CP topics today")

    save(new_topics)

if __name__ == "__main__":
    main()