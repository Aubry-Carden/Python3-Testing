import json
import random

with open('words.json') as f:
    data = json.load(f)

words = data
wordnum = len(words)
print("#" * 30)
print("The number of possible words are: " + str(wordnum))
word = random.randint(0, wordnum)
word = words[randomword]
