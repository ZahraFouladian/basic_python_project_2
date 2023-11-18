import random

class RockPaperScissors:
    """main class for Rock Paper Scissors
    """
    def __init__(self):
        self.list_choice = ["rock", "scissors", "paper"]
            
    def get_player_choice(self):
        """Method to select the player's choice"""
        print("\n-Rock\n-Paper\n-Scissors")
        choice = (input("Enter your choice: ")).lower()
        if choice in self.list_choice:
            self.player_choice = choice
            return True
        else:
            print("Invalid choice. Please make sure your choice is in 'rock', 'paper' or 'scissors'.")
            return self.get_player_choice()

    def get_computer_choice(self):
        """Method to select the computer's choice"""
        self.computer_choice = random.choice(self.list_choice)
        return True

    def get_winner(self):
        """Method to define game winner based on the rules."""
        if self.computer_choice == self.player_choice:
            return "It's a tie!"
        
        elif (self.computer_choice == "rock" and self.player_choice == "scissors") or \
             (self.computer_choice == "paper" and self.player_choice == "rock") or \
             (self.computer_choice == "scissors" and self.player_choice == "paper") :
            return "Oh no, the computer won!"
        else :
            return "Congratulations, you won!"
                       
    def play(self):
    """Main method to play Rock, Paper, Scissors"""
        self.get_player_choice()
        self.get_computer_choice()
        print('Computer chose: ', self.computer_choice)
        print(self.get_winner())


if __name__ == '__main__':
    game = RockPaperScissors()
    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break
