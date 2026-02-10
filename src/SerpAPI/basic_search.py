from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

print("API Key loaded:", bool(api_key))

params = {
  "engine": "google",  # Use the Google search engine
  "q": "Pratt & Whitney supply chain",  # Search query string
  "location": "United States",  # Geographical location to influence search results
  "hl": "en",  # Language of the search results (English)
  "gl": "us",  # Country of the search (United States)
  "num": 20,  # Number of results to return per page
  "tbm": "nws",   # news articles for disruption or announcements
  "tbs": "qdr:y",   # last year only
  "api_key": api_key  # SerpAPI key
}

search = GoogleSearch(params)
results = search.get_dict()

with open("src/SerpAPI/output/basic_search_results.json", "w") as f:
    json.dump(results, f, indent=2)