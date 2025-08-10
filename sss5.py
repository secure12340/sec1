import random

quotes = [
    "Be the change you wish to see in the world.",
    "Stay hungry, stay foolish.",
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
]

def get_random_quote():
    return random.choice(quotes)

print("Random Quote of the Day:")
print(get_random_quote())