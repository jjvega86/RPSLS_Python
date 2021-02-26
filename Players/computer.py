from player import Player
from random import random


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        choice = random.randint(0, 4)
        self.chosen_gesture = self.gestures[choice]
        return self.chosen_gesture
