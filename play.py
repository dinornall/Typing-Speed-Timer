from readline import clear_history
from time import time
import random
import os


file = open("quotes.txt", "r")
content = file.read()
quotes = content.splitlines()

def clear():
    os.system("clear")

def count_words(quote):
    wordCount = 1
    for i in range(len(quote)):
        if quote[i] == " ":
            wordCount = wordCount + 1
    return wordCount

def play():
    quote = quotes[random.randint(0,len(quotes)-1)]
    trial = " "
    while trial != quote:
        countdown = 3
        countdownTime = time()
        while countdown >= 0:
            if time() >= countdownTime + 1:
                countdownTime = time()
                print (countdown)
                countdown = countdown - 1
        clear()
        print("GO!")
        print (quote)
        startTime = time()
        trial = str(input())
    stopTime = time()
    timeTaken = stopTime - startTime
    words = count_words(quote)
    wpm = (words/timeTaken)*60
    clear()
    print()
    print("Your wpm is: " + str(wpm))
    print()