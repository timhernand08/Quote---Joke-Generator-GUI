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
    self.create_cache()
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

  def create_cache(self, primary_api, backup_api=None, is_backup=False):
    """
    Fetch data from the given API and adds them to a JSON file
    """
    api_url = backup_api if is_backup and backup_api else primary_api
    try:
      response = requests.get(api_url)
      response.raise_for_status()
      json_data = json.loads(response.text)
    except requests.ResquestException as e:
      print(f"Error fetching data from {api_url}: {e}")
      return
    
    for index, item in enumerate(json_data):
        item["used"] = "False"
        if not is_backup and primary_api == QUOTE_API: 
            item["id"] = index
          

    with open(resource_path(self.cache_file), 'w', encoding="utf-8") as file:
      json.dump(json_data, file, indent=4)

    print(f"Cache updated with new data from {api_url}") 

  def set_backup(self, value) -> None:
      self.backup_val = value

  def get_backup(self) -> bool:
    return self.backup_val
