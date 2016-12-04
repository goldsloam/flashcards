import json
import random
from sys import argv

script, cardstack = argv

with open(cardstack) as cards:
    stack = json.load(cards)

keys = list(stack.keys())

# Offer 4 possible values for each key presented
while True:
    question = keys[random.randint(0, len(keys) - 1)]
    answer = input("Question: " + question + " or (q)uit > ")
    if answer == "q":
        exit(0)
    elif answer == stack.get(question):
        print("Correct!")
    else:
        print("Wrong, the correct answer was", stack.get(question))
