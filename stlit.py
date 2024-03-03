import streamlit as st
from utils.valid import word_Chooser
from utils.wordlist import words
from utils.visual import lives_visual_dict
import string



#ishaan method
#use cd to navigate anaconda
#conda activate ausdevcamps to go to that enviornment 

if "lives" not in st.session_state:
    st.session_state.lives = 7
if "word" not in st.session_state:
    st.session_state.word = word_Chooser(words)
if "used_letters" not in st.session_state:
    st.session_state.used_letters = set()
if "word_letters" not in st.session_state:
    st.session_state.word_letters = set(st.session_state.word)
# our word is now know as st.session_state.word for context
    
# starts off as a empty set
    
#front end stuff
alphabet = set(string.ascii_uppercase)
#state variables is for variables that change across runs
# Display lives and used letters at the top
st.title("Welcome to hangman")
st.write(f"You have {st.session_state.lives} lives remaining \n")
if len(st.session_state.used_letters) > 0:
    st.write(f"You have used the following letters: {st.session_state.used_letters} in your guess")

#st.write(f"You chose {st.session_state.word}")


#display the current STATE of the word 
word_list = [letter if letter in st.session_state.used_letters else "-" for letter in st.session_state.word]

st.write ("".join(word_list))
#re run refreshes code 
#now user guesses letter

user_letter = st.text_input("Guess a letter: " ,key="user_letter")

#add a button to submit 

st.button("Submit")