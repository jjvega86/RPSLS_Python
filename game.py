from Players.human import Human
from Players.computer import Computer
from Players.player import Player


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Player()

    def choose_game_type(self):
        player_input = input('Press 1 for Single Player or 2 for Multiplayer')
        if player_input == 1:
            self.player_two = Computer()
        else:
            self.player_two = Human()

    @staticmethod
    def display_rules():
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rocks')

    def compare_gestures(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()