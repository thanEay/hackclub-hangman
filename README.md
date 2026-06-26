# 🖥️ Hack Club Hangman 🖥️

A hangman game implemented in Python 🐍. Made for Hack Club Stardance ⭐️. 

The code runs a text-based hangman game where a player guesses letters to reveal a hidden word 🫣. Incorrect guesses reduce the number of remaining attempts until the game is won or lost.

## 🏃‍♂️ Try the game

```bash
# Clone the repository
git clone https://github.com/thaneay/hackclub-hangman.git
cd hackclub-hangman

# Run the game
python3 main.py
```

There is also an online **[demo](hangman.epin.to)** at hangman.epin.to to quickly try it out.


## How to play ⏯️

1. Select your mode 
	- There are 4 modes: manual word selection, random word selection, manual word selection with infinite guesses, and random word selection with infinite guesses
	- There are a few different ways to choose each mode
		+ For manual, type "manual", "man", or "m"
			* Manual word selection allows you to choose the secret word: great for playing with a friend
		+ For random, type "random", "rand", or "r"
			* Random word selection chooses a random word from a list in random_words.py. Great for playing by yourself.
	- To enable 'infinite guessing' (playing without the ability to lose), put an exclamation mark before your mode selection. For example, '!manual' or '!random'.
		+ Notice: Enabling infinite guessing turns off the hangman sprites. Incorrect guesses are not kept track of, there are no body parts to draw in.
		
2. If you selected manual word input, enter a secret word for your friend to guess
3. Guess letters or words
	- To guess a leter, type it out and press enter
	- To guess a word, enter an exclamation mark followed by your guess. For example, '!stardance', '!jacket', '!umbrella'. Guessing a word without a starting '!' will not work.

4. Win! 🥇
	- Guess all of the letters right or guess the entire word correctly to win

