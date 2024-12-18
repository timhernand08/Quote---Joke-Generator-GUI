from memory import storeData, hasJoke, hasQuote, update_time_trigger
from initdb import initialize_db
from gui import App, get_value
from tkinter.messagebox import askyesno


initialize_db()


get_gen = App()

def confirm():
    ans = askyesno(title = 'Exit', message='Do You Want To Exit?')
    if ans:
        get_gen.destroy()

get_gen.protocol("WM_DELETE_WINDOW", confirm)
get_gen.mainloop()



update_time_trigger("quotes")
update_time_trigger("jokes")
  
quote = get_value("quote")
joke = get_value("joke")


storeData(quote, joke)
print(f"\nQuote: {quote}")
print(f"Joke: {joke}")
print("\nData has been saved to memory. Thank you for using the Quote & Joke Generator!")


"""if __name__ == "__main__":
    get_gen = App()
    get_gen.mainloop()"""