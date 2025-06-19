# utils/logger.py

import csv
import os
from datetime import datetime

LOG_FILE = "data/logs/daily_log.csv"

def log_to_csv(food: str, nutrients: dict):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d")

    row = {
        "Date": date,
        "Food": food.strip(),
        "Protein (g)": nutrients.get("Protein (g)", ""),
        "Carbs (g)": nutrients.get("Carbs (g)", ""),
        "Fat (g)": nutrients.get("Fat (g)", ""),
        "Calories (kcal)": nutrients.get("Calories (kcal)", ""),
    }

    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
