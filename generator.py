import requests, json 
from memory import hasJoke, hasQuote

QUOTE_API = 'https://zenquotes.io/api/random'
JOKE_API = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,explicit'

def get_quote():
  response = requests.get(QUOTE_API)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
  return quote

def get_joke():
  response = requests.get(JOKE_API)
  json_data = json.loads(response.text)
  try:
    joke = json_data['joke']
    return joke
  except:
    setup = json_data['setup']
    delivery = json_data['delivery']
  return setup + "\n" + delivery

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
  elif (value == "joke"):
      gen = get_joke()
      count =0
      while hasJoke(gen):
          gen = get_joke()
          count+=1
          if count == 10:
              print("You're about to brick your PC homie")
  return gen