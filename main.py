import requests, json 
from memory import storeData, hasJoke, hasQuote, update_time_trigger
from initdb import initialize_db

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



quote = get_quote()
joke = get_joke()
print(quote + "\n" + joke + "\n")
initialize_db()
update_time_trigger("quotes")
update_time_trigger("jokes")

user = input("Please enter if you want a new quote or joke. Or enter 'done': ")
while(user != "done"):
  if(user == "quote"):
    quote = get_quote()
    count =0
    while hasQuote(quote):
      quote = get_quote()
      count+=1
      if count == 10:
        print("You're about to brick your PC homie")
        break
    print(quote)
  if (user == "joke"):
    joke = get_joke()
    while hasJoke(joke):
      joke = get_joke()
      count+=1
      if count == 10:
        print("You're about to brick your PC homie")
        break
    print(joke)  
  elif(user == "help"):
    print("Whoa you entered a secret menu! Nothing has been programmed for this yet. I love you, bye.")
  user = input("\nMake a new request: ")

storeData(quote, joke)
print(f"\nQuote: {quote}")
print(f"Joke: {joke}")
end = input("\nData has been saved to memory. Thank you for using the Quote & Joke Generator!\nPress 'enter' key to exit.")
