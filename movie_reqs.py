import os

import pymongo
import requests
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client.sample_mflix
collection = db.movies

# docs = collection.find().limit(5)

# for doc in docs:
#   print(doc)

hf_access_token = os.getenv("HF_ACCESS_TOKEN")
model_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {hf_access_token}"}

def generate_embeddings(text: str) -> list[float]:
  response = requests.post(model_url, headers=headers, json={"inputs": text})
  if response.status_code != 200:
    raise ValueError(f"Request failed with statuc code {response.status_code}: {response.text}")
  
  return response.json()

# print(generate_embeddings("Tahmid is super cool"))

# * vectorize the plot property value and update the documents
# docs = collection.find({"plot": {"$exists": True}}).limit(100)
# for doc in docs:
#   doc["plot_hf_embeddings"] = generate_embeddings(doc["plot"])
#   collection.replace_one({"_id": doc["_id"]}, doc)

# * search
query = "powerful characters save the world"
results = collection.aggregate([
  {
    "$vectorSearch": {
      "queryVector": generate_embeddings(query),
      "path": "plot_hf_embeddings",
      "numCandidates": 100,
      "limit": 5,
      "index": "PlotSemanticSearch"
    }
  }
])

for doc in results:
  print(f"Movie name: {doc['title']}\nMovie plot: {doc['plot']}\n\n")