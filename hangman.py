# File for hangman game

from utils.valid import word_Chooser
from utils.wordlist import words
from utils.visual import lives_visual_dict
import string

def hangman ():
    word = word_Chooser(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    lives = 7
    used_letters = set()
    print(word)
    # start the game
    while lives > 0:
        print("Welcome to Hangman! \n")
        print(f"You have {lives} remaining \n ")
        print(f"You have used {used_letters} in your guess")

        # if the user has guessed the letters b,l,h
        #ex: for the world blah this would print bl_h
        """
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")

        """

        # What this is doing (the line below us)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word ", word_list)
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in used_letters :
            print("You have already used this letter. Guess again")

        elif user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                #word_letter is [b,o] 
                #user guessed b 
                #word_letters holds all the unique letters in the word
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print("This letter is not in the word")
        else:
            lives = lives-1
            print(f"The letter {user_letter} is not in the word")
            print("Not a valid character/letter")
        # User inputted a letter, checks if user letter is actually a letter in (use alphabet)
        # Makes sure it isnt already used_letters



if __name__ == "__main__":
    hangman()