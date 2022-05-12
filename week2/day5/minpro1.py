from game import Game


def get_user_menu_choice():
    option = input("Play a new game(1), Show scores(2), Quit(3): ")
    while option not in list("123"):
        user = input("Please enter a valid input: ")
    return option


def print_results(results):
    print(f"""Game Results:
        You won {results['win']} times
        You lost {results['loss']} times
        You drew {results['draw']} times""")


def main():
    option = get_user_menu_choice()
    scoreboard = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }
    while option != "3":
        if option == '1':
            new_game = Game()
            scoreboard[new_game.play()] += 1
        if option == '2':
            print_results(scoreboard)
        option = get_user_menu_choice()
    print("Hope you had fun!")


main()
