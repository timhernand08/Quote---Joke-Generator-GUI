import requests, json 
from memory import hasJoke, hasQuote
from cache import Cache


JOKE_API = 'https://icanhazdadjoke.com/'
QUOTE_API = 'https://zenquotes.io/api/quotes'
QUOTE_API2 = 'https://quote-slate-timothy-hernandezs-projects.vercel.app/api/quotes/random?count=5'

quote = Cache(False, 'quotes.json')
joke = Cache(False, 'jokes.json')

def get_quote() -> str:
	"""
	Gets an unused quote or resets the cache if all are used.
	Returns:
		str: The retrieved quote or an error message.
	"""
	quotes = quote.get_file()
	for item in quotes:
		try:
			if item["used"] == "False":
				return format_quote(item)
			elif quotes ==[]:
				break
		except KeyError:
			quote.delete_cache()
			return "No API calls available. Please try again later"

	return reset_cache(quote, QUOTE_API, QUOTE_API2, quote.get_backup())

def format_quote(item) -> str:
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

def reset_cache(file: Cache, primary_api, secondary_api:None, is_backup:False) -> str:
	file.create_cache(primary_api, secondary_api, is_backup)
	if file is quote:
		return get_quote()
	else:
		return get_joke()



def checker(value):
	"""
	Generates a quote or joke based on the input value and ensures uniqueness by checking against existing data.
	Args:
		value (str): The type of content to generate. 
					 Accepts "quote" for generating quotes or "joke" for generating jokes.
	Returns:
		str: The generated quote or joke. If the API fails or uniqueness cannot be ensured after 10 attempts, 
			 a fallback message is returned.
	Notes:
		- The function uses a backup API if the primary API fails.
		- If the same quote or joke is repeatedly generated, the function retries up to 10 times.
		- Prints warnings if the retry limit is reached.
	"""
	gen = ""
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
