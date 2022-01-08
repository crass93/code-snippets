import random
import math

class Player:
    """
    class Player is essentialy a parent class from which our players will inherit from, we use it to initialize the variable letter
    """
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    """
    this class represents the computer player, it uses its parents class initializer and overrides the parents class get_move method
    instance of the class is used as an argument for play method of TicTacToe class creating a computer player for the game

    """
    def __init__(self, letter):
        super().__init__(letter) #we use the parents class initializer

    def get_move(self, game):
        """
        method uses choice function of random module to select a spot from available_moves
        method of TicTacToe class from game.py dependent file

        takes instance of a TicTacToe class (game) as argument
        """
        square = random.choice(game.available_moves()) 
        return square

class HumanPlayer(Player):
    """
    this class represents the human player, it uses its parents class initializer and overrides the parents class get_move method
    instance of the class is used as an argument for play method of TicTacToe class creating a human player for the game
    """
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """
        this method asks for user input, checks if input can be turned into integer and if input is in list of available moves 
        (game.available_moves method in TicTacToe class, game.py dependent file) if all checks come true, returns value, else
        raises ValueError
        
        takes instance of a TicTacToe class (game) as argument
        """
        valid_square = False
        val = None
        while valid_square == False:
            square = input(self.letter + "\"s turn. Input move (0-8):")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again!")
        return val
