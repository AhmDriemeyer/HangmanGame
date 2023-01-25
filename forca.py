import random

#   This is a hangman game

def load_word():
    with open("words.txt", "r") as f:
        words = f.readlines()
        return random.choice(words).strip()
