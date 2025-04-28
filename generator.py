import requests, json 
from memory import hasJoke, hasQuote
from cache import quote_cache, delete_cache, mark_used, set_backup, create_cache


JOKE_API = 'https://icanhazdadjoke.com/'


def get_quote() -> str:
	try:
		with open('quotes.json', 'r') as file:
			quotes = json.load(file)
	except FileNotFoundError:
		print("JSON doesn't exist. Creating JSON")
		quotes = create_cache()
		

	for item in quotes:
		try:
			if item["used"] == "False":
				return quoter(item)
			elif quotes ==[]:
				break
		except KeyError:
			delete_cache()
			return "No API calls available. Please try again later"

	return reset_cache()

def quoter(item) -> str:
	if not backup_q:
		quote = item['q'] + "\r\n - " + item['a']
	else:
		quote = item['quote'] + "\r\n - " + item['author']
	mark_used(item['id'])
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

def reset_cache() -> str:
	quote_cache()
	return get_quote()

global backup_q
set_backup(backup_q := False)

def checker(value):
	gen = ""
	global backup_q 
	print(f"Using backup API? {backup_q}")

	if(value == "quote"):
			gen = get_quote()
			count = 0
			while hasQuote(gen):
					gen = get_quote()
					count+=1
					if count == 10:
							print("You're about to brick your PC homie")
							gen = "Could not connect to API. Please try again later"
							set_backup(backup_q := True)
							break
	elif (value == "joke"):
			gen = get_joke()
			count =0
			while hasJoke(gen):
					print(f"The joke is '{gen}' and this exists")
					gen = get_joke()
					count+=1
					if count == 10:
							print("You're about to brick your PC homie")
							gen = "Could not connect to API. Please try again later"
							break
	return gen

if __name__ == "__main__":
	print(get_quote())
	#quote_cache()