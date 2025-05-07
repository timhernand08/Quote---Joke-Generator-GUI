APIS = {
    "quotes": {
        "primary": "https://zenquotes.io/api/quotes",
        "backup": "https://quote-slate-timothy-hernandezs-projects.vercel.app/api/quotes/random?count=5"
    },
    "jokes": {
        "primary": "https://icanhazdadjoke.com/",
        "backup" : "https://official-joke-api.appspot.com/random_joke"
        }
}

def format_quote(item, is_backup=False):
    key_text, key_author = ('q', 'a') if not is_backup else ('quote', 'author')
    return f"{item[key_text]}\r\n - {item[key_author]}"

def format_joke(item, is_backup=False):
    if not is_backup:
        return item["joke"]
    else:
        return f"{item['setup']} {item['punchline']}"