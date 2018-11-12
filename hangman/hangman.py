## Hangman by Thermixia

import random
import json

def gameStart():
    print("Title: Hangman")
    print("By: Thermixia")
    print("#" * 30)

    wordcont = input("User Word or Random Word (type user or random): ").lower()
    if wordcont == "user":
        word = input("Word: ").upper()
    else:
        with open('words.json') as f:
            data = json.load(f)

        words = data
        wordnum = len(words)
        print("#" * 30)
        print("The number of possible words are:", str(wordnum))
        word = random.randint(0, wordnum)
        word = words[word]

    return word

def gameMain(word):
    gameComplete = False
    gameWon = False
    wordlist = list(word)
    attempts = 6
    knownlist = []
    knownwrong = []

    for item in wordlist:
        knownlist.append(False)

    print(knownlist)

    while gameComplete == False:
        attempt = input("Letter or word (type letter or word): ").lower()
        knownletters = []
        letterpos = 0

        for item in knownlist:
            if item == True:
                knownletters.append(wordlist[letterpos])
            else:
                knownletters.append("_")

            letterpos += 1
            print(letterpos)

        print(knownletters)

        if attempt == "word":
            attempt = input("Word: ").upper()
            if attempt == word:
                gameComplete = True
                gameWon = True
            else:
                attempts -= 1
                print("Incorrect! Attempts:", attempts)
        else:
            attempt = input("Letter: ").upper()
            letterpos = 0

            if attempt in wordlist:
                for item in wordlist:
                    if item == attempt:
                        knownlist[letterpos] = True
                    letterpos += 1
            else:
                attempts -= 1
                print("Incorrect! Attempts:", attempts)
                knownwrong.append[attempt]

        if all(item == True for item in knownlist):
            gameComplete = True
            gameWon = True
    if gameComplete == True:
        if gameWon == True:
            return True
        else:
            return False
    else:
        return False

def outcomeCheck(outcome):
    if outcome == True:
        print("You win!")
    else:
        print("You lose!")


word = gameStart()
outcome = gameMain(word)
outcome(outcome)
