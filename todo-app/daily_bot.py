import json
import datetime
import arxiv

KEYWORDS = [
    "constraint programming",
    "mixed integer linear programming",
    "MILP",
    "combinatorial optimization",
    "CP-SAT"
]

MAX_RESULTS = 15

def run():
    query = " OR ".join(KEYWORDS)
    results = []

    search = arxiv.Search(
        query=query,
        max_results=MAX_RESULTS,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    for paper in search.results():
        results.append({
            "title": paper.title,
            "url": paper.entry_id,
            "published": paper.published.strftime("%Y-%m-%d"),
            "summary": paper.summary[:300],
            "source": "arXiv"
        })

    output = {
        "generated_at": datetime.datetime.utcnow().isoformat(),
        "items": results
    }

    with open("data/items.json", "w") as f:
        json.dump(output, f, indent=2)


if __name__ == "__main__":
    run()