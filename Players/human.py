from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.print_gesture_options()
        self.chosen_gesture = input("Please choose your gesture!")
        return self.chosen_gesture






