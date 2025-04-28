import json, requests
from utils import resource_path

QUOTE_API = 'https://zenquotes.io/api/quotes'
QUOTE_API2 = 'https://quote-slate-timothy-hernandezs-projects.vercel.app/api/quotes/random?count=5'

global backup_q

def mark_used(id):
  with open(resource_path('quotes.json'), 'r', encoding="utf-8") as file:
    quotes = json.load(file)

  for item in quotes:
     if item['id'] == id:
        item['used'] = "True"

  with open(resource_path('quotes.json'), 'w', encoding="utf-8") as file:
    json.dump(quotes, file, indent=4)  

  print("Quote has been mark as used")



def delete_cache():
  data = []
  with open(resource_path('quotes.json'), 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)
  print("Cache deleted")

def create_cache() -> list:
  print("Cache created")
  quote_cache()
  with open(resource_path('quotes.json'), 'r', encoding="utf-8") as file:
    return json.load(file)

def quote_cache():
  """
  Fetch quotes from one of the APIs and add them to a JSON file
  """
  global backup_q
  if not backup_q:
    response = requests.get(QUOTE_API)
  else:
    response = requests.get(QUOTE_API2)
  json_data = json.loads(response.text)

  for index, item in enumerate(json_data):
     item["used"] = "False"
     if not backup_q:
        item["id"] = index
        

  with open(resource_path('quotes.json'), 'w', encoding="utf-8") as file:
    json.dump(json_data, file, indent=4)

  print("Cache updated with new quotes")

def set_backup(value):
    global backup_q
    backup_q = value

