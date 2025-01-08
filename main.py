from memory import storeData, update_time_trigger
from initdb import initialize_db
from gui import App, get_value


initialize_db()


get_gen = App()

get_gen.mainloop()



update_time_trigger("quotes")
update_time_trigger("jokes")
  
quote = get_value("quote")
joke = get_value("joke")


storeData(quote, joke)
print(f"\nQuote: {quote}")
print(f"Joke: {joke}")
print("\nData has been saved to memory. Thank you for using the Quote & Joke Generator!")

