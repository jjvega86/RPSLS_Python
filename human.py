from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def choose_gesture(self):
        self.print_gesture_options()
        user_choice = input("Please choose your gesture!")
        int_choice = int(user_choice)
        return self.gestures[int_choice]






