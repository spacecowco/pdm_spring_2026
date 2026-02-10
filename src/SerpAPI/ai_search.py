from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

print("API Key loaded:", bool(api_key))
params = {
  "api_key": api_key,
  "engine": "google_ai_mode",
  "q": "Pratt & Whitney supply chain",
  "hl": "en",
  "gl": "us"
}

search = GoogleSearch(params)
results = search.get_dict()

with open("src/SerpAPI/output/ai_mode_results.json", "w") as f:
    json.dump(results, f, indent=2)