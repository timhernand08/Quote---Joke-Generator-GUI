import requests, json 
from memory import hasJoke, hasQuote
from utils import resource_path
from cache import Cache


JOKE_API = 'https://icanhazdadjoke.com/'

quote = Cache(False, 'quotes.json')
#joke = Cache(False, 'jokes.json')

def get_quote() -> str:
	"""
	Retrieves an unused quote or resets the cache if all are used.
	Returns:
		str: The retrieved quote or an error message.
	"""
	quotes = quote.get_file()
	for item in quotes:
		try:
			if item["used"] == "False":
				return quoter(item)
			elif quotes ==[]:
				break
		except KeyError:
			quote.delete_cache()
			return "No API calls available. Please try again later"

	return reset_cache(quote)

def quoter(item) -> str:
	"""
	Formats a quote string and marks it as used.

	Args:
		item (dict): Contains quote details.

	Returns:
		str: Formatted quote.
	"""
	key_text, key_author = ('q', 'a') if not quote.get_backup() else ('quote', 'author')
	quote.mark_used(item['id'])
	return f"{item[key_text]}\r\n - {item[key_author]}"

def get_joke():
	headers = {
			"Accept": "application/json",
			"User-Agent": "Quote Joke Generator (https://github.com/timhernand08/Quote---Joke-Generator-GUI)"
	 }
	response = requests.get(JOKE_API, headers = headers)
	json_data = json.loads(response.text)
	joke = json_data['joke']
	return joke

def reset_cache(file: Cache) -> str:
	file.create_quote_cache()
	return get_quote()

global backup_q
#set_backup(backup_q := False)

def checker(value):
	gen = ""
	global backup_q 
	print(f"Using backup quote API? {quote.get_backup()}")

	if(value == "quote"):
			gen = get_quote()
			count = 0
			while hasQuote(gen):
					gen = get_quote()
					count+=1
					if count == 10:
							print("You're about to brick your PC homie")
							gen = "Could not connect to API. Please try again later"
							quote.set_backup(True)
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
	print(checker("quote"))
