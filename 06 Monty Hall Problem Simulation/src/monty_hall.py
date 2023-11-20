import random

def monty_hall_game(switch_choise: bool) -> bool:
    """
    Simulate a single Monty Hall game.

    :param bool switch_choise: If True, the contestant will switch their choice after a goat door is revealed.
    :return: True if the contestant won the car, False otherwise.
    :rtype: bool
    """

    door = ['goat','car','goat']
    random.shuffle(door)
    initial_choice = random.randint(0,len(door))
    reveal_door = random.choice([i for i in range(len(door)) if (i != initial_choice and door[i] != "car")])
    if switch_choise:
        finale_choise = [i for i in range(len(door)) if i != reveal_door and i != initial_choice][0]        
    else:
        finale_choise = initial_choice
    return door[finale_choise] == "car"    


def simulate_games(num_games: int = 1000) -> None:
    """
    Simulate a number of Monty Hall games and print the statistics.

    :param int num_games: The number of games to simulate. Defaults to 1000.
    :return: None
    """

    # Simulate games where contestant keeps and switches doors
    winner = 0
    for _ in range(num_games):
        if monty_hall_game(True):
            winner += 1
    num_wins_without_switching = num_games - winner
    num_wins_with_switching = winner
    return num_wins_without_switching, num_wins_with_switching

if __name__ == "__main__":
    num_games = 1000
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games)
    print(f"Winning percentage without switching doors: {(num_wins_without_switching / num_games) * 100}%")
    print(f"Winning percentage with switching doors: {(num_wins_with_switching/ num_games) * 100}%")
   
