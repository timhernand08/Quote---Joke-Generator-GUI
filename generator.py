import requests, json 
from memory import hasJoke, hasQuote

QUOTE_API = 'https://zenquotes.io/api/random'
JOKE_API = 'https://icanhazdadjoke.com/'

def get_quote():
  response = requests.get(QUOTE_API)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
  return quote

def get_joke():
   headers = {
      "Accept": "application/json",
      "User-Agent": "Quote Joke Generator (https://github.com/timhernand08/Quote---Joke-Generator-GUI)"
   }
   response = requests.get(JOKE_API, headers = headers)
   json_data = json.loads(response.text)
   joke = json_data['joke']
   return joke



def checker(value):
  gen = ""
  if(value == "quote"):
      gen = get_quote()
      count =0
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
          gen = get_joke()
          count+=1
          if count == 10:
              print("You're about to brick your PC homie")
              gen = "Could not connect to API. Please try again later"
              break
  return gen