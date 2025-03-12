# Quote and Joke Generator

This project is a simple Python script that generates a random quote and a joke every time it is run. It fetches data from two public APIs: ZenQuotes for inspirational quotes and JokeAPI for random jokes. The user can also request new quotes or jokes, and the program will continue until the user types "done" to terminate.

## Features

- Automatically generates and displays a random quote and a random joke when the program starts.
- Users can request a new quote or joke at any time.

## APIs Used

- **Quote API**: [ZenQuotes](https://zenquotes.io/) provides random inspirational quotes.
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
Changed the joke API. The last API featured too many jokes related to programming. Changed to an API that is more general.


## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/timhernand08/Quote---Joke-Generator/blob/main/LICENSE) file for details

