import pandas as pd
import json
import re
import os

# Create a function to clean numeric values
def clean_value(val):
    if pd.isna(val) or isinstance(val, float):
        return None
    val = str(val)
    val = re.sub(r"[a-zA-Z%()\n]", "", val)  # Remove letters, %, (), and newlines
    val = val.replace(",", "").strip()
    if val == "":
        return None
    try:
        return float(val)
    except ValueError:
        return None

# Set input/output file paths
input_csv_path = os.path.join("data", "raw", "Indian_Food_DF.csv")
output_jsonl_path = os.path.join("data", "preprocessed", "Indian_Food_DF.jsonl")

# Read the CSV
df = pd.read_csv(input_csv_path)

# Write to JSONL
with open(output_jsonl_path, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        food = str(row.get("name", "")).strip()
        food = food.encode("ascii", "ignore").decode()  # Remove fancy Unicode characters
        if not food:
            continue

        energy = clean_value(row.get("nutri_energy", ""))
        fat = clean_value(row.get("nutri_fat", ""))
        satu_fat = clean_value(row.get("nutri_satuFat", ""))
        carbs = clean_value(row.get("nutri_carbohydrate", ""))
        sugar = clean_value(row.get("nutri_sugar", ""))
        fiber = clean_value(row.get("nutri_fiber", ""))
        protein = clean_value(row.get("nutri_protein", ""))
        salt = clean_value(row.get("nutri_salt", ""))

        if all(v is None for v in [energy, fat, carbs, protein]):
            continue

        parts = []
        if energy is not None:
            parts.append(f"{energy} kcal")
        if protein is not None:
            parts.append(f"{protein}g protein")
        if fat is not None:
            parts.append(f"{fat}g fat")
        if satu_fat is not None:
            parts.append(f"{satu_fat}g saturated fat")
        if carbs is not None:
            parts.append(f"{carbs}g carbs")
        if sugar is not None:
            parts.append(f"{sugar}g sugar")
        if fiber is not None:
            parts.append(f"{fiber}g fiber")
        if salt is not None:
            parts.append(f"{salt}g salt")

        nutrition_str = ", ".join(parts)
        prompt = f"User: What is the nutrition in 1 serving of {food}?"
        response = f"Assistant: 1 serving of {food} contains {nutrition_str}."

        f.write(json.dumps({"prompt": prompt, "response": response}) + "\n")
