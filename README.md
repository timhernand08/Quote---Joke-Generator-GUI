# Quote and Joke Generator

This project is a simple Python script that generates a random quote and a joke every time it is run. It fetches data from two public APIs: ZenQuotes for inspirational quotes and JokeAPI for random jokes. The user can also request new quotes or jokes, and the program will continue until the user types "done" to terminate.

## Features

- Automatically generates and displays a random quote and a random joke when the program starts.
- Users can request a new quote or joke at any time.
- The program will continue running until the user types `done` to exit.

## APIs Used

- **Quote API**: [ZenQuotes](https://zenquotes.io/) provides random inspirational quotes.
- **Joke API**: [JokeAPI](https://jokeapi.dev/) provides random jokes with the ability to filter out inappropriate content (NSFW, racist, or explicit).

## How to Use

1. Clone or download this repository to your local machine.
2. Install the required libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Python script:
    ```bash
    python quote_joke_generator.py
    ```
4. The program will display a random quote and a random joke.
5. You can request a new quote by typing `quote`, or a new joke by typing `joke`.
6. To terminate the program, type `done`.

## Example Usage

```bash
"Believe you can and you're halfway there."
 - Theodore Roosevelt

What do you call fake spaghetti?
An impasta!

Please enter if you want a new quote or joke. Or enter 'done': quote

"Success is not the key to happiness. Happiness is the key to success."
 - Albert Schweitzer

Make a new request: joke

Why don't skeletons fight each other?
They don't have the guts!

Make a new request: done
Data has been saved to memory. Thank you for using the Quote & Joke Generator!
```
## New Features!
Added memory database. This will store the last quotes and jokes that were given before the user terminated the program with "done". This will allow the program
to keep track of what has been said so they won't be repeated. Any entries over 90 days old will be removed automatically so that they can be reused.


## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/timhernand08/Quote---Joke-Generator/blob/main/LICENSE) file for details

