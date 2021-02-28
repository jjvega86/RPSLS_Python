from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Human(input("What is your name?"))
        self.player_two = None  # Setting Player 2 equal to None, equivalent of no value. Will determine
        # using choose_game_type

    def choose_game_type(self):
        player_input = input('Press 1 for Single Player or 2 for Multiplayer')
        if player_input == '1':
            self.player_two = Computer('HAL')
        else:
            self.player_two = Human(input("What is your name?"))

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
        p1_chosen_gesture = self.player_one.choose_gesture()
        p2_chosen_gesture = self.player_two.choose_gesture()

        if p1_chosen_gesture.name in p2_chosen_gesture.loses_to:
            self.player_two.current_score += 1
            print('Player 2 wins the round!')
        elif p2_chosen_gesture.name in p1_chosen_gesture.loses_to:
            self.player_one.current_score += 1
            print('Player 1 wins the round!')
        else:
            print('Round is a tie!')

    def game_rounds(self):
        game_incomplete = True

        while game_incomplete:
            self.compare_gestures()
            if self.player_one.current_score == 3 or self.player_two.current_score == 3:
                game_incomplete = False

    def declare_winner(self):
        if self.player_one.current_score == 3:
            print('Player One wins!')
        else:
            print('Player Two wins!')

    def play_game(self):
        self.choose_game_type()
        self.display_rules
        self.game_rounds()
        self.declare_winner()






