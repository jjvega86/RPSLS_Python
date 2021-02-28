from player import Player
import random


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        return random.choice(self.gestures)
