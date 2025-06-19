```markdown
# 🥗 Indian Nutrition Tracker - AI Nutritionist

**Transform your fitness journey with an AI nutritionist that understands Indian food.**

> Track your protein and calories easily by just describing your meal. Powered by a fine-tuned, locally hosted LLaMA model via Ollama.

---

## 🌟 Overview
This project solves the daily pain of Googling nutrition info for every Indian meal — from "3 rotis" to "1 katori dal". It uses a conversational LLM to extract meaningful macronutrient data from natural language and logs it locally.

---

## 🚀 Current Progress

**✅ Phase 1: CLI MVP**
- CLI-based logger: `log_nutrition.py`
- Integrated with local LLaMA model via `Ollama`
- Basic regex parser for protein/carb/fat/kcal detection
- CSV logging: `daily_log.csv`

**🚧 Phase 2: Enhanced Parsing**
- Modularized `parse_nutrition.py` with cleaner value extraction
- Fallback to fuzzy parsing when one or more macros are missing
- Error handling and logging framework via `logger.py`

**🔜 Phase 3: Visualization & Usability**
- Interactive Jupyter dashboards (macros over time)
- More structured input/output handling
- Support for food aliases, regional synonyms (e.g., “katori” → “cup”)
- Streamlit frontend or FastAPI wrapper

---

## 🍳 What It Does

- 🤖 **Conversational AI**: Describe your meal naturally, e.g. _"I had 2 rotis and 1 cup dal"_
- 🔍 **Parses Approximate Nutrition**: Uses regex + NLP cues to extract values from LLM response
- 📦 **Logs to CSV**: `daily_log.csv` logs everything with timestamp
- 🧠 **Locally Hosted LLM**: Secure, private food tracking
- 🇮🇳 **Built for Indian Food**: Recognizes local food names and portions

---

## 📂 Project Structure

```

daily-protein-tracker/
├── data/
│   ├── raw/
│   └── preprocessed/
├── ollama\_finetune/               # JSONL and Modelfile for fine-tuning
├── src/
│   └── log\_nutrition.py           # CLI entry point
├── utils/
│   ├── parse\_nutrition.py         # Nutrition parser
│   ├── logger.py                  # CSV logging utility
│   └── csv\_to\_json.py             # Convert CSV to JSONL for model training
├── daily\_log.csv                  # Nutritional logs
├── .gitignore
└── README.md

````

---

## 🧪 Sample CLI Session

```bash
$ python src/log_nutrition.py

🍽️ Indian Nutrition CLI (type 'exit' to quit)

👤 You: I ate 3 rotis and 1 cup sabzi
🤖 Response:
3 rotis: 9g protein, 45g carbs
1 cup sabzi: 2g protein, 20g carbs, 1g fat
Total: ~11g protein, 65g carbs, 1g fat, 350 kcal

✅ Logged to daily_log.csv
````

Corresponding CSV output:

```csv
Date,Food,Protein (g),Carbs (g),Fat (g),Calories (kcal)
2025-06-19,I ate 3 rotis and 1 cup sabzi,11.0,65.0,1.0,350.0
```

If any macro is not parsed:

```csv
2025-06-19,I ate 4 pieces of chicken tandoor today,,,,
```

---

## 🌀 Setup Instructions

### 🔧 Prerequisites

* Python 3.8+
* [Ollama](https://ollama.com) installed and running
* Fine-tuned LLaMA model (your `.jsonl` training data should be in `ollama_finetune/`)

### 🔨 Installation

```bash
git clone https://github.com/yourusername/daily-protein-tracker.git
cd daily-protein-tracker

pip install -r requirements.txt
```

### ▶️ Run the CLI

```bash
python src/log_nutrition.py
```

---

## 📈 Roadmap

| Milestone | Description                               | Status     |
| --------- | ----------------------------------------- | ---------- |
| Phase 1   | CLI-based LLM integration                 | ✅ Done     |
| Phase 2   | Stable parser with better extraction      | 🟡 Ongoing |
| Phase 3   | Jupyter/Streamlit-based dashboard         | 🔜 Planned |
| Phase 4   | REST API (FastAPI) + container deployment | 🔜 Planned |

---

## 🔍 Example Prompts & Challenges

### Good Prompt

> "I had 2 rotis, 1 cup chana, 1 bowl rice"

→ Returns accurate breakdown

### Edge Prompt

> "I had a masala dosa, coffee, and chutney"

→ Parser may miss fat or calories → improvements ongoing

---

## 💡 Vision

> A personal AI nutritionist that works offline, understands your food culture, and helps you hit your fitness goals — without needing MyFitnessPal or international food databases.

---

## 🛠️ Contributing

We welcome PRs and ideas! Here’s how you can help:

* Add parsing rules in `parse_nutrition.py`
* Create more training samples in JSONL for fine-tuning
* Help clean and normalize food log data
* Suggest UI ideas for Streamlit dashboards

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

* LLaMA model team
* Ollama for amazing local LLM serving
* Gymbros and home chefs testing Indian meal queries
* ChatGPT (OpenAI) for coding + logic pairing

---

## 📧 Contact

**📬 [nutrition.tracker.help@gmail.com](mailto:nutrition.tracker.help@gmail.com)**

For bugs, ideas, or to showcase your logs, feel free to reach out!

```
