from operator import truediv
import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    # comment this line out if you use a words.txt file with each word on a new line
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


secret_word = load_word()

print("Welcome to Spaceman!")
print(f"The secret word contains {len(secret_word)} letters.")
print("You have 7 incorrect guesses, please enter one letter per round")

#TODO: Ask the player to guess one letter per round and check that it is only one letter
player = False
while player == False:
     while True:
        letter_choice = input("Please guess one letter: ")
        if len(letter_choice) > 1:
            print("Please only enter one letter at a time.")
        else:
            break
