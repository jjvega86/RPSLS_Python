from player import Player


class Human(Player):
    def __init__(self, name, gestures, chosen_gesture):
        super().__init__(name, gestures, chosen_gesture)
