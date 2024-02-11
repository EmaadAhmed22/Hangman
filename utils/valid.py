# Good to make your code split into different files Uses comments to explain functions, and use the as reminders

import random



def word_Chooser(wordList):
    """
    Chooses a random word from word list
    """
    word = random.choice(wordList)
    #The () in random choice is the list you pull from
    # Keep selecting a word untill it doesnt have a space or a -
    # Using while loop because we need to keep selecting words untill they meet the condition of no space/-
    while "-" in word or " " in word:
        word = random.choice(wordList)
    
    return word.upper()