import re

def average_range(text):
    """Extract average from values like '10-12 grams' or 'approximately 120–150'"""
    match = re.search(r"(\d+\.?\d*)\s*(?:–|-)\s*(\d+\.?\d*)", text)
    if match:
        low, high = float(match.group(1)), float(match.group(2))
        return round((low + high) / 2, 1)
    match = re.search(r"(\d+\.?\d*)", text)
    if match:
        return float(match.group(1))
    return None

def parse_nutrition(response: str) -> dict:
    nutrients = {
        "Protein (g)": None,
        "Carbs (g)": None,
        "Fat (g)": None,
        "Calories (kcal)": None,
    }

    lines = response.lower().splitlines()

    for line in lines:
        if "protein" in line:
            nutrients["Protein (g)"] = average_range(line)
        elif "carbohydrate" in line or "carbs" in line:
            nutrients["Carbs (g)"] = average_range(line)
        elif "fat" in line:
            nutrients["Fat (g)"] = average_range(line)
        elif "calories" in line:
            nutrients["Calories (kcal)"] = average_range(line)

    return nutrients
