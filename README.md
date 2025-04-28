# Quote and Joke Generator

This project is a simple Python script that generates a random quote and a joke every time it is run. It fetches data from two public APIs: ZenQuotes for inspirational quotes and JokeAPI for random jokes. The user can also request new quotes or jokes using the buttons on screen.

![image](https://github.com/user-attachments/assets/0ef0bfe1-91db-481d-b9f1-24a1ced9c61d)

## Features

- Automatically generates and displays a random quote and a random joke when the program starts.
- Users can request a new quote or joke at any time.

## APIs Used

- **Quote API**: [ZenQuotes](https://zenquotes.io/) provides random inspirational quotes.
- **Quote API 2**: [QuoteSlate API](https://quote-slate-timothy-hernandezs-projects.vercel.app) backup API for quotes.
- **Joke API**: [icanhazdadjoke](https://icanhazdadjoke.com/) provides random dad jokes.

## How to Use

1. Clone or download this repository to your local machine.
2. Install the required libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Python script:
    ```bash
    python main.py
    ```
4. The program will display a random quote and a random joke.
5. You can request a new quote by pressing `generate quote`, or a new joke by pressing `generate joke`.

## New Features!
Added a backup API to be used in the event that the main API is down or has requested too many times. Also added a cache feature for the quotes to locally save multiple quotes to a users machine to prevent making too many API requests at a time.

## Features to Add
- Cache feature for jokes and a backup API.
- Window to display history of all jokes and quotes used.
- Delete history
- Category chooser to specify specific quotes and jokes to be displayed.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/timhernand08/Quote---Joke-Generator/blob/main/LICENSE) file for details

