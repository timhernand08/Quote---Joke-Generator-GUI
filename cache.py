import json, requests
from utils import resource_path

QUOTE_API = 'https://zenquotes.io/api/quotes'
QUOTE_API2 = 'https://quote-slate-timothy-hernandezs-projects.vercel.app/api/quotes/random?count=5'
class Cache:
  def __init__(self, backup_val: bool, cache_file: str):
    self.backup_val = backup_val
    self.cache_file = cache_file

  def mark_used(self, id) -> None:
    with open(resource_path(self.cache_file), 'r', encoding="utf-8") as file:
      quotes = json.load(file)

    for item in quotes:
      if item['id'] == id:
          item['used'] = "True"

    with open(resource_path(self.cache_file), 'w', encoding="utf-8") as file:
      json.dump(quotes, file, indent=4)  

    print("Quote has been mark as used")

  def delete_cache(self) -> None:
    data = []
    with open(resource_path(self.cache_file), 'w', encoding="utf-8") as file:
      json.dump(data, file, indent=4)
    print("Cache deleted")

  def create_cache(self) -> list:
    print("Cache created")
    self.create_quote_cache()
    with open(resource_path(self.cache_file), 'r', encoding="utf-8") as file:
      return json.load(file)
    
  def get_file(self):
    try:
      with open(resource_path(self.cache_file), 'r') as file:
        files = json.load(file)
    except FileNotFoundError:
      print("JSON doesn't exist. Creating JSON")
      self.create_cache()
    return files

  def create_quote_cache(self):
    """
    Fetch quotes from one of the APIs and add them to a JSON file
    """
    if not self.backup_val:
      response = requests.get(QUOTE_API)
    else:
      response = requests.get(QUOTE_API2)
    json_data = json.loads(response.text)

    for index, item in enumerate(json_data):
      item["used"] = "False"
      if not self.backup_val:
          item["id"] = index
          

    with open(resource_path(self.cache_file), 'w', encoding="utf-8") as file:
      json.dump(json_data, file, indent=4)

    print("Cache updated with new quotes")

  def set_backup(self, value) -> None:
      self.backup_val = value

  def get_backup(self) -> bool:
    return self.backup_val
