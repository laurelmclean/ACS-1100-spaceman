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
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    
    for letter in range(len(letters_guessed)):
        if letters_guessed[letter] in secret_word:
            return True
        else:
            return False

        

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_letters = ""
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            guessed_letters += secret_word[letter]
        else:
            guessed_letters += "_"

    return guessed_letters

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    game_over = False
    guesses = 7
    letters_guessed = []

    #TODO: show the player information about the game according to the project spec

    print("Welcome to Spaceman!")

    instruction = input("Would you like instructions? (yes/no) ")
    instruction = instruction.lower()
    if instruction == "yes":
        print("Spaceman is a guessing game. There is a mystery word that you will try to guess one letter at a time.\nA placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word.\nIf the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.\nGuess the word before you run out of guesses!")
    
    print(f"The secret word contains {len(secret_word)} letters.")
    print("You have 7 incorrect guesses, please enter one letter per round")

   

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    while not game_over:
        # show guessed word so far
        print(f'The guessed word is {get_guessed_word(secret_word, letters_guessed)}')
        print(f'The guessed letters are: {letters_guessed}')
        check_guess = False
        while check_guess == False:
            guess = input("Please guess one letter: ").lower()
            if len(guess) > 1:
                print("Please only enter one letter at a time.")
            elif guess.isalpha() == False:
                print("Please only guess letters, no numbers or special characters allowed.")
            else:
                letters_guessed.append(guess)
                break

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

        if is_guess_in_word(guess, secret_word) == True:
            print("Your guess appears in the word!")
        else:
            guesses -= 1
            print("Sorry your guess was not in the word. Please try again.")
            print(f"You have {guesses} guesses remaining.")



    #TODO: check if the game has been won or lost

        if guesses == 0:
            print(f"Sorry, you ran out of guesses! The secret word was {secret_word}")
            
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print(
                f"Congratulations, you win! The secret word was {secret_word}")



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
