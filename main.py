from memory import storeData, hasJoke, hasQuote, update_time_trigger
from initdb import initialize_db
from gui import App

initialize_db()

get_gen = App()

update_time_trigger("quotes")
update_time_trigger("jokes")

"""try:
    get_gen.mainloop()
except Exception as e:
    print(f"An error occurred: {e}")"""

storeData(get_gen.get_quote(), get_gen.get_joke())
print(f"\nQuote: {get_gen.get_quote()}")
print(f"Joke: {get_gen.get_joke()}")
print("\nData has been saved to memory. Thank you for using the Quote & Joke Generator!")

