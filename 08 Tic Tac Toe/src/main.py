import random

class TicTacTeo:
    """A class used to represent a Tic Tac Teo game.
    """
    def __init__(self):
        """initializes the game board and randomly selects the first player.
        """
        self.board = [" "] * 10
        self.board[0] = 1
        self.player_turn = self.get_random_first_player()
        
    def get_random_first_player(self):
        """A def used to choose first player to play game.
        """
        return random.choice(["X","O"])
        
    def swap_player_turn(self):
        """A def used to swap player turn.
        """
        player = ["X","O"]
        self.player_turn = player[0] if self.player_turn == "O" else player[1]    
        
    def has_player_won(self):
        """A def used to define wiiner.
        """
        combination_win = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                           (1, 4, 7), (2, 5, 8), (3, 6, 9),
                           (1, 5, 9), (3, 5, 7)]
        for combination in combination_win:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == self.player_turn:
                return True
        return False
    
    def show_board(self):
        """A def to prints out the current state of the game board.
        """
        print('****************')
        print('   ', end='')
        print(self.board[1], self.board[2],self.board[3], sep = " | ",)
        print('   ', end='')
        print('——————————')
        print('   ', end='')
        print(self.board[4], self.board[5],self.board[6], sep = " | ",)
        print('   ', end='')
        print('——————————')
        print('   ', end='')
        print(self.board[7], self.board[8],self.board[9], sep = " | ",)
        print('****************')
        
    def fix_spot(self, cell, player):
        """allows a player to mark a cell on the board.
        """
        self.board[cell] = player
        
    def is_board_filled(self):
        """ checks if the game board is completely filled.
        """
        return ' ' not in self.board
    
    def start(self):
        """begins the game loop, processing user input and game updates.
        """
        while True:
            self.show_board()
            try:
                number = int(input(f"Player {self.player_turn}, Enter the cell number between 1 and 9: "))
                if number in range(1, 10) and self.board[number] == ' ':
                    self.fix_spot(number, self.player_turn)

                    if self.has_player_won():
                        print(f"Player {self.player_turn} wins!")
                        self.show_board()
                        break

                    if self.is_board_filled():
                        print("It's a Draw!")
                        self.show_board()
                        break

                    self.swap_player_turn()

                else:
                    print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")



if __name__ == "__main__":
    game = TicTacTeo()
    game.start()
