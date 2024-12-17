from langdetect import detect
from serpapi import GoogleSearch
import os

print(detect("Jesus is Lord"))

toSearch = "Tech"

params = {
    "engine": "google",
    "q": toSearch,
    "api_key": "dc3a634cd2e9369e916094e883d0084077848098e6fd71caee74114aec17850e",
}


search = GoogleSearch(params)

results = search.get_dict()

print(results["organic_results"])
# for result in results["organic_results"]:
#   print(f"Title: {result['title']}\nSummary: {result['snippet']}\nLink: {result['link']}\n")