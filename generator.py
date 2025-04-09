import requests, json 
from memory import hasJoke, hasQuote

QUOTE_API = 'https://zenquotes.io/api/random'
QUOTE_API2 = 'https://quote-slate-timothy-hernandezs-projects.vercel.app/api/quotes/random?count=5'
JOKE_API = 'https://icanhazdadjoke.com/'

def get_quote():
  response = requests.get(QUOTE_API)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
  return quote

def get_quote2():
  with open('quotes.json', 'r') as file:
    quotes = json.load(file)

  for item in quotes:
    try:
      if item["used"] == "False":
        quote = item['quote'] + "\r\n - " + item['author']
        mark_used(item['id'])
        return quote
    except KeyError:
      delete_cache()
      return "No API calls available. Please try again later"

  return reset_cache()

def get_joke():
   headers = {
      "Accept": "application/json",
      "User-Agent": "Quote Joke Generator (https://github.com/timhernand08/Quote---Joke-Generator-GUI)"
   }
   response = requests.get(JOKE_API, headers = headers)
   json_data = json.loads(response.text)
   joke = json_data['joke']
   return joke

def mark_used(id):
  with open('quotes.json', 'r') as file:
    quotes = json.load(file)

  for item in quotes:
     if item['id'] == id:
        item['used'] = "True"

  with open('quotes.json', 'w', encoding="utf-8") as file:
    json.dump(quotes, file, indent=4)  

  print("Quote has been mark as used")

def reset_cache():
  quote_cache()
  return get_quote2()

def delete_cache():
  data = []
  with open('quotes.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)
  print("Cache deleted")

def quote_cache():
  response = requests.get(QUOTE_API2)
  json_data = json.loads(response.text)

  for item in json_data:
     item["used"] = "False"

  with open('quotes.json', 'w', encoding="utf-8") as file:
    json.dump(json_data, file, indent=4)

  print("Cache updated with new quotes")

global backup_q
backup_q = False

def checker(value):
  gen = ""
  global backup_q 
  print(f"Using backup API? {backup_q}")

  if(value == "quote"):
      if(not backup_q):
        gen = get_quote2()
      else:
        backup_q = True
        gen = get_quote()
      count = 0
      while hasQuote(gen):
          gen = get_quote()
          count+=1
          if count == 10:
              print("You're about to brick your PC homie")
              gen = "Could not connect to API. Please try again later"
              break
  elif (value == "joke"):
      gen = get_joke()
      count =0
      while hasJoke(gen):
          print(f"The quote is '{gen}' and this exists")
          gen = get_joke()
          count+=1
          if count == 10:
              print("You're about to brick your PC homie")
              gen = "Could not connect to API. Please try again later"
              break
  return gen

if __name__ == "__main__":
  print(get_quote2())
  #quote_cache()