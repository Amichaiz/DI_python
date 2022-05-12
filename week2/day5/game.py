from random import choice


class Game:
    options = ['r', 'p', 's']

    def __init__(self):
        self.user = self.get_user_item()
        self.comp = self.get_computer_item()

    @staticmethod
    def get_user_item():
        user = input("Select (r)ock, (p)aper, (s)cissors: ")
        while user not in list("rps"):
            user = input("Please enter a valid input: ")
        return user

    @staticmethod
    def get_computer_item():
        return choice(Game.options)

    def get_game_result(self):
        if self.user == self.comp:
            return 'draw'
        if Game.options.index(self.user)-1 == Game.options.index(self.comp):
            return 'win'
        return 'loss1'

    def play(self):
        print(f'You selected {self.user}. The computer selected {self.comp}. {self.get_game_result()}')
        return self.get_game_result()

