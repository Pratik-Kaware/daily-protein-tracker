from fastapi import FastAPI
from pydantic import BaseModel
from src.log_nutrition import query_ollama
from utils.parse_nutrition import parse_nutrition
from fastapi.middleware.cors import CORSMiddleware


# FastAPI application setup
app = FastAPI()

# CORS policy 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model for User Input 

class NutritionQuery(BaseModel):
    txt: str

# Health Route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Indian Nutrition API"}

# Main POST endpoint to analyze nutrition
@app.post("/analyze")
def analyze_nutrition(query: NutritionQuery):
    response = query_ollama(query.txt)
    parsed = parse_nutrition(response)
    
    return {
        "food" : query.txt,
        "ollama_response": response.strip(),
        "parse_nutrition" : parsed
    }

