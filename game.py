#######################################################
#program: tic_tac_toe.py
#author: Crass93
#version: 1.0
#date: 30.12 2021
#description: Play the game of tic tac toe!
#######################################################

from player import HumanPlayer, RandomComputerPlayer #this line of code imports HumanPlayer and RandomComputerPlayer classes from player.py dependent file
import time #this module is used to add a time delay between the moves

class TicTacToe:
    """
    class TicTacToe is the heart of the program, we play the game by creating an instance of this class
    """
    def __init__(self):
        self.board = [" " for _ in range(9)]   #we will use a single list to represent our 3 x 3 board
        self.current_winner = None   #keep track of a current winner

    def print_board(self):
        """
        function prints the layout of the playing board
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|" + "|".join(row) + "|")

    @staticmethod
    def print_board_nums():
        """
        this static method tells us which numbers correspond to what box (0|1|2 etc.)
        
        method takes no arguments
        """
        numbered_board = [[str(i) for i in range(j*3, (j+1)*3 )] for j in range(3)]
        for row in numbered_board:
            print("|" + "|".join(row) + "|")

    def available_moves(self):
        """
        this method returns the available spots within a playing board

        takes no arguments
        """
        moves = []
        for (i, spot) in enumerate(self.board):  #["x","x","o"] --> [(0, "x"),(1, "x"),(2, "o")]
            if spot == " ":
                moves.append(i)
        return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        """
        this function makes a move on a spot and checks if move is valid, if yes, returns True, else returns False
        """
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """
        you win the game if there is three of X or O in a row, function checks whether there three of a same i n row, column or diagonal
        """
        #row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True
        #column
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if row, column and diagonals check fail, return false
        return False

def play(game, x_player, o_player, print_game=True):
    """
    basicaly a method that runs the game, it iterates through the empty_squares method which checks if there are empty squares in board,
    it uses a make_move method to move to a spot and prints the updated board representation, it checks for a winner using a current_winner method
    and prints his letter, if it finds that current_winner method doesnt get called and are no more empty squares in board and there is no winner, it prints "its a tie"

    arguments:
    game --> instance of a TicTacToe class
    x_player --> instance of a player subclass (HumanPlayer or RandomComputerPlayer)
    o_player --> instance of a player subclass (HumanPlayer or RandomComputerPlayer)
    keyowrd arguments:
    print_game=True --> set if you want the game to print every step of every player, default value is set to true
    """

    print("Welcome to my Tic-Tac-Toe game! this is the layout of the playng board,\n"
              "use numbers to select the spot you want to move to\n")
    if print_game:
        game.print_board_nums()

    letter = "X" #starting letter
    #iterate while the game still has empty squares
    #(we dont have to worry about the winner because we will just break out of the loop with a return)
    while game.empty_squares():
        #get the move from appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            #after we made our move, we need to alternate letters
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
        #time delay method of a sleep module, module is used to make the game appear more natural
        time.sleep(1)

    if print_game:
        print("its a tie!")

if __name__ == "__main__":
    """
    this code runs if game is run from command line, (within a module, modules name as a string is stored in the global namespace as __name__,
    but if the module file is run as program from command line, python sets the modules __name__ to __main__)
    """
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
