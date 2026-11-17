import csv
import json
import time
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
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / "run_log.csv"

    today = datetime.date.today().isoformat()
    scraped_at = datetime.datetime.now(datetime.timezone.utc).isoformat()

    for token in BOARDS:
        start = time.time()
        data = fetch_board(token)
        seconds = round(time.time() - start, 2)

        for job in data["jobs"]:
            job["board"] = token
            job["scraped_at"] = scraped_at

        path = out_dir / f"{token}_{today}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        write_header = not log_path.exists()
        with open(log_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(["date", "board", "jobs", "seconds"])
            writer.writerow([today, token, len(data["jobs"]), seconds])

        print(token, len(data["jobs"]), seconds)


if __name__ == "__main__":
    main()