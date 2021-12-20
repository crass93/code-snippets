#######################################################
#program: num_guess_game.py
#author: Crass93
#version: 1.0
#date: 20.12 2021
#description: Guess the correct number or have computer guess yours! 
#######################################################

import random #this module chooses a random item, in this case number

def check_int_input():
    """
    this function checks whether user input is an integer by trying to convert it to integer using a int() function,
    performing integer operations on it, and raising the error if it isnt, prompting the user to try again,
    if it succeeds it returns the user input.

    it takes no arguments.
    """
    while True:
        try:
            x = int(input("enter a number: "))
            x + 1
            x - 1
        except (TypeError, ValueError):
            print("that didnt look like a number to me, try again!")
            continue
        else:
            return x

start_word_list = ["computer", "me"]
word_list = ["high", "low", "correct"]
bad_word_list = ["fuck","shit","bitch", "cunt", "fuck off", "piss off", "nigger","motherfucker"]

def check_word_input(word, word_list, bad_word_list=None):
    """
    this function compares the word, in this case user input against a wordlist to see if input is correct, by checking if
    words is present in a wordlist. if not, user is notified that his input is not valid. 
    optionally checks the word against a list of bad words and gives feedback

    arguments:
    word -- word you want to check
    word_list -- list of words you want your word to compare against
    keyword arguments: 
    bad_word_list -- list of words that give custom feedback to the user. (default None)
           
    """
    if word in word_list:
        return word
    elif bad_word_list and word in bad_word_list:
        print("How dare you?!")
    else:
        print("invalid input, (check for typos)")




def guess(x):
    """
    this function uses random.randint() function to generate a random number in range from 1 to the number specified as an argument.
    user must guess the correct number using hints given by the function.
    if guess is correct, function notifies the user that he guessed the correct number. 

    arguments: 
    x -- highest number in a range from which random.randint() generates the random number. Must be positive integer
    """
    random_number = random.randint(1, x)
    guess = 0
    print(f"Try to guess the number between 1 and {x}.")
    while guess != random_number:
        guess = check_int_input()        #this function takes user input and checks if value is correct
        if guess < random_number:
            print("number is too low, try again!")
        elif guess > random_number:
            print("number is too high, try again!")
    print("Congratulations! you guessed the correct number.")


def computer_guess(x):
    """
    function generates random integer using random.randint() function and asks user if the guess is too high, low or correct.
    if guess is too high, it assigns variable high value of the inputed guess, and subtracts 1 from it. if value is low
    it assigns variable guess value low and adds 1 to it, thus narrowing down the range of numbers everz time a guess is made
    until user types "correct"

    arguments:
    x -- highest number in a range from which random.randint() generates the random number. Must be positive integer
    """
    low = 1
    high = x
    feedback = ""
    print(f"let me guess a number between 1 and {x}")
    while feedback != "correct":
        if low != high:                           #function random.randint() throws an error if low and high are the same value
            guess = random.randint(low, high)     #so we prevent this by assigning our variable guess, value low, if low is equal to high
        else:
            guess = low 
        feedback = input(f"i guess the number {guess}, is my guess too high? (type 'high') too low? (type 'low') or correct? (type 'correct'): ".lower())
        check_word_input(feedback, word_list, bad_word_list)    #function checks against word_list if input is correct
        if feedback == "high":                                  #and against bad_word_list if input contains profanity
            high = guess - 1
        elif feedback == "low":
            low = guess + 1
    print(f"YaY! computer guessed the number {guess} correctly!" )

def start_game():
    """
    this function lets user choose the range of numbers used in a guessing game and whether he wants the computer to guess the number
    or whether he wants to guess himself. function than uses that input to call the respective function and pass it the arguments.

    function takes no arguments
    """
    print("Hi stranger, Welcome to my number guessing game! \ntype the highest number in a range of numbers we are going to guess (type any positive whole number bigger than 1)")
    args_num = check_int_input()
    start = input("Who is going to guess? computer or you? (type 'computer' or 'me'): ")
    check_word_input(start, start_word_list, bad_word_list)
    if start == "me":
        guess(args_num)
    elif start == "computer":
        computer_guess(args_num)

start_game()
