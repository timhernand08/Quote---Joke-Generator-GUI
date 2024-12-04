import customtkinter
from generator import checker


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
        self.text.insert("0.0", f"{checker(self.value)}")
        self.text.configure(state="disabled")

    def get_button(self):
        self.text.configure(state="normal")
        self.text.delete("0.0", "end")
        self.text.insert("0.0", f"{checker(self.value)}")
        self.text.configure(state="disabled")

    def get(self):
        return self.text.get("0.0", "end")
    


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quote & Joke Generator")
        self.geometry("400x200")
        customtkinter.set_default_color_theme("custom_theme.json")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.quote_button = ButtonFrame(self, title="Generate Guote", value="quote")
        self.quote_button.grid(row = 0, column = 0, padx=10, pady=10, sticky = "nsew")

        self.joke_button = ButtonFrame(self, title = "Generate Joke", value="joke")
        self.joke_button.grid(row=0, column = 1, padx=10, pady=10, sticky="nsew")


    def get_quote(self):
        return self.quote_button.get()
    
    def get_joke(self):
        return self.joke_button.get()

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()"""