import customtkinter
from generator import checker
import os
import sys
import threading

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, value, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.value = value
        self.title= title

        button = customtkinter.CTkButton(self, text=title, command=self.get_button)
        button.grid(row = 0, column = 0, padx=10, pady=(10, 0), sticky = "ew")

        self.text = customtkinter.CTkTextbox(self, height=100, wrap="word")
        self.text.grid(row = 1, column = 0, padx=10, pady=(10, 0), sticky = "nsew")
        self.text.insert("0.0", "Loading...")
        self.text.configure(state="disabled")
        
        threading.Thread(target=self.load_initial_text).start()

    def load_initial_text(self):
        text = checker(self.value)
        self.update_text(text)
        set_value(self.value, text)
    
    def update_text(self, text):
        self.text.configure(state="normal")
        self.text.delete("0.0", "end")
        self.text.insert("0.0", f"{text}")
        self.text.configure(state="disabled")


    def get_button(self):
        text = checker(self.value)
        self.update_text(text)
        set_value(self.value, text)

    def get(self):
        return self.text.get("0.0", "end")
    


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quote & Joke Generator")
        self.geometry("400x200")
        customtkinter.set_default_color_theme(resource_path("custom_theme.json"))
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.quote_button = ButtonFrame(self, title="Generate Quote", value="quote")
        self.quote_button.grid(row = 0, column = 0, padx=10, pady=10, sticky = "nsew")
        
        self.joke_button = ButtonFrame(self, title = "Generate Joke", value="joke")
        self.joke_button.grid(row=0, column = 1, padx=10, pady=10, sticky="nsew")
        

    def get_quote(self):
        return self.quote_button.get()
    
    def get_joke(self):
        return self.joke_button.get()

quote = ""
joke = ""

def get_value(type) -> str:
    return quote if type == "quote" else joke

def set_value(value, text):
    if value == "quote":
        global quote 
        quote = text
    else:
        global joke
        joke = text

        
    
"""app = App()
app.mainloop"""


