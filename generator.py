import requests, json 
from memory import hasJoke, hasQuote
from cache import Cache
from api_handler import APIS, format_joke, format_quote

headers = {
			"Accept": "application/json",
			"User-Agent": "Quote Joke Generator (https://github.com/timhernand08/Quote---Joke-Generator-GUI)"
	 		}

quote = Cache(False, 'quotes.json', APIS["quotes"]["primary"], "quote")
joke_cache = Cache(False, 'jokes.json', APIS["jokes"]["primary"], "joke", headers)


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
				quote.mark_used(item['id'])
				return format_quote(item=item, is_backup=quote.get_backup())
			elif quotes ==[]:
				break
		except KeyError:
			quote.delete_cache()
			return "No API calls available. Please try again later"

	reset_cache(quote, APIS["quotes"]["primary"], APIS["quotes"]["backup"], quote.get_backup())
	return get_quote()

def format_quoter(item) -> str:
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
	""" headers = {
			"Accept": "application/json",
			"User-Agent": "Quote Joke Generator (https://github.com/timhernand08/Quote---Joke-Generator-GUI)"
	 }
	try:
		response = requests.get(APIS["jokes"]["primary"], headers = headers)
		json_data = json.loads(response.text)
		jke = json_data['joke']
	except requests.RequestException as e:
		jke = "Could not connect. Please try again later."
	return jke  """
	jokes = joke_cache.get_file()
	try:
		if jokes["used"] == "False":
			joke_cache.mark_used(jokes['id'])
			return format_joke(jokes, is_backup=joke_cache.get_backup())
	except KeyError:
		joke_cache.delete_cache()
		return "No API calls available. Please try again later"

	reset_cache(joke_cache, APIS["jokes"]["primary"], APIS["jokes"]["backup"], joke_cache.get_backup())
	return get_joke()

def reset_cache(file: Cache, primary_api, secondary_api=None, is_backup=False) -> str:
	file.create_cache(primary_api, secondary_api, is_backup)
	#return get_quote()


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
	content = ""
	print(f"Using backup quote API? {quote.get_backup()}")

	if(value == "quote"):
			content = get_quote()
			count = 0
			while hasQuote(content):
					content = get_quote()
					count+=1
					if count == 10:
							print("You're about to brick your PC homie")
							content = "Could not connect to API. Please try again later"
							quote.set_backup(True)
							break
	elif (value == "joke"):
			content = get_joke()
			count =0
			while hasJoke(content):
					print(f"The joke is '{content}' and this exists")
					content = get_joke()
					count+=1
					if count == 10:
							print("You're about to brick your PC homie")
							content = "Could not connect to API. Please try again later"
							break
	return content



if __name__ == "__main__":
	user = input("Would you like to test 'joke' or 'quote': ")
	print(checker(user))
	while (user := input("Enter 'joke', 'quote', or 'quit': ")) != "quit":
		print(checker(user))

