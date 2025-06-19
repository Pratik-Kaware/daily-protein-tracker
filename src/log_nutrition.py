# src/log_nutrition.py
import os 
import sys
import subprocess
from datetime import datetime
from utils.parse_nutrition import parse_nutrition
from utils.logger import log_to_csv

MODEL_NAME = "nutri-llm"

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def query_ollama(user_input: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME],
            input=user_input.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return result.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Ollama failed: {e}")
        return ""

def main():
    print("🍽️ Indian Nutrition CLI (type 'exit' to quit)")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        print("🤖 Thinking...")
        response = query_ollama(user_input)
        print("🧠 Response:\n", response)

        nutrients = parse_nutrition(response)
        log_to_csv(user_input, nutrients)
        print("✅ Logged to CSV")

if __name__ == "__main__":
    main()
