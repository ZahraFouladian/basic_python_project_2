from game_logic.number_generator import number_generator
from game_logic.hint_generator import hint
from game_logic.scorer import Scorer
from utils.input_validator import get_valid_input

def main():
    actual_number = number_generator(1,100)
    score = Scorer()
    while True:
        guess = get_valid_input("Enter your guess: ", 1, 100)
        if guess == actual_number:
            print(f"Congratulations! Your final score is: {score.get_score()}")
            break
        else:
            print(hint(guess, actual_number))
            score.decrement_score()

if __name__ == "__main__":
    main()

