
def is_word_guessed(secret_word, letters_guessed):
    #  Loops through the letters in the secret_word and check if a letter is not in lettersGuessed
    # Returns true if all letters have been guessed, otherwise returns false
    guessed_word = ""
    correct = False
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            guessed_word += secret_word[letter]
            if guessed_word == secret_word:
                correct = True

    return correct


def get_guessed_word(secret_word, letters_guessed):
    # Loops through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_letters = ""
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            guessed_letters += secret_word[letter]
        else:
            guessed_letters += "_"

    return guessed_letters


def is_guess_in_word(guess, secret_word):
    # checks if the letter guess is in the secret word. Returns true if it is, otherwise false

    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    #  Function controls game
    game_over = False
    guesses = 7
    letters_guessed = []
# Shows player the rules
    print("Welcome to Spaceman!")

    instruction = input("Would you like instructions? (yes/no) ")
    instruction = instruction.lower()
    if instruction == "yes":
        print("Spaceman is a guessing game. There is a mystery word that you will try to guess one letter at a time.\nA placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word.\nIf the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.\nGuess the word before you run out of guesses!")

    print(f"The secret word contains {len(secret_word)} letters.")
    print("You have 7 incorrect guesses, please enter one letter per round")

    #Prompt player to enter one letter per round

    while game_over == False:

        check_guess = False
        # Stretch challenge - only allow players to guess one LETTER at a time
        while check_guess == False:
            guess = input("Please guess one letter: ").lower()
            if len(guess) > 1:
                print("Please only enter one letter at a time.")
            elif guess.isalpha() == False:
                print(
                    "Please only guess letters, no numbers or special characters allowed.")
            # stretch challenge - alert player if they've already guessed a letter
            elif guess in letters_guessed:
                print("You have already guessed that letter. Try again.")
            else:
                letters_guessed.append(guess)
                break

    #check if the guessed letter is in the secret or not and give the player feedback

        if is_guess_in_word(guess, secret_word) == True:
            print("Your guess appears in the word!")
            # show guessed word so far
            print(
                f'The guessed word so far is {get_guessed_word(secret_word, letters_guessed)}')
            print(f'The guessed letters are: {letters_guessed}')
        # subtract a guess and show number of guesses remaining
        else:
            guesses -= 1
            if guesses > 0:
                print("Sorry your guess was not in the word. Please try again.")
                print(f"You have {guesses} guesses remaining.")
                print(
                    f'The guessed word so far is {get_guessed_word(secret_word, letters_guessed)}')
                print(f'The guessed letters are: {letters_guessed}')

    #Check if game has been won
    # If user runs out of guesses
    # Stretch challenge - show the player the mystery word if they lose
        if guesses == 0:
            print(
                f"Sorry, you ran out of guesses! The secret word was {secret_word}")
            game_over = True
        # If player wins
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print(
                f"Congratulations, you win! The secret word was {secret_word}")
            game_over = True
# Stretch challenge - Asks if player wants to play again and calls functions to restart game if yes
    print(f"GAME OVER!!!")
    play_again = input("Would you like to play again? (yes/no) ")
    play_again = play_again.lower()
    if play_again == "yes":
     
        spaceman(secret_word)
    else:
        print("See you later!")


#These function calls that will start the game

spaceman("apple")
