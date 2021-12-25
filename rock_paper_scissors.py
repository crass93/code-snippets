#######################################################
#program: rock_paper_scissors.py
#author: Crass93
#version: 1.0
#date: 22.12 2021
#description: Play rock, paper, scissors against a computer
#######################################################

import random #this module is used to select randomly one of the three values, rock paper or scissors

def game():
    """
    this function is a rock, paper, scissors game which uses a random fucntion to select one of three values for computer and input to
    accept value from player, it uses a whileloop with a condition to run an if\elif\else code block to see who won, display a score and check
    if user input is valid. 

    function has no arguments
    """
    computer_wins = 0
    player_wins = 0
    feedback = " "
    wordlist = ["rock","paper","scissors"]
    print("Welcome to my Rock, Paper, Scissors game!, rules are simple, rock beats scissors, paper beats rock and scissors beat paper.\n")
    while feedback != "quit":
        feedback = input("Type  'rock', 'paper' or 'scissors' to play or 'score' to view the scoreboard: ").lower()
        computer = random.choice(["rock","paper","scissors"])
        if feedback == computer:
            print("its a tie!")
        elif feedback in wordlist and (feedback == 'rock' and computer == 'scissors') or (feedback == 'paper' and computer == 'rock') or (feedback == 'scissors' and computer == 'paper'):
            player_wins += 1
            print("you won!, your current score is now %d" %player_wins)
        elif feedback == "score":
            print("player score is: %d" % player_wins)
            print("computer score is: %d" % computer_wins)
        elif feedback in wordlist and feedback != (feedback == 'rock' and computer == 'scissors') or (feedback == 'paper' and computer == 'rock') or (feedback == 'scissors' and computer == 'paper'):
            computer_wins += 1
            print("you lost!, opponents current score is now %d" %computer_wins)
        else:
            print("invalid input")
        print("type 'quit' to quit")
        feedback = input("or press any key to play again: ")
        continue

game()
