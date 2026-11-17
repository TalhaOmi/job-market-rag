import json
import datetime
from pathlib import Path

import requests

BOARDS = ["databricks", "cardata", "guidepoint", "grafanalabs"]
BASE_URL = "https://boards-api.greenhouse.io/v1/boards/{token}/jobs"


def fetch_board(token):
    url = BASE_URL.format(token=token)
    response = requests.get(url, params={"content": "true"}, timeout=30)
    response.raise_for_status()
    return response.json()

def main():
    out_dir = Path("data/raw")
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()

    for token in BOARDS:
        data = fetch_board(token)
        path = out_dir / f"{token}_{today}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        print(token, len(data["jobs"]))


if __name__ == "__main__":
    main()